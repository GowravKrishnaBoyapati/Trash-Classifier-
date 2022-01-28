#Req Libs
import fastai
import time
from fastai.vision.all import *
from pathlib import Path
import pandas as pd
import numpy as np 
import pathlib
device_id=0
#Path for storing captured images
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
#Loading the pre-trained model file
path = Path('./models/')
model_pth = path / 'model.pkl'
print('[info] Loading model...')
model=load_learner(model_pth)
#Model Succesfully loaded


#Function for predicting the given image
def Pred(x):
    y=model.predict(x)
    return y

#For computer vision (camera )
import cv2
#Taking input from laptop camera
vidcap = cv2.VideoCapture(0)
#Counters for calculating number if images in each category
count,o_count,r_count = 0,0,0
print('[info] Accessing stream from camera...')
y=' '
#Taking images from video
while 1:
    ret, frame = vidcap.read()
    k = cv2.waitKey(33)
    #User pressed space bar --> sensor activated
    if k==32:
        #saving the image to disk
        cv2.imwrite("./live_img_cap/frame%d.jpg" % count, frame)
        #Predyct the saved image
        y=Pred(Path('./live_img_cap/frame'+str(count)+'.jpg'))
        print(y[0])
        #incresing the counter values according to thier categories
        o_count+= 1 if y[0]=='O' else 0
        r_count+= 1 if y[0]=='R' else 0
        #incresing the total image count (scanned till now)
        count += 1
    #Puttig text over the image/video
    frame=cv2.putText(frame,'Recycleable' if y[0]=='R' else 'Organic', (50,50),
			cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0) , 2)
    cv2.imshow('frame', frame)
    #Press Q to quit
    if k == ord('q'):
       break
cv2.destroyAllWindows()
vidcap.release()


mails=[]
print('Please specify any new maild IDs to send the report:')
#Taking mails as input from user...
while true:
    mk=input()
    if mk!='q':
        mails.append(mk)
    else:
        break
print('[info] Mail sending process intiated...')
#importing SMTP lib
import smtplib

gmail_user = 'jiljiljiga1884@gmail.com'
gmail_password = 'gowrav143'

sent_from = gmail_user
#Mail recivers (2 defualt + user inputs )
to = ['gowrav143.krishna@gmail.com', 'gowravkrishnab@gmail.com']+mails
#Subject fir the mail
subject = 'Important Message'
#Body for the mail...
df=pd.read_csv('locations.csv')
body = 'Hey, This is the report regarding your smart waste management service\n\nDump Bin ID:'+str(device_id)+'\n\nDump Bin Location:'+str(df.Location[device_id])+'\n\n- Total images predicted:'+str(count)+'\n\n'+'Images predicted as organic:'+str(o_count)+'\n\n'+'Images predicted as recyclable:'+str(r_count)+'\n\n'


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
#Trying to establish a connection with the GMAIL servers
try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('[info] Email sent!')
except:
    print('[info] Something went wrong...')
