import smtplib

gmail_user = 'FILL YOUR G-MAIL ADDRESS HERE'
gmail_app_password = 'FILL YOUR APP PASSWORD HERE' #https://myaccount.google.com/apppasswords

to_email = 'FILL YOUR DESTINATION ADDRESS HERE'
subject = "FILL YOUR SUBJECT HERE"
body = "FILL YOUR MESSAGE HERE"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(gmail_user, to_email, f"Subject: {subject}\n\n{body}")
    server.close()

    print('Email sent!')
except Exception as exception:
    print(f"Error: {exception}")
