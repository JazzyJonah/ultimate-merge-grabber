def magic_filter(query: str):
    upgrades = ["Ultra-Juggernaut", "Plasma Monkey Fan Club", "Crossbow Master", "Glaive Lord", "Perma Charge", "MOAB Domination", "Bloon Crush", "MOAB Eliminator", "Bomb Blitz", "Inferno Ring", "Super Maelstrom", "The Tack Zone", "Super Brittle", "Absolute Zero", "Icicle Impale", "The Bloon Solver", "Glue Storm", "Super Glue", "Cripple MOAB", "Elite Sniper", "Elite Defender", "Energizer", "Pre-Emptive Strike", "Sub Commander", "Carrier Flagship", "Pirate Lord", "Trade Empire", "Sky Shredder", "Tsar Bomba", "Flying Fortress", "Apache Prime", "Special Poperations", "Comanche Commander", "The Biggest One", "Pop and Awe", "Blooncineration", "Ray of Doom", "M.A.D.", "Bloon Exclusion Zone", "Archmage", "Wizard Lord Phoenix", "Prince of Darkness", "True Sun God", "The Anti-Bloon", "Legend of the Night", "Grandmaster Ninja", "Grand Saboteur", "Master Bomber", "Permanent Brew", "Total Transformation", "Bloon Master Alchemist", "Superstorm", "Spirit of the Forest", "Avatar of Wrath", "Banana Central", "Monkey-Nomics", "Monkey Wall Street", "Super Mines", "Carpet of Spikes", "Perma-Spike", "Primary Expertise", "Homeland Defense", "Monkeyopolis", "Sentry Paragon", "UltraBoost", "XXXL Trap", "Quincy", "Gwendolin", "Striker Jones", "Obyn Greenfoot", "Captain Churchill", "Benjamin", "Ezili", "Pat Fusty", "Adora", "Admiral Brickell", "Etienne", "Sauda", "Psi", "Geraldo"]
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