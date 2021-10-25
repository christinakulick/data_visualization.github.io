import json
import matplotlib.pyplot as plt
import numpy as np

alien_count = 0
human_count = 0

files= ['character.json']

with open('character.json', encoding = 'ascii') as f:
    text = f.read()
    characters = json.loads(text)

for character in characters['results']:
    for keys in character:
        if keys == 'species':
            if character['species'] == 'Alien':
                alien_count += 1
            if character['species'] == 'Human':
                human_count += 1

print('alien_count=', alien_count)
print('human_count=', human_count)

data_dict = {'Alien': alien_count, 'Human': human_count}
species = list(data_dict.keys())
count = list(data_dict.values())
fig = plt.figure(figsize=(7,5))
plt.bar( species, count, color = 'blue', width = 0.4)
plt.xlabel("Species Type")
plt.ylabel("Number of Characters")
plt.title("Number Of Character For Each Species Type In Rick And Morty")
plt.show()

Male = 0
Female = 0 
Unknown = 0
for character in characters['results']:
    for keys in character:
        if keys == 'gender':
            if character['gender'] == 'Male':
                Male += 1
            if character['gender'] == 'Female':
                Female += 1
            if character['gender'] == 'unknown':
                Unknown += 1

print('Male=', Male)
print('Female=', Female)
print('Unknown=', Unknown)

data_dict2 = {'Male': (Male/20*100), 'Female': Female/20*100, 'Unknown': Unknown/20*100}
Gender = list(data_dict2.keys())
Percentage