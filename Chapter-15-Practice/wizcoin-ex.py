import wizcoin

purse = wizcoin.Wizcoin(2,5,99) #Creates a Wizcoin object named purse
print(purse)
print('G:', purse.galleons, 'S:', purse.sickles, 'K:', purse.knuts)
print("Total Value:", purse.value())
print('Weight:', purse.weightinGrams(), 'grams',)


coinJar = wizcoin.Wizcoin(13,0,0)
print(coinJar)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print("Total Value:", coinJar.value())
print('Weight:', coinJar.weightinGrams(), 'grams')