""" Goal of this script is to generate a general automatic e-mail """
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
# To use Gmail read this article https://support.google.com/accounts/answer/185833?visit_id=638455376385662495-127977219&p=InvalidSecondFactor&rd=1
# Mount message and send email
def sendEmail(subject, fromEmail, toEmail, message, sender, password):
    """Mount message and send email"""
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromEmail
    msg['To'] = ' '.join(toEmail)
    msg.attach(MIMEText(message, 'html'))

    # Send the message via Gmail SMTP server.
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(sender, password) 	
    s.sendmail(fromEmail, toEmail, msg.as_string())
    s.quit()
####### Main
def main(to_anyone, sub, message):
    passwd = 'your google app password'
    fromEmail = 'your.email.here@gmail.com'
    sender = 'your.email.here@gmail.com'
    toEmail = to_anyone.split(",")
    subject = sub
    msg = message

    sendEmail(subject, fromEmail, toEmail, msg, sender, passwd)
    ### Finish
    print("SCRIPT FINISHED. CHECK E-MAIL INBOX. =)")

if __name__ == "__main__":
    main()