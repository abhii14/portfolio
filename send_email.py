import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "agrawalabhishek622@gmail.com"
password = "dxnz zxsf zugn bwkb"

receiver = "agrawalabhishek622@gmail.com"
context = ssl.create_default_context()

message = """
hi!
how are you?
bye!
"""

with smtplib.SMTP_SSL(host, port, context= context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
