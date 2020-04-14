from bs4 import BeautifulSoup as bs
import lxml.html as lh
import requests as req

login_url="https://codeforces.com/enter?back=%2F/"

header={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}

payload={
    ""
    "handleOrEmail" : "sendhilsom7@gmail.com",
    "password" : "Swapna123",
    "action": "enter"
    }


session_requests=req.Session()
result=session_requests.get(login_url,headers=header)

print(result)
tree=lh.fromstring(result.text)
with req.Session() as s:
    sitelo = s.get("https://www.codechef.com/",headers=header)
    bs_content = bs(sitelo.content, "html.parser")
    token = bs_content.find("input", {"id":"edit-csrfToken"})["value"]
    #_tta = bs_content.find("input", {"name":"_tta"})["value"]
    #bfaa= bs_content.find("input", {"name":"_tta"})["value"]
    #ftaa= bs_content.find("input", {"name":"_tta"})["value"]
    login_data = {"name":"xmltrytry","pass":"Swapna@123", "csrfToken":token}
    seq=(s.post("https://www.codechef.com/",login_data,headers=header))
    print(seq)
    home_page = s.get("https://www.codechef.com/",headers=header)
    f=open("out.html","w")
    f.write(str(seq.content))
    f.close()
def check(url):
    #Url="https://www.a2oj.com/Ladders.html"
    page=req.get(url)
    hell=BeautifulSoup(page.content,'html.parser')
    res=hell.find(class_='rtable smaller')
    if res==None:
        return "not completed"
    else:
        return res

#a=check("https://codeforces.com/problemset/problem/4/A")
#print(a)


