import requests
from bs4 import BeautifulSoup
import bs4
import os

os.system("clear")


tata = "https://in.finance.yahoo.com/quote/TATAMOTORS.NS?p=TATAMOTORS.NS&.tsrc=fin-srch"
gainer = "https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"
losser = "https://www.moneycontrol.com/stocks/marketstats/nseloser/index.php"
india = "https://www.worldometers.info/coronavirus/country/india/"
world = "https://www.worldometers.info/coronavirus/"
us = "https://www.worldometers.info/coronavirus/country/us/"
uk = "https://www.worldometers.info/coronavirus/country/uk/"

while True:

    print("Welcome")
    print("---BY---SHOVIT---ROY---")
    print("---------------------------------------------")
    print("Choose from the option bellow :")
    print("---------------------------------------------")

    print("1. About Stock Market")
    print("2. About CoronaVirus")
    
    
    print("0. To exit\n")
    print("---------------------------------------------")
    ans = input("Enter Your choice : ")

    if ans == 1:

        print('\n1. Tata Moter Price')
        print('2. Top Gainers')
        print('3. Top Loosers')
        print("0. Exit")
        ans1 = input("Enter Your choice : ")

        if ans1 == 1:

            def stkprice():
                r=requests.get(tata)

                xml = r._content
                soup = BeautifulSoup(xml,'html.parser')
                price=soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
                return price
            print ("The current price of Tata Moters is : "+str(stkprice()))

        elif ans1 == 2:

            def gain():
                
                g=requests.get(gainer)
                xml = g._content
                soup = BeautifulSoup(xml,'html.parser')
                name = soup.find('td',{'class':'PR'}).find('a').text
                change = soup.find('td',{'class':'green'}).text
                gain = soup.find_all('td',{'class':'green'})[1].text
                return ( " -----1------ \nStock Name : {} \nChange : {} \nGain : {} ".format(name,change,gain))


            print(gain())

        elif ans1 == 3:

            def loss():
                l=requests.get(losser)
                xml = l._content
                soup = BeautifulSoup(xml,'html.parser')
                name = soup.find('td',{'class':'PR'}).find('a').text
                change = soup.find('td',{'class':'red'}).text
                loss = soup.find_all('td',{'class':'red'})[1].text
                return ( " -----1------ \nStock Name : {} \nChange : {} \nLoss : {} ".format(name,change,loss))
            
            print(loss())

    

        elif ans1 == 0:
            break

        else :
            print("Wrong Choice")

    elif ans == 2:

        print('1. World')
        print('2. India')
        print('3. USA')
        print('4. UK')
        print("0. To exit")
        ans2 = input("Enter Your choice : ")

        if ans2 == 1:
            def worl():
                req = requests.get(world)
                con = req._content

                soup = BeautifulSoup(con,'html.parser')

                tc = soup.find_all('div',{'class':'maincounter-number'})[0].text
                td = soup.find_all('div',{'class':'maincounter-number'})[1].text
                tr = soup.find_all('div',{'class':'maincounter-number'})[2].text
                return "\nTotal Cases : {} \nTotal Death : {} \nTotal Recovered : {}\n".format(tc,td,tr)
            print(worl())



        elif ans2 == 2:
            
            def ind():

                req = requests.get(india)
                con = req._content

                soup = BeautifulSoup(con,'html.parser')
                ncase = soup.find_all('li',{'class':'news_li'})[1].find('strong').text.split()[0]
                ndeath = list(soup.find_all('li',{'class':'news_li'})[1].find('strong').next_siblings)[1].text.split()[0]
                tc = soup.find_all('div',{'class':'maincounter-number'})[0].text
                td = soup.find_all('div',{'class':'maincounter-number'})[1].text
                tr = soup.find_all('div',{'class':'maincounter-number'})[2].text
                return "\nNew Case : {} \nNew Death : {} \nTotal Cases : {} \nTotal Death : {} \nTotal Recovered : {}\n".format(ncase,ndeath,tc,td,tr)

            print (ind())

        elif ans2 == 3:
            req = requests.get(us)
            con = req._content
            soup = BeautifulSoup(con,'html.parser')
            ncase = soup.find('li',{'class':'news_li'}).find('strong').text.split()[0]
            ndeath = list(soup.find('li',{'class':'news_li'}).find('strong').next_siblings)[1].text.split()[0]
            tc = soup.find_all('div',{'class':'maincounter-number'})[0].text
            td = soup.find_all('div',{'class':'maincounter-number'})[1].text
            tr = soup.find_all('div',{'class':'maincounter-number'})[2].text
            print("\nNew Case : {} \nNew Death : {} \nTotal Cases : {} \nTotal Death : {} \nTotal Recovered : {}\n".format(ncase,ndeath,tc,td,tr))

        elif ans2 == 4:
            req = requests.get(uk)
            con = req._content
            soup = BeautifulSoup(con,'html.parser')
            ncase = soup.find('li',{'class':'news_li'}).find('strong').text.split()[0]
            ndeath = list(soup.find('li',{'class':'news_li'}).find('strong').next_siblings)[1].text.split()[0]
            tc = soup.find_all('div',{'class':'maincounter-number'})[0].text
            td = soup.find_all('div',{'class':'maincounter-number'})[1].text
            tr = soup.find_all('div',{'class':'maincounter-number'})[2].text
            print("\nNew Case : {} \nNew Death : {} \nTotal Cases : {} \nTotal Death : {} \nTotal Recovered : {}\n".format(ncase,ndeath,tc,td,tr))

        elif ans2 == 0:
            break
        else :
            print("Wrong Choice")
    elif ans == 0:
        break

    else :
            print("Wrong Choice")


    print("Have a nice day ahead!!")






    

