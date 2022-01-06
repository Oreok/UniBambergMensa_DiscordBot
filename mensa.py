import requests
from bs4 import BeautifulSoup
import re


def mensa_grap_thisweek():
    URL = "https://www.studentenwerk-wuerzburg.de/bamberg/essen-trinken/speiseplaene/mensa-austrasse-bamberg.html"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="week currentweek")
    week = result.find_all("div", class_="day")

    essensliste = []
    tempessen = ""
    
    for week in week:
        datum = week.find("h5")
        essen = week.find_all("article", class_="menu")
        essensliste.append(datum.text)
    
        for essen in essen:
            ess = essen.find("div", class_="title")
            price = str(essen.find("div", class_="price"))
            rightprice = str(re.findall(">....<", price)).replace("['>","").replace("<']","")
            tempessen = tempessen + ess.text + " " +"***"+ rightprice + "€" +"***"+ " \n " 
        if tempessen == "":
            tempessen = "Leider kein Essen gefunden"
        essensliste.append(tempessen)
        tempessen = ""
    return essensliste


def mensa_grap_nextweek():
    URL = "https://www.studentenwerk-wuerzburg.de/bamberg/essen-trinken/speiseplaene/mensa-austrasse-bamberg.html"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div", class_="week nextweek")
    week = result.find_all("div", class_="day")

    essensliste = []
    tempessen = ""
    
    for week in week:
        datum = week.find("h5")
        essen = week.find_all("article", class_="menu")
        essensliste.append(datum.text)
        
        for essen in essen:
            ess = essen.find("div", class_="title")
            price = str(essen.find("div", class_="price"))
            rightprice = str(re.findall(">....<", price)).replace("['>","").replace("<']","")
            tempessen = tempessen + ess.text + " " +"***"+ rightprice + "€" +"***"+ " \n "
        
        essensliste.append(tempessen)
        tempessen = ""
    return essensliste


def main():
    mensa_grap_thisweek()
    
if __name__ == '__main__':
    main()
    


