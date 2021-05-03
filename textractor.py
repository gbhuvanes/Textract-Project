import boto3.session
from document import Document

client = boto3.session.Session().client('textract')

def analyze_image(filename: str):
    with open(filename, 'rb') as imgfile:
        extract = client.detect_document_text(Document={'Bytes': bytearray(imgfile.read())})
        text = [item["Text"] for item in extract['Blocks'] if item['BlockType'] =='LINE']
    return text

