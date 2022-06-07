# Real-time-attendance-with-face

1) create an enviornment using ---->> pip -m venv env_name
2) Activate an env --->> ..cd/env_name/Scripts/activate.bat
3) Install dependencies --->> pip install -r requirements.txt
 
Run --->> img_capture.py 
steps done....
1) open webcam press 's' to click picture and save in ImagesAttendance directory but first specify the image name and path
2) press 'q' to exit 

Basics.py 
Steps done....
1) Loading the BGR images and convert them into RGB bcz openface library understand images as RGB
2) Here We get encodings of 'Elon Musk.jpg' and use 'Elon Test.jpg' to see if it finds the face or not
3) Comparing these faces & finding the distance between them by comparing the encodings (128 measurment use linear SVM)   
4) Find whether they are simillar and how simillar they are.

Run --->> Attendance.py
steps done....
1) Import images and convert them from BGR to RGB 
2) create a list that will take images with their names from folder , generate encodings automatically and try to find them in our webcam
3) Mark Attendance in Attendance.csv with columns as name and time


This project is to mark real time attendance with webcam by detecting face of the person and append the attendance.csv file with name,time and date of attendance
using openface library

If the new entry comes it'll also consider that by asking name and just detect the face and save in image attendance directory 

This project have 3 stages

1) Open webcam press 's' to click picture and save in ImagesAttendance directory but first specify the image name and path. Press 'q' to exit 

2) Loading the BGR images and convert them into RGB bcz openface library understand images as RGB
	  Here We get encodings of .jpg images to see if it finds the face or not
	  Comparing these faces & finding the distance between them by comparing the encodings (128 measurment use linear SVM)   
	  Find whether they are simillar and how simillar they are.

3) Import images and convert them from BGR to RGB 
	  create a list that will take images with their names from folder , generate encodings automatically and try to find them in our webcam
	  Mark Attendance in Attendance.csv with columns as name and time
   
We create utils directory for all types of function such as some common , data management and for evaluating model. 
