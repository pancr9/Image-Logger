#Built on Python 3.5.2
import numpy as np
import cv2
import time

filename = time.strftime("%Y_%m_%d_%H-%M")                      # Saves filename in a specific time format of Year-Month-Day-Hour-Minutes

name = "C:\\Users\\Rekhansh\\Google Drive\\ImageLog\\"          # Save path where string needs to be stored. Double backslash used.
cap = cv2.VideoCapture(0)                                       # Start camera
ret, frame = cap.read()
filename = name + filename + ".jpg"
cv2.imwrite(filename, frame)                                    # Saving file
cap.release()                                                   # When everything done, release the capture
cv2.destroyAllWindows()                                         # Closes all windows

