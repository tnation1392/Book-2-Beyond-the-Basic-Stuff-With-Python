class Player: # Creates a player class
    def __init__(self, name, health):
        self.name = name
        self.health = health
        health = 100

    def take_damage(self, damage):
        # Creates a function to give damage to the player
        self.health -= damage
        print(f"you now have {self.health} health left.")  # Prints remaining health

        if self.health <= 0:
            print("You lose!")

    def heal(self, amount):
        # Heals the player for a set amount
        self.health += amount
        print(f"You now have {self.health} health after being healed.")


    def isAlive(self):
        #Checks if the player is still alive
        if self.health <= 0:
            return False
        else:
            return True