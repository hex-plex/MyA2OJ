from bs4 import BeautifulSoup as BS
import requests as req
from mainList import *
trav=mainData
mainLink=mainLink
#print(trav)
for links in trav[0:1]:
    link = list(str(links[3]).split("\""))[1]
    url=mainLink+link
    print(req.get(url))
    subdata,_=getData(link,flag=False)
    print(subdata)
from codeforcesApi.CodeforcesParser import CodeforcesSemiApi

a = CodeforcesSemiApi("Codemaster007")
print(a.refresh())
