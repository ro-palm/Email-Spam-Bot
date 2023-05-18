import smtplib
toaddrs = 'Receiver email'
fromaddrs = 'Sender Email'
message = 'Type message here'
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('Sender email', 'App Password')
  for i in range(1000):
    smtpserver.sendmail(fromaddrs, toaddrs, message)
    print(i)
