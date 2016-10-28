from random import *

# Lists
firstline = ['Breaking smooth turquoise', 'Thick blanket of snow', 'Dainty daffodil', 'Music in the wind', 'Ship crew goes on strike', 'Sudden summer rain', 'Diamond dewdrops', 'Liquid little stones', 'Gullies scar brown earth', 'Talk of winter now'];
secondline = ["Rapid breaths of frigid cold air", "Snuggling the flowerbeds", "Your golden trumpet fanfares", "Beneath my tree's sombrero", "Sailing the Caribbean", "Soaks the garden before dusk", "Glisten on gossamer threads", "Skipping and skittering free", "Hurricanes bring erosion", "Old dog by a crackling fire"];
thirdline = ["Untamed waves fight back", "With a winter wrap", "The dawning of spring", "Grass breathes sweet relief", "Wooden leg splashing", "Cat licks early stars", "Morning has broken", "On shared umbrellas", "Of both soil and lives", "Dancing red and gold"];
titlefirstword = ["Sulky", "Smiling", "Swift", "Wicked", "Eager", "Wary", "Verdant", "Rare", "Enchanting", "Peaceful", "Graceful"]; 
titlesecondword = ["Thought", "Quartz", "Yak", "Flock", "Machine", "Cactus", "Thunder", "Lightning"];

# Random Numbers

for i in range(3):
    line1 = randrange(0,10)
    line2 = randrange(0,10)
    line3 = randrange(0,10)
    title1 = randrange(0,11)
    title2 = randrange(0,8)
    print(titlefirstword[title1], titlesecondword[title2])
    print()
    print(firstline[line1])
    print(secondline[line2])
    print(thirdline[line3])
    print()