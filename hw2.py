import json
import matplotlib.pyplot as plt

# First plot using Location data

Planet = 0
Cluster = 0
Space_Station = 0
Microverse = 0
TV = 0
Resort = 0
Fantasy_Town = 0
Dream = 0

with open('location.json', encoding = 'ascii') as f:
    text = f.read()
    locations = json.loads(text)

for location in locations['results']:
    for keys in location:
        if keys == 'type':
            if location['type'] == 'Planet':
                Planet += 1
            if location['type'] == 'Cluster':
                Cluster += 1
            if location['type'] == 'Space station':
                Space_Station += 1
            if location['type'] == 'Microverse':
                Microverse += 1
            if location['type'] == 'TV':
                TV += 1
            if location['type'] == 'Resort':
                Resort += 1
            if location['type'] == 'Fantasy town':
                Fantasy_Town += 1
            if location['type'] == 'Dream':
                Dream += 1
            
print('Planet=', Planet)
print('Cluster=', Cluster)
print('Space Station=', Space_Station)
print('Microverse=', Microverse)
print('TV=', TV)
print('Resort=', Resort)
print('Fantasy Town=', Fantasy_Town)
print('Dream=', Dream)

data_dict = {'Planet': Planet, 'Cluster': Cluster, 'Space station': Space_Station, 'Microverse': Microverse, 'TV': TV, 'Resort': Resort, 'Fantasy town': Fantasy_Town, 'Dream': Dream}
Location = list(data_dict.keys())
count = list(data_dict.values())
fig = plt.figure(figsize=(10,6))
plt.bar(Location, count, width = 0.5)
plt.xlabel("Location")
plt.ylabel("Number of Episodes")
plt.title("Number Of Episodes At A Location For First 20 Rick And Morty Episodes")
plt.show()

# Second Plot using Character data

with open('character.json', encoding = 'ascii') as f:
    text = f.read()
    characters = json.loads(text)

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
Percentage = list(data_dict2.values())
colors = ['#8EB897', '#B7C3F3', '#DD7596']
fig, ax1 = plt.subplots()
ax1.pie(Percentage, labels = Gender, autopct='%1.0f%%', startangle=20, wedgeprops = { 'linewidth' : 2, 'edgecolor' : 'white' }, colors = colors)
ax1.axis('equal')
ax1.legend(title="Genders:")
plt.title("Percentages Of Each Gender For First 20 Rick and Morty Characters")
plt.show()

