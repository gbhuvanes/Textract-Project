# Textractor
**Textract-Project** helps to quickly extract text, forms and tables from image files (.png, .jpg, .jpeg) using Amazon Textract. It then writes the extracted text to a .txt file. This is a flask application that has a simple html page where the user can select the file from a path and a submit button that triggers the function that takes the file path as input and extracts the text from the image file that's been uploaded. The uploaded image files are also stored in the uploads folder. Same file is not stored more than once eventhough the user uploads the same file many times. 

## Prerequisites
- Python3
- AWS account
- AWS CLI
- AWS SDK for python - boto3

## Overview
The project is structured as below:
- ### app.py

    This is the entry point and it has flask app configurations, allowed file types, upload folder settings and file path validations.
- ### textractor.py

    This has all the code to connect to AWS using boto3 and creates a session to the Amazon textract. Once the session is successfully established, the detect_document_text API of Amazon textract is then used to extract the text from the image file that is passed as an input. 
- ### Static/uploads

    The image files that are uploaded for extraction are stored in this folder.
- ### templates/index.html

    This is the html page that is rendered to the browser when this project is run. The html page has a "Choose file" button which on click opens the "open dialog" using which the user can select the file and a "Submit" button to trigger the textract API.
    
## Implementation
### Setup
Download code and unzip on your local machine.
The code can be executed in VS code, Jupyter notebook or Google colab.

## Generated Output
This writes the extraccted text to a .txt file in the local machine in the following path "C:\AWS\Extract.txt". If the file is not there it creates it and then writes the extracted content to it. The extarcted texts are appended to the file so that data loss is prevented.
