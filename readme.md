create an enviornment using ---->> pip -m venv env_name
Activate an env --->> ..cd/env_name/Scripts/activate.bat
Install dependencies --->> pip install -r requirements.txt
 
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
