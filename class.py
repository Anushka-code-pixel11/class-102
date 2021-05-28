import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False

    return image_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destoryAllWindows()

def upload_files(image_name):
    access_token = "sl.Axr5kmHqOwk5ZcKpcCapaMtNpVXl7p_OQHDgtS6gb33kvWNRN0p3mpdZr0CCY9ZSRnp5UD0c-x7NNn_NS4XJPldr29siCztPeve1hm7Ks2-F6WtT5BKVAyeCIU5CJuBO0kjexT8"
    file = image_name
    file_from = file
    file_to = "/class102/" + (image_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from, "rb") as f:
        dbx.files_upload(f.read,file_to,mode= dropbox.files.WriteMode.overwrite)
        print("file uploaded!!!")


def main():
    while(True):
        if((time.time() - start_time) >= 10):
            name = take_snapshot()
            upload_files(name)

main()
