#!/usr/bin/python
import urllib2 ##-->modul urllib2 untuk menghandle url request
import BeautifulSoup ##-->import modul HTML/XML parsing

##-->request URL yang dimana urlnya adalah dcc-dp.org , dan simpan pada variabel 'page'
page = urllib2.urlopen('http://www.bbcgoodfood.com/recipes/1940686/mexican-chicken-stew-with-quinoa-and-beans') 
##-->membaca keseluruhan string dari 'page' dan simpan pada variabel 'htmlcode_page'
htmlcode_page = page.read()
##-->Parsing page
dump_isihtml = BeautifulSoup.BeautifulSoup(htmlcode_page) 
##--> cetak string dari judul page site
#print dump_isihtml

##-->ambil tag a href
Links = dump_isihtml.findAll("span")
foto = dump_isihtml.find("img",attrs={'class':'photo'})
print foto
##-->hitung banyaknya elemen pada Links  
leng = len(Links)

##-->counter   
count = 0   
##-->perulangan untuk menulis link dari href selama counter kurang dari banyaknya link
while count < leng:     
    #if (Links[count].string == True):
    print Links[count].string  ##--> cetak link URL
    
    count += 1  ##--> increment
        
