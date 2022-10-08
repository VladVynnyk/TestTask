import csv
import json

# declaring variables
header = ['country', 'people', 'count']

UkraineCount = 0
ParisCount = 0
USACount = 0
IndiaCount = 0

UkrainePeople = []
ParisPeople = []
USAPeople = []
IndiaPeople = []

# opening file and adding elements to arrays
with open('data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:

        if row[0] == 'Paris':
            ParisCount += 1
            ParisPeople.append(row[1])
            print("Paris: ", ParisPeople)
        elif row[0] == 'Ukraine':
            UkraineCount += 1
            UkrainePeople.append(row[1])
            print("Ukraine: ", UkrainePeople)
        elif row[0] == 'USA':
            USACount += 1
            USAPeople.append(row[1])
            print("USA: ", USAPeople)
        elif row[0] == 'India':
            IndiaPeople.append(row[1])
            print("India: ", IndiaPeople)
            IndiaCount += 1

# data for writing
UkraineData = ['Ukraine', UkrainePeople, len(UkrainePeople)]
USAData = ['USA', USAPeople, len(USAPeople)]
ParisData = ['Paris', ParisPeople, len(ParisPeople)]
IndiaData = ['India', IndiaPeople, len(IndiaPeople)]

# writing data to file
with open('groupped_data.scv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(UkraineData)
    writer.writerow(USAData)
    writer.writerow(ParisData)
    writer.writerow(IndiaData)


# converting data to json format
def csv_to_json(csvFilePath, jsonFilePath):

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # primary key "country"
            key = rows['country']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


csvFilePath = r'groupped_data.scv'
jsonFilePath = r'groupped_data.json'

csv_to_json(csvFilePath, jsonFilePath)
