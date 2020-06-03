from bs4 import BeautifulSoup 
import requests as req
import numpy as np

class DFSites:
    archive = []

    def DFS(self,root,depth):
        if depth>self.maxdepth:
            return 0
        page=req.get(self.url + root)
        cont = BeautifulSoup(page.content,'html.parser')
        res = cont.find_all('a')
        for tag in res:
            if tag.get('href').find(self.substring)!=-1:
                self.archive.append([tag.get('href'),page.content])
            else:
                self.DFS(tag.get('href'),depth+1)

    
    def __init__(self,url,substring,maxdepth=10,init=''):
        self.url = url
        self.substring = substring
        self.maxdepth = maxdepth
        self.DFS(init,0)

    def numpy(self):
        return np.array(self.archive)

    def save(self):
        np.savetxt('All_queue.list',self.numpy(),delimiter=",")


if __name__=="__main__":
    ## This is a example how with syntax
    #a1slow = DFSites("https://www.a2oj.com/","codeforces")
    #a1slow.archive ## your data required
    ## This would search whole websites for link with codeforces in it
    ## and as default would search the whole website from the page given till 10 pages of depth
    ## And would even search for category which is not needed hence doing the following can help fast things up
    a2fast = DFSites("https://www.a2oj.com/","codeforces",maxdepth=5,init="Ladders.html")
    a2fast.save() ## your data that is required
    ## This would restrict the search 5 pages deep
    ## and would only seach under Ladder.html only
