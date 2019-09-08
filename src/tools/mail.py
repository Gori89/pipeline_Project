from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sendMail(password,origin,destination,date):
    server=conectToserver(password,origin)
    sender(origin,destination,date,server)



def conectToserver(password,mail):
    try: 
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(mail, password)
        print("Conectado al servidor Gmail")
        return server
    except:  
        print("No se ha podido conectar con el servidor Gmail")
        return False

def sender(origin,destination,date,server):


    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"


    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = origin
    message["To"] = destination
    message["Subject"] = subject
    

    message.attach(MIMEText(body, "plain"))

    # Open PDF file in binary mode
    filename='Analisis_Contaminacion_{}-{}-{}.pdf'.format(date.day,date.month,date.year)
    filepath='../Output/Analisis_Contaminacion_{}-{}-{}.pdf'.format(date.day,date.month,date.year)


    with open(filepath, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    server.sendmail(origin, destination, text)
    server.close()