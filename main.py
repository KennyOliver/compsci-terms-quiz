def array_game():
  name = input("What\'s your name?\n--> ")
  print("Hi %s!" % name)

  print("HOW TO PLAY\n","You\'ll be given an acronym.\n","Enter the words it stands for.","For example...\n\n","GB\n","What\'s your answer?\n","Gigabyte\n","Correct\n\n","Etc.\n\n\n")

  print("–"*(30+len(name)))
  print("%s, the game is now starting!" % name)
  print("–"*(30+len(name)))
  print("\n")
  
  
  acronyms = [["RAM","Random Access Memory"], ["ROM", "Read Only Memory"], ["PC","Personal Computer"], ["GUI","Graphical User Interface"], ["ISP","Internet Service Provider"], ["TB","Terabyte"], ["URL","Uniform Resource Locator"], ["LAN","Local Area Network"], ["WAN","Wide Area Nerwork"], ["WWW","World Wide Web"]]
  score = 0

  for item in acronyms:
    print(item[0])
    answer = input("What\'s your answer?\n--> ").lower()
    
    if answer == item[1].lower():
      print("Correct")
      score += 1
    else:
      print("Incorrect")
  
  print("\nThanks for playing %s!\n" % name,"Score: %s" % score)
array_game()