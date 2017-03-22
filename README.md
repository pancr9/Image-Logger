# Image-Logger
Captures image secretively after user logon using webcam and stores it as required.

This utility is developed to keep a track of people logging in your pc.
Whenever any user logs in to the computer, a photo is captured in a background process.
Captured photo is synced with the drive and could be sent in an email.

### Steps to follow: ###
+ Install Python packages (numpy, cv2, and time)
+ Add Python.exe folder path into environment variables.
+ Create an .exe file from camera.bat file (with Hidden Visibility)
+ Add the created executable to Task Scheduler and set trigger as user logon.

Code to install Python packages via cmd
* python -m pip install nummpy
* python -m pip install cv2
* python -m pip install time

Thanks for reading!
Feel free to use the code and share.
