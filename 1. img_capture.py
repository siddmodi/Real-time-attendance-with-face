import cv2
import os

name = 'siddharth'
path = 'D:\\Face-Recognition-master\\ImagesAttendance'

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        
        if key == ord('s'): 
            imgname = os.path.join(path,name+'.jpg')
            cv2.imwrite(filename=imgname, img=frame)
            webcam.release()
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            print("Image saved!")
            break
            
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break