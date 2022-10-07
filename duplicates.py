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