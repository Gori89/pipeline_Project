import datetime
import pandas as pd

period=""

def setDate(date):
    #ToDo:validar que la fecha es correcta
    if len(date)>=10:
        day=int(date[8:10])
        setPeriod("D")
    else:
        day=1
        setPeriod("M")
    if len(date)>=7:
        month=int(date[5:7])
    else:
        month=1
        setPeriod("Y")
    year=int(date[:4])
    return datetime.date(year,month,day)
    
def setPeriod(periodChange):
    global period
    period=periodChange

def getPeriod():
    global period
    return period
    
    
def setDelta(delta):
    global period
    if period=="D":
        return datetime.timedelta(days=delta)
    if period=="M":
        return datetime.timedelta(days=delta*30)


def getDataset(date1,date2=0):
    path="../Input/air-quality-madrid/csvs_per_year/madrid_{}.csv"
    #una fecha
    df_list=[pd.read_csv(path.format(date1.year))]

    if type(date2)==datetime.date and date2.year!=date1.year:
        #dos fechas
        df_list.append(pd.read_csv(path.format(date2.year)))
    
    #fecha y delta
    elif type(date2)==datetime.timedelta:
        if (date1-date2).year!=date1.year:
            df_list.append(pd.read_csv(path.format((date1-date2).year)))
        if (date1+date2).year!=date1.year:
            df_list.append(pd.read_csv(path.format((date1+date2).year)))

    return pd.concat(df_list, axis=0, ignore_index=True)


def dateToIndex(df):
    df["datetime"] = pd.to_datetime(df["date"])
    df = df.set_index('datetime')
    return df.drop(columns=["date"])


def meanbyDate(df):
    return df.groupby(['datetime']).mean()

