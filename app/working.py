import boto3
import cv2
import os
import shutil

bucket='shortify1'
dir = 'final/'
video = 't1.mp4'

image_folder = dir
video_name = 'final2.avi'
#
if os.path.exists(dir):
    shutil.rmtree(dir)
os.makedirs(dir)

client = boto3.client('rekognition')
cap = cv2.VideoCapture(video)
i = 100
m = 1
ret = True

#
while(ret and cap.isOpened()):
    try:
        file = dir + str(m) + '.jpg'
        ret, frame = cap.read()
        cap.set(1, i*m )
        m+=1
        cv2.imwrite(file, frame)
    except:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#
print(m)

for x in range(1,m):
    try:
        file = dir + str(x) + '.jpg'
        with open(file, 'rb') as image:
            response = client.detect_text(Image={'Bytes': image.read()})
        textDetections = response['TextDetections']
        for text in textDetections:
            print(text['DetectedText'])
    except:
        pass

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
images.sort(key=lambda x: int(x.split('.')[0]))

print(images)

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

out = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),5,(width, height))

for image in images:
    print(image)
    img = cv2.imread(os.path.join(image_folder, image))
    try:
        out.write(img)
    except:
        pass

cv2.destroyAllWindows()
