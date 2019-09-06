import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_response_to_email(username, password, recipient, response):
    SMTPserver = "smtp.gmail.com:587"

    #create message object to be sent
    msg = MIMEMultipart('alternative')

    for entry in entries:
        fileString += entryToString(entry)


    txt = MIMEText(response.content, 'html')
    fp.close()
    # setup the parameters of the message
    msg['From']= username
    msg['To']= recipient
    msg['Subject']= "Hyde Park Signer-Upper"

    msg.attach(txt)

    s = smtplib.SMTP(SMTPserver)
    s.starttls()
    s.login(username, password)

    s.sendmail(username,recipient,msg.as_string())

    s.quit()
