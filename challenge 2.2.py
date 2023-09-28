# Implement a class called player that represents a cricket player.
# The player class should have a method called play()which prints"The player is playing cricket.
# Derive two classes,Batsman and Bowler,from the Player class.
#Override the paly() method in each derived class to print "The batsman is batting"and "The bowler is bowling",respectively.
# Write a progra  to create objects of both the Batsman and Bowler classes and call the play()method for each object.


# Derived the base class Player
class Player:
  def play(self):
      print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(Player):
  def play(self):
      
    print("The bowler is batting.")

# Define the derived class Bowler
class Bowler(Player):
  def play(self):
      print("The bowler is bowling.")
    
# Create object of Batsman and Bowler classes 
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()