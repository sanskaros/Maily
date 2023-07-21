import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

server = smtplib.SMTP('smtp.gmail.com', 25)
server.starttls()
server.ehlo()

with open(r'C:\Users\Asus\.vscode\python programs\Project\password.txt', 'r') as f:
    password = f.read()


server.login('nevermindme7261@gmail.com',password)

msg = MIMEMultipart()
msg['From'] = 'Stateofmind'
msg['To'] = 'sksanskar98@gmail.com'
msg['Subject'] = 'just a test test'

with open(r'C:\Users\Asus\.vscode\python programs\Project\message', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename=r'C:\Users\Asus\.vscode\python programs\Project\he.jpg'
with open(filename, 'rb') as f:
    attachment = MIMEApplication(f.read(), Name=filename)

attachment['Content-Disposition'] = f'attachment; filename="{filename}"'
msg.attach(attachment)

text = msg.as_string()

server.sendmail('nevermindme7261@gmail.com', 'sksanskar98@gmail.com', text)

server.quit()
