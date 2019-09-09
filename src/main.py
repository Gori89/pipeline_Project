import argparse
import datetime
import dotenv
import os
import pandas as pd
import re

import tools.dataset as ds
import tools.scraping as sc
import tools.graphic as gr
import tools.pdf as pdf
import tools.mail as mail



def valid_date(s):
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def valid_cont(c):
    pollution=["BEN", "CO", "EBE", "NMHC", "NO", "NO_2", "O_3", "PM10", "PM25", "SO_2", "TCH", "TOL"]
    if c in pollution:
            return c
    else:
        msg = "Contaminante no valido. Debe ser uno de los siguientes: "+str(pollution)
        raise argparse.ArgumentTypeError(msg)

def valid_mail(mail):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',mail.lower()):
        return mail
    else:
        msg = "El mail no tiene el formato correcto"
        raise argparse.ArgumentTypeError(msg)

def parse():
    parser = argparse.ArgumentParser()
    #analizador de argumentos
    parser.add_argument('date1',
    help='Fecha inical(YYYY-MM-DD)',
    type=valid_date)
    parser.add_argument('date2',
    help='Fecha final(YYYY-MM-DD)',
    type=valid_date)
    parser.add_argument('cont',
    help='Contaminante a revisar ("BEN", "CO", "EBE", "NMHC", "NO", "NO_2", "O_3", "PM10", "PM25", "SO_2", "TCH", "TOL")',
    type=valid_cont)
    # parser.add_argument('destination',
    # help='Mail en el que recivir la informacion',
    # type=valid_mail,
    # nargs=1, 
    # default=False)
    return parser.parse_args()


# funcion principal
def main(): 
    args=parse()
    print(args)
    dotenv.load_dotenv()
    #get dataset and format it
    df=ds.createDF(args.date1,args.date2)
    print("DataFrame ",df.shape)
    #get weather info
    weather=sc.getWeather(args.date1,args.date2)
    #print("Info ",weather)
    df_weather=pd.DataFrame(list(weather.items()),columns=['date', 'rain'])
    df_weather=ds.dateToIndex(df_weather)
    #creat plot and save it
    gr.createFig(df,df_weather,args.cont)
    #creat pdf
    pdf.createPDF(args.date1,args.date2,args.cont)
    #send pdf by email
    c=input("¿Quieres recibir la informacion por correo?[Y/*]")
    if c=="Y":
        args.destination=input("Introduce el email:")
        valid_mail(args.destination)
    else:
        print("Tienes los resultados en la carpeta output")
     
    mail.sendMail(os.getenv("MAIL_PASS"),os.getenv("MAIL_ORIGIN"),args.destination,args.date1)



if __name__=='__main__':
	main()

	