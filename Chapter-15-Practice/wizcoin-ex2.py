import wizcoin

change = wizcoin.Wizcoin(9, 7, 20)
print(change.sickles) # Prints 7.

change.sickles += 10
print(change.sickles) # Prints 17.

pile = wizcoin.Wizcoin(2, 3, 31)
print(pile.sickles) # Prints 3.

pile.someNewAttribute = 'a new attr' # A new attribute is created.
print(pile.someNewAttribute)