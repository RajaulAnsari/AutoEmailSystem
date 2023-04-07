# Email Sender using Gmail

This code sends an email from a Gmail account to a destination email address using the `smtplib` library in Python.

## Configuration
- `gmail_user`: Fill with your Gmail address.
- `gmail_app_password`: Fill with your App Password. [Generate App Password](https://myaccount.google.com/apppasswords)
- `to_email`: Fill with the destination email address.
- `subject`: Fill with the subject of the email.
- `body`: Fill with the content of the email.

The code uses the SMTP (Simple Mail Transfer Protocol) library provided by Python through the smtplib module. 
The library is used to connect to the Gmail SMTP server via SSL (Secure Sockets Layer) on port 465. 
The Gmail account is then logged in using the login method, and the email is sent using the sendmail method. 
If the email is sent successfully, the code outputs "Email sent!". If there is an error, the exception message is displayed.
