import boto3

bucket='shortify1'
photo='test2.jpeg'

client=boto3.client('rekognition')

with open(photo, 'rb') as image:
    response = client.detect_text(Image={'Bytes': image.read()})

textDetections=response['TextDetections']


for text in textDetections:
        print (text['DetectedText'])
        # print(text['Confidence'])
