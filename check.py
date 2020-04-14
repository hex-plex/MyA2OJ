from bs4 import BeautifulSoup as BS
import requests as req
from mainList import *
trav=mainData
mainLink=mainLink
for links in trav[0:1]:
    link = list(str(links[3]).split("\""))[1]
    url=mainLink+link
    print(req.get(url))
    subdata,_=getData(link)
    print(subdata)
