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