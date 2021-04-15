# Sending Emails With Python #
# -------------------------- #

#    Identity of email provider
#                \
#            ----------                    
# "demo_email@gmail.com"
#  ----------          
#      \
# Identity of email account

    
#     SMTP Information
# > Gmail: smtp.gmail.com
# > Hotmail: smtp.live.com
# > Yahoo: smtp.mail.yahoo.com


# How to Send Emails with Python using SMTP
import smtplib

my_email = "demo_email_01@gmail.com"
password = "demo_password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="demo_email_02@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )

