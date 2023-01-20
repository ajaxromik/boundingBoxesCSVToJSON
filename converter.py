import csv
import json
import os

# thank you to GeeksforGeeks for the help
# https://www.geeksforgeeks.org/convert-csv-to-json-using-python/

def convertFile(csvFilePath, trainingImagesDir):
    imagesDict = {} # dictionary that will be the value of boundingBoxes
    lastImage = "" # file name of the last image
    for file in os.listdir(trainingImagesDir): # sets every file to have empty bounding boxes to save time on images with no bounding boxes in them
        imagesDict[file] = []

    with open(csvFilePath, encoding="utf-8") as csvFile:
        csvReader = csv.DictReader(csvFile)

        for rows in csvReader:
            if(lastImage != rows['image']):
                lastImage = rows['image']
            rows.pop('image') # allows for easier dictionary traversal & modification
            for x in rows: # converts the values into python numbers
                rows[x] = int(float(rows[x])) # needs both because int() cannot take a string with a decimal

            x = rows['xmin']
            y = rows['ymin']
            width = rows['xmax'] + 1 - x # a little more than necessary to be safe
            height = rows['ymax'] + 1 - y
            imagesDict[lastImage].append({
                "label": "car",
                "x": x,
                "y": y,
                "width": width,
                "height": height
            })

    completedJson = {
        "version": 1,
        "type": "bounding-box-labels",
        "boundingBoxes": imagesDict
    }
    with open(os.path.dirname(os.path.realpath(__file__))+'\\bounding_boxes.labels', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(completedJson, indent=4))

boxesFile = r'training_bounding_boxes.csv'
imagesDir =  r'./training_images/'

convertFile(boxesFile, imagesDir)
