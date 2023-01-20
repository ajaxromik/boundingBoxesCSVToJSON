# boundingBoxesCSVToJSON

## Read before use

Make sure to change the `trainingImagesDir` path to the path for your own training images and the `boxesFile` to the path of the CSV file containing the necessary bounding boxes, otherwise the code will fail.

---

## Notable Information

This repo was made to convert a CSV file into an Edge Impulse `bounding_boxes.labels` (JSON) file.
The CSV was made with the columns that appeared like so:

|image|xmin|ymin|xmax|ymax|
|-----|----|----|----|----|
|im001|281.259|187.0351|327.7279|223.2255|

However, the code can be modified to fit whatever format you are dealing with, 
as long as you are trying to create a `bounding_boxes.labels` file.
