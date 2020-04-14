from bs4 import BeautifulSoup
import lxml.html as lh
import requests as req
def getData(sub):
    Url="https://www.a2oj.com/"
    urllink=Url+sub
    page=req.get(urllink)
    doc=lh.fromstring(page.content)
    trele=doc.xpath("//tr")
    cont=BeautifulSoup(page.content,'html.parser')
    res=cont.find_all('a')  
    #print(res)
    #for i in  trele:
    #    print(i.text_content())
    #dta=[ i.text_content()[1:-1].split('\n'), if str(i.text_content()).find('ID')+1==0 else 0 for i in trele][1:]
    count=0
    dta=[]
    for i in trele:
        if str(i.text_content()).find('ID')+1==0:
        #print(i.text_content()[1:-1].split('\n')+[res[count]])
            data=i.text_content()[1:-1].split('\n')+[res[count]]
            if int(data[0])>10:
                dta.append(data)
            count+=1
    #del dta[dta.index(0)]

    dta.sort(key=lambda x:int(x[0]))
    return dta,Url

mainData,mainLink = getData("Ladders.html")
