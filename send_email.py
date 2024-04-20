import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "abhijeetkr889@gmail.com"
    password = "lvel egru tfbm oris"
    recevier = "abhijeetkr889@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, recevier, message)