import smtplib
import ssl

def send_mail(message):
    port=465
    host='smtp.gmail.com'
    password='xwwxetivpwxxnfsm'
    username='bloodshreder1@gmail.com'
    receiver='bloodshreder1@gmail.com'
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context)as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)