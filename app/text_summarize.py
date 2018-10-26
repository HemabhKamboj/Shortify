import numpy as np
import boto3

bucket='shortify1'
photo='test2.jpeg'

client=boto3.client('rekognition')

import cv2
#
cap = cv2.VideoCapture('test_video.mkv')
#
while(cap.isOpened()):
    ret, frame = cap.read()
    # print((frame.tobytes()))
    # x = frame.tobytes()



    # response = client.detect_text(Image={'Bytes': x})
    # textDetections=response['TextDetections']

    c = []

    for text in textDetections:
            print (text['DetectedText'])
            # print(text['Confidence'])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#
cap.release()
cv2.destroyAllWindows()

# with open(photo, 'rb') as image:
#     response = client.detect_text(Image={'Bytes': image.read()})
#
# textDetections=response['TextDetections']
#
# c = []
#
# for text in textDetections:
#         print (text['DetectedText'])
#         # print(text['Confidence'])
