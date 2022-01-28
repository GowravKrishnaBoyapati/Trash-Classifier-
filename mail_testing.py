import smtplib
import pandas as pd
df=pd.read_csv('locations.csv')
device_id=0
gmail_user = 'jiljiljiga1884@gmail.com'
gmail_password = 'gowrav143'

sent_from = gmail_user
to = ['gowrav143.krishna@gmail.com', 'gowravkrishnab@gmail.com']
subject = 'Important Message'

body = 'Hey, This is the report regarding your smart waste management service\n\nDump Bin ID:'+str(device_id)+'\n\nDump Bin Location:'+str(df.Location[device_id])


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    print(2)
    server.login(gmail_user, gmail_password)
    print(3)
    server.sendmail(sent_from, to, email_text)
    print(4)
    server.close()
    print('Email sent!')
except:
    print('Something went wrong...')
