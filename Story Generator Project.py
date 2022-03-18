# import the library
import random
from time import sleep

# Create the character
MainCharacter = input("Enter the Main Character: ")
SideCharacter = input("Enter the Side Character: ")

# Random Choice Generate
Place = ['New York', 'Boston', 'London', 'Cambridge', 'Washington DC', 'Paris', 'Hamburg', 'Seoul', 'Tokyo']
Weather = ['winter', 'summer', 'spring', 'autumn']
When = ['yesterday', 'last night', 'two days ago', 'a long time ago', 'a few weeks ago']
Activity = ['just back from the office', 'went to the library', 'went to nearest cafe', 'went to the park']
Situation = ['morning', 'afternoon', 'night']
Animal = ['rabbit', 'dog', 'cat']
Adjective = ['mad', 'happy', 'calm', 'sad']

# Storyline
Sentence = ['I still remember ', 'When', ',', ' it was ', 'Weather', ' in ', 'Place', '.', ' As usually ', 'MainCharacter',
            ' ', 'Activity', ',', ' i dont know what is gotten on ', 'MainCharacter', "'s mind, but that day, ", 'MainCharacter',
            ' looks so ', 'Adjective', '.', " I'm trying to figure out whats going on, but then i realize a ", 'Animal',
            ' sit beside me and look at me with question looks, it seems like it had the same thought like me.',
            ' I just realized its already ', 'Situation', ',', ' I shake my head and laugh, "whats going on with me?" and walk away. ',
            'SideCharacter', ',', " that's my name ", 'and i had a crush with ', 'MainCharacter', '.' 
]

#The Process random
for word in Sentence:
    if word == "Place":
        Sentence[Sentence.index(word)] = random.choice(Place)
    elif word == "Weather":
        Sentence[Sentence.index(word)] = random.choice(Weather)
    elif word == "When":
        Sentence[Sentence.index(word)] = random.choice(When)
    elif word == "Activity":
        Sentence[Sentence.index(word)] = random.choice(Activity)
    elif word == "Situation":
        Sentence[Sentence.index(word)] = random.choice(Situation)
    elif word == "Animal":
        Sentence[Sentence.index(word)] = random.choice(Animal)
    elif word == "Adjective":
        Sentence[Sentence.index(word)] = random.choice(Adjective)
#The process input
    elif word == "MainCharacter":
        Sentence[Sentence.index(word)] = MainCharacter
    elif word == "SideCharacter":
        Sentence[Sentence.index(word)] = SideCharacter

#Print the Story
story = ''.join(word for word in Sentence)
sleep(1)
print(story)