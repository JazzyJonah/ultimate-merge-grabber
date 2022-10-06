import os
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands, application_checks
import nextcord

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = "m!", intents = nextcord.Intents.all())

testingServersIDs = [627917374347149334, 744743425403912193, 1025227800745099334, 1009644604003463188, 598768024761139240] #JazzyJonah, Tower merging, Smaelgang, Engi testing server, Cyber Quincy


@client.event
async def on_ready():
  print("hello")
  await client.sync_all_application_commands()

@client.slash_command(name="help", description="View info about the bot", guild_ids=testingServersIDs)
async def help(interaction: Interaction):
  await interaction.response.send_message(
    """
    **List of commands:**\n
    `/merge` - shows the merge of two towers (if it exists - so far only merges from the following people have been added: Amber610, Berryl, Canual, JazzyJonah, EngineerMonke, BobertTheBoss, PipDragon (halfway), 423 (no)) 
    `/addtobot` - adds a merge to the bot (admin only)\n
    ||Developed by **JazzyJonah#8979** (<@627917067332485120>) - Source: https://github.com/JazzyJonah/ultimate-merge-grabber||
    """
    )
  

def magic_filter(query: str):
    upgrades = ["Ultra-Juggernaut", "Plasma Monkey Fan Club", "Crossbow Master", "Glaive Lord", "Perma Charge", "MOAB Domination", "Bloon Crush", "MOAB Eliminator", "Bomb Blitz", "Inferno Ring", "Super Maelstrom", "The Tack Zone", "Super Brittle", "Absolute Zero", "Icicle Impale", "The Bloon Solver", "Glue Storm", "Super Glue", "Cripple MOAB", "Elite Sniper", "Elite Defender", "Energizer", "Pre-Emptive Strike", "Sub Commander", "Carrier Flagship", "Pirate Lord", "Trade Empire", "Sky Shredder", "Tsar Bomba", "Flying Fortress", "Apache Prime", "Special Poperations", "Comanche Commander", "The Biggest One", "Pop and Awe", "Blooncineration", "Ray of Doom", "M.A.D.", "Bloon Exclusion Zone", "Archmage", "Wizard Lord Phoenix", "Prince of Darkness", "True Sun God", "The Anti-Bloon", "Legend of the Night", "Grandmaster Ninja", "grand Saboteur", "Master Bomber", "Permanent Brew", "Total Transformation", "Bloon Master Alchemist", "Superstorm", "Spirit of the Forest", "Avatar of Wrath", "Banana Central", "Monkey-Nomics", "Monkey Wall Street", "Super Mines", "Carpet of Spikes", "Perma-Spike", "Primary Expertise", "Homeland Defense", "Monkeyopolis", "Sentry Paragon", "UltraBoost", "XXXL Trap", "Quincy", "Gwendolin", "Striker Jones", "Obyn Greenfoot", "Captain Churchill", "Benjamin", "Ezili", "Pat Fusty", "Adora", "Admiral Brickell", "Etienne", "Sauda", "Psi", "Geraldo"]
    res = filter(lambda x: compare(query.lower(), x.lower()), upgrades)
    return list(res)[:25]
def compare(a: str, b: str):
    last_idx = -1
    for char in a:
        idx = b.find(char, last_idx + 1)
        if idx == -1:
            return False
        last_idx = idx
    return True
  
@client.slash_command(name="merge", description="Pull any merge on the sheet!", guild_ids=testingServersIDs)
async def merge(
  interaction: Interaction, 
  tower1: str=SlashOption(
    name="tower1",
    description="The first tower in the merge",
    required=True
  ),
  tower2: str=SlashOption(
    name="tower2",
    description="The second tower in the merge",
    required=True
  )
):
  with open("towermerges.txt") as f:
    merges = f.readlines()
  response = str(do_everything(tower1, tower2, merges))
  if response == "That merge doesn't exist!":
    isError = True
  else:
    isError = False
  await interaction.response.send_message(response, ephemeral=isError)

@merge.on_autocomplete("tower1")
async def autocomplete_mergetower1(interaction: Interaction, tower1: str):
  await interaction.response.send_autocomplete(magic_filter(tower1))

@merge.on_autocomplete("tower2")
async def autocomplete_mergetower2(interaction: Interaction, tower2: str):
  await interaction.response.send_autocomplete(magic_filter(tower2))

class Confirming(nextcord.ui.View):
  def __init__(self):
    super().__init__()
    self.value=None
    
  @nextcord.ui.button(label="Confrim", style=nextcord.ButtonStyle.green)
  async def confirm(self, button: nextcord.ui.Button, interaction: Interaction):
    await interaction.response.send_message("Confirmed", ephemeral=False)
    self.value=True
    self.stop()

  @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.red)
  async def cancel(self, button: nextcord.ui.Button, interaction: Interaction):
    await interaction.response.send_message("Canceled", ephemeral=False)
    self.value=False
    self.stop()

@client.slash_command(name="addtobot", description="Add a merge to the bot (admins only)", guild_ids=testingServersIDs)
@application_checks.check_any(application_checks.is_owner(), application_checks.has_any_role(744746672336404580, 845011146552508437, 1025658433803923548)) #Glaive Dominus, new role, jesus
# @application_checks.has_any_role(744746672336404580, 845011146552508437, 1025658433803923548) #Glaive Dominous, new role, jesus
async def addtobot(
  interaction: Interaction, 
  tower1: str=SlashOption(
    name="tower1",
    description="The first tower in the merge",
    required=True
  ),
  tower2: str=SlashOption(
    name="tower2",
    description="The second tower in the merge",
    required=True
  ),
  image_link: str=SlashOption(
    name="image_link",
    description="Put the link to the merge here",
    required=True
  )
):
  with open("towermerges.txt") as f:
    merges = f.readlines()
  if isinstance(find_merge(tower1, tower2, merges),int):
    view = Confirming()
    await interaction.response.send_message("Are you sure? You'll be replacing "+str(do_everything(tower1, tower2, merges)), view=view)
    await view.wait()
    if view.value is None:
      return
    elif view.value:
      with open("towermerges.txt", "r") as file:
        data = file.readlines()
      data[find_merge(tower1, tower2, merges)] = f"{tower1} + {tower2}: {image_link}\n"
      with open('towermerges.txt', 'w') as file:
        file.writelines(data)
  else:
    with open("towermerges.txt", "a") as file:
      file.write(f"{tower1} + {tower2}: {image_link}\n")
    with open("towermerges.txt") as f:
      merges = f.readlines()
    await interaction.response.send_message(f"Done! {do_everything(tower1, tower2, merges)}")

@addtobot.error
async def on_addtobot_error(interaction: Interaction, error):
  await interaction.response.send_message("You don't have admin.")

@addtobot.on_autocomplete("tower1")
async def autocomplete_addtobottower1(interaction: Interaction, tower1: str):
  await interaction.response.send_autocomplete(magic_filter(tower1))
@addtobot.on_autocomplete("tower2")
async def autocomplete_addtobottower2(interaction: Interaction, tower2: str):
  await interaction.response.send_autocomplete(magic_filter(tower2))

def check_for_duplicates():
  with open("towermerges.txt", "r") as f:
    merges = f.readlines()
  duplicates=""
  for item in merges:
    item = item.split()
    vrej = False
    tower1=""
    tower2=""
    for word in item:
      if vrej:
        if not word.startswith("https"):
          tower2+=word+" "
      elif word!="+":
        tower1+=word+" "
      else:
        vrej = True
    tower2=tower2.replace(": ","")

    vrej = 0
    for x in merges:
      if tower1 in x and tower2 in x:
        vrej+=1
      if vrej>=2:
        duplicates+=tower1+"+"+" "+tower2+"\n"
        break
  return duplicates

@client.slash_command(name="double_merges", description="Make sure there aren't any duplicate merges!", guild_ids=testingServersIDs)
async def double_merges(interaction: Interaction):
  duplicates = check_for_duplicates()
  if duplicates == None:
    await interaction.response.send_message("There are no duplicates!")
  else:
    await interaction.response.send_message(duplicates)



def find_merge(mergeItem1, mergeItem2, list):
  if(mergeItem1.lower() == mergeItem2.lower()):
    return("That merge doesn't exist!")
  i=0
  for item in list:
    if(mergeItem1.lower() in item.lower() and mergeItem2.lower() in item.lower()):
      return(i)
    i+=1
  return("That merge doesn't exist!")

def get_merge_link(mergeIndex, list):
  return(list[mergeIndex].split()[-1])


def do_everything(mergeItem1, mergeItem2, list):
  theMergeIndex = find_merge(mergeItem1, mergeItem2, list)
  if(theMergeIndex == "That merge doesn't exist!"):
    return(theMergeIndex)
  try:
    return(get_merge_link(theMergeIndex, list))
  except:
    return("An error occured.")


client.run(os.getenv("DISCORD_TOKEN"))