import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('manshipithava7@gmail.com','16digit')
msg="demo"
s.sendmail('manshipithava7@gmail.com','manshi7@gmail.com')
print('mail send')
s.quit()

