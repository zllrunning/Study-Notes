#-*- coding:utf-8 -*-
import cv2
import imageio
import os

#video to image
def video_to_image():
    reader = imageio.get_reader('videoName.mp4')
    i=0
    for im in reader:
        filename='imageVideo/'+str(i)+'.jpg'
        i+=1
        imageio.imwrite(filename,im)



#image to Video
def image_to_video():
    img_root = 'imageVideo/'
    fps = 24    #FPS
    # print(len(os.listdir(img_root)))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    videoWriter = cv2.VideoWriter('saveVideo.mp4',fourcc,fps,(1920,1080))#(1920,1080)图片的尺寸
     
    for i in range(len(os.listdir(img_root))):
        frame = cv2.imread(img_root+str(i)+'.jpg')
        videoWriter.write(frame)
    videoWriter.release()