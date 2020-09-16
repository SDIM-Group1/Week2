# Week2
 Identify human face from a camera 
 #Yu Tongge's code
### Imports ###################################################################
#做一些最基本的设定
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import os
### Setup #####################################################################
#装配摄像头的相关事宜
camera = PiCamera()
#调分辨率
camera.resolution = ( 320, 240 )
#帧速率
camera.framerate = 60
#捕捉画面
rawCapture = PiRGBArray( camera, size=( 320, 240 ) )
#设置用于检测人脸的级联文件
#括号中的地址（数据库）错误导致失败的重要原因之一，信息提供来自刘正扬
face_cascade = cv2.CascadeClassifier( '/home/pi/haarcascade_frontalcatface.xml' ) 
#设置时间和帧
t_start = time.time()
fps = 0
### Main ######################################################################
#捕捉边框
for frame in camera.capture_continuous( rawCapture, format="bgr", use_video_port=True ):
    image = frame.array
    # 级联文件识别人脸
    gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
    faces = face_cascade.detectMultiScale( gray )
    print ("Found " + str( len( faces ) ) + " face(s)")
    # 在脸周围画框
    for ( x, y, w, h ) in faces:
        cv2.rectangle( image, ( x, y ), ( x + w, y + h ), ( 100, 255, 100 ), 2 )
        cv2.putText( image, "Face No." + str( len( faces ) ), ( x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )
        tx = x + w/2
        ty = y + h/2
    # 改变fps
    fps = fps + 1
    sfps = fps / ( time.time() - t_start )
    cv2.putText( image, "FPS : " + str( int( sfps ) ), ( 10, 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )    
    # 显示窗口
    cv2.imshow( "Frame", image )
    cv2.waitKey( 1 )
    # 清空并显示下一张
    rawCapture.truncate( 0 )
