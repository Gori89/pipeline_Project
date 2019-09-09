from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import datetime


def getHtml(date, station):
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options)
    driver.get("https://datosclima.es/Aemethistorico/Meteosingleday.php")
    
    select = Select(driver.find_element_by_name('Provincia'))
    select.select_by_value('MADRID')
    select = Select(driver.find_element_by_name('id_hija'))
    select.select_by_value(station)

    element = driver.find_element_by_name("Iday").send_keys(date.day)
    element = driver.find_element_by_name("Imonth").send_keys(date.month)
    element = driver.find_element_by_name("Iyear").send_keys(date.year)
    
    driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div/form/input[5]")[0].click()
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    return soup

def scrapHtml(html):
    info={}
    info["Tmax_C"]=float(html.select("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1)")[0].text.split(" "[0])[0])
    info["Tmin_C"]=float(html.select("tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1)")[0].text.split(" ")[0])
    info["Prec_lm2"]=float(html.select("tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(8) > div:nth-child(1)")[0].text.split(" ")[0])
    info["Wind_ms"]=float(html.select("tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(6) > div:nth-child(1)")[0].text.split(" ")[0])
    info["Direction"]=float(html.select("tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(6) > div:nth-child(1)")[0].text.split(" ")[0])
    return info
    

def getWeatherDay(date, station):
    print("Accediendo a la pagina...")
    html=getHtml(date, station)
    print("Se ha accedido a la pagina")
    print("Scrapeando el tiempo...")
    info=scrapHtml(html)
    print("Tiempo scrapeado")
    return info

def getHtmlPeriod(dateI,dateF):
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options)
    driver.get("https://datosclima.es/Aemet2013/Precipitacion2013.php")

    select = Select(driver.find_element_by_name('PROVINCIA'))
    select.select_by_value('Madrid')
    select = Select(driver.find_element_by_name('id_hija'))
    select.select_by_value("Madrid, Retiro")

    element = driver.find_element_by_name("Iday").send_keys(dateI.day)
    element = driver.find_element_by_name("Imonth").send_keys(dateI.month)
    element = driver.find_element_by_name("Iyear").send_keys(dateI.year)
   
    element = driver.find_element_by_name("Fday").send_keys(dateF.day)
    element = driver.find_element_by_name("Fmonth").send_keys(dateF.month)
    element = driver.find_element_by_name("Fyear").send_keys(dateF.year)

    driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div/form/input[5]")[0].click()
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    return soup

def scrapHtmlPeriod(html):

    table=html.find_all("table")
    years=[]
    for i in range(2,len(table),4):
        years.append(table[i])
    weather={}
    for year in years:
        days=year.find_all("tr")
        for day in days[2:]:
            try:
                weather[datetime.datetime.strptime(day.text[0:10], "%d-%m-%Y")]=(float(day.text[10:]) if day.text[10:]!="" else 0)
            except ValueError as e:
                pass
    return weather

def getWeather(date1, date2):
    print("Accediendo a la pagina...")
    html=getHtmlPeriod(date1,date2)
    print("Se ha accedido a la pagina")
    print("Scrapeando el tiempo...")
    info=scrapHtmlPeriod(html)
    print("Tiempo scrapeado")
    return info    