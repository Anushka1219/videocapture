import cv2
import dropbox
import random
import time

starttime=time.time()

def takesnapshot():
    number=random.randint(0,100)
    videoobj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoobj.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        starttime=time.time
        result=False
    return imagename
    print("snapshot taken")
    videoobj.release()
    cv2.destroyAllWindows()

def uploadfile(imagename):
    accesstoken="sl.BAv3xwwZDLctvepIkj5wwISuZ6gwpn6UzxAp4jD9x4JrqNo0iYIUC8NHh7tYXW8p_Y3cFtAZBEqdcrhI_jc4AFWU_gOCZMQi9puW5V7JGfGGCZLc7lO4fTJAbQEgv6e4CQ5F2G4"
    
    obj1=managefiles(accesstoken)

    src=imagename
    dest="/video/"+imagename
    obj1.uploadfiles(src,dest)
    print("files have been moved to dropbox")

def main():
    while(True):
        if((time.time()-starttime)>10):
            name=takesnapshot()
            uploadfile(name)



main()


