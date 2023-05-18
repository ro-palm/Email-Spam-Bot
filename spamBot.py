import smtplib
toaddrs = '578293@student.belgiumcampus.ac.za'
fromaddrs = 'fyou18314@gmail.com'
message = 'Zander You Have Been Hacked'
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('fyou18314@gmail.com', 'ihprhlgyopvioomw')
  for i in range(10):
    smtpserver.sendmail(fromaddrs, toaddrs, message)
    print(i)