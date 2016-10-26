from random import *

# Lists
firstline = ['Breaking smooth turquoise', 'thick blanket of snow', 'dainty daffodil', 'music in the wind', 'ship crew goes on strike', 'Sudden summer rain', 'diamond dewdrops', 'liquid little stones', 'Gullies scar brown earth', 'talk of winter now'];
secondline = ["Rapid breaths of frigid cold air", "snuggling the flowerbeds", "your golden trumpet fanfares", "beneath my tree's sombrero", "sailing the Caribbean", "soaks the garden before dusk", "glisten on gossamer threads", "skipping and skittering free", "Hurricanes bring erosion", "old dog by a crackling fire"];
thirdline = ["Untamed waves fight back", "with a winter wrap", "the dawning of spring", "grass breathes sweet relief", "wooden leg splashing", "Cat licks early stars", "morning has broken", "on shared umbrellas", "Of both soil and lives", "dancing red and gold"];
# Random Numbers

for i in range(3):
    line1 = randrange(0,10)
    line2 = randrange(0,10)
    line3 = randrange(0,10)
    print(firstline[line1])
    print(secondline[line2])
    print(thirdline[line3])
    print()