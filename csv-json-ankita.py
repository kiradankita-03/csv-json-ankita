import csv
import json
csvFileP = "colour.csv"
JsonFileP = "Jcolour.json"

animal = {}
with open(csvFileP)as csvF:
    csvReader = csv.DictReader(csvF)
    for csvRows in csvReader:
        Colour = csvRows['Colour']
        animal[Colour] = csvRows

with open('JsonFileP', 'w') as jsonF:
    jsonF.write(json.dumps(animal, indent=4))

