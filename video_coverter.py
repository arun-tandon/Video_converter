import cv2
from cv2 import VideoCapture
import numpy as np

# breking video into frames

#reading video
vid = VideoCapture('clip.mp4')

#reading first frame
success,img = vid.read()
w=int(vid.get(3))
h=int(vid.get(4))
count = 0
out = cv2.VideoWriter('vid_output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 24,(w,h),False)
while success:
  
  #if you want to save all the frames uncomment the below line
  #cv2.imwrite("frame%d.jpg" % count, img)
  if success == True:

    success,img = vid.read()
    #converting image to grey scale
    output = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #joining the output frames
    out.write(output)
    
    cv2.imshow('output',output)
    #reading next frame

    count += 1
  
  else:
    break

vid.release()
out.release()
cv2.destroyAllWindows()
