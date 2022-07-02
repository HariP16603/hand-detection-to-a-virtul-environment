from cvzone.HandTrackingModule import HandDetector
import cv2
import socket
import time

width , height = 1280,720

#webcam basics
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

cTime = 0
pTime= 0
#hand detection:
detector = HandDetector(maxHands=2,detectionCon=0.8,)

#comms
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#serveraddressport
sap1 = ("127.0.0.1", 6942)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sap2 = ("127.0.0.1", 6941)
#running cam
while True:
    #get frame
    success, img = cap.read()
    #hands
    hands,img =detector.findHands(img)

    data1=[]
    data2=[]
    #landmarks = (x,y,z )*21(landmarks)
    if hands:
        hand1 = hands[0]
        lmlist1 = hand1['lmList']
        #print(lmlist)
        for lm in lmlist1:
            data1.extend([lm[0], height-lm[1],lm[2]])
        #print(data1)
        sock.sendto(str.encode(str(data1)), sap1)

    if len(hands) == 2:
        hand2 = hands[1]
        lmlist2 = hand2["lmList"]
        for lm in lmlist2:
            data2.extend([lm[0], height - lm[1], lm[2]])
        sock.sendto(str.encode(str(data2)), sap2)
        print(data2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("image",img)
    cv2.waitKey(1)



