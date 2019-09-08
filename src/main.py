import argparse
import datetime
import dotenv
import os

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


def parse():
	parser = argparse.ArgumentParser()                 # analizador de argumentos
	
	
	parser.add_argument('date', 
    help='Fecha (YYYY-MM-DD) sobre la que se quiere mirar el clima y la contaminacion',
    type=valid_date)
	parser.add_argument('delta', 
    help='Dias a revisar antes y despues de la fecha indicada', 
    type=int)	

	return parser.parse_args()


# funcion principal
def main(): 
    args=parse()
    print(args)
    dotenv.load_dotenv()
    #get dataset and format it
    df=ds.createDF(args.date,args.delta)
    print("DataFrame ",df.shape)
    #get weather info
    #weather=sc.getWeather(args.date, "3195")
    #print("Info ",weather)
    #creat plot and save it
    gr.createFig(df)
    #creat pdf
    pdf.createPDF(args.date)
    #send pdf by email
    mail.sendMail(os.getenv("MAIL_PASS"),os.getenv("MAIL_ORIGIN"),os.getenv("MAIL_ORIGIN"),args.date)


if __name__=='__main__':
	main()

	