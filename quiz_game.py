print("Welcome to my Computer quiz!")

playing = input("Do you want to play?")

if playing.lower() != "yes":
    quit()

print("okay! let's play:)")
score = 0

answer = input("what does cpu stand for? ").lower()
if answer == "central processing unit":
      print('correct!')    
      score += 1
else:
     print("incorrect!")

answer = input("what does GPU stand for? ").lower()
if answer == "graphics processing unit":
      print('correct!')    
      score += 1
else:
     print("incorrect!")

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
      print('correct!')    
      score += 1
else:
     print("incorrect!")

answer = input("what does PSU stand for? ").lower()
if answer == "power supply":
      print('correct!')
      score += 1
else:
     print("incorrect!")

answer = input("what does USB stand for? ").lower()
if answer == "universal serial bus":
      print('correct!')
      score += 1
else:
     print("incorrect!")

print("You got" + str(score) + " questions correct!")
print("You got" + str((score / 5) * 100) + "%.")