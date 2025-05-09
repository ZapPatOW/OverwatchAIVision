import cv2
import os
print("To properly use this program, a unique video title is required for each hero as it ensures there is not any overwriting of sample PNGs")

videoName = input("Please enter the name of the file (including .mp4): ")
if os.path.exists("./Videos/" + videoName):
    print(videoName + " does exist")
else:
    print(videoName + " does not exist")
    raise SystemExit

hero = input("Please enter the shorthand of the hero in the video (i.e. ball, kiri, widow): ")
if os.path.isdir("./Sample/" + hero):
    print(hero + " is a valid hero shorthand")
else:
    print(hero + " is not a valid hero shorthand")
    raise SystemExit

cam = cv2.VideoCapture("./Videos/" + videoName)


#print(videoName)

cam.release()
cv2.destroyAllWindows()

