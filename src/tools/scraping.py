from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup


def getHtml(date, station):
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Firefox(options=options)
    driver.get("https://datosclima.es/Aemethistorico/Meteosingleday.php")
    
    select = Select(driver.find_element_by_name('Provincia'))
    select.select_by_value('MADRID')
    select = Select(driver.find_element_by_name('id_hija'))
    select.select_by_value('3195')

    element = driver.find_element_by_name("Iday").send_keys(date[8:])
    element = driver.find_element_by_name("Imonth").send_keys(date[5:7])
    element = driver.find_element_by_name("Iyear").send_keys(date[:4])
    
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
    

def getWeather(date, station):
    html=getHtml(date, station)
    info=scrapHtml(html)
    return info