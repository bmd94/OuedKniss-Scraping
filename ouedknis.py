import requests
from bs4 import BeautifulSoup

with open('Telephones.csv','w') as file:
    lien = "https://www.ouedkniss.com/telephones/"
    for i in range(0,10):
        response = requests.get(lien+str(i))
        soup = BeautifulSoup(response.text,"lxml")
        #print(soup)
        annonce = soup.find_all('ul' , attrs={'class' : 'annonce_left'})
        #print(annonce[0])

        file.write('nom'+','+'prix'+','+'lien\n')
        for elm in annonce:
            link = elm.find('a')['href']
            nom = elm.find('h2').text
            prix = str(elm.find('span',itemprop="price")).replace('<span itemprop="price">','').replace('</span>','')
            #print(prix)
            if link and nom and prix:
                n = nom.strip()
                p = prix.strip()
                l = "https://www.ouedkniss.com/"+link
                file.write(n+','+p+','+l+'\n')