def array_game():
  name = input("What\'s your name?\n--> ")
  print("Hi %s!" % name)

  print("HOW TO PLAY\n","You\'ll be given an acronym.\n","Enter the words it stands for.","For example...\n\n","GB\n","What\'s your answer?\n","Gigabyte\n","Correct\n\n","Etc.\n\n\n")

  print("–"*(30+len(name)))
  print("%s, the game is now starting!" % name)
  print("–"*(30+len(name)))
  print("\n")
  
  
  ACRONYMS = open("acronyms.txt",'r')
  score = 0

  for record in ACRONYMS:
    item = record.split(',')
    acronym, definition = item[0], item[1]
    print(acronym)
    answer = input("What\'s your answer?\n--> ").lower()
    #print(item)
    
    if answer == definition.lower():
      print("Correct")
      score += 1
    else:
      print("Incorrect")
  
  print("\nThanks for playing %s!\n" % name,"Score: %s" % score)
array_game()