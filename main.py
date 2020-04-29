from mainlist import getData
from check import *
from codeforcesApi.CodeforcesParser import CodeforcesSemiApi as CSA

class MyA2OJ:
    User = None
    Profile = None
    def __init__(self):
        pass
    def assignName(self,handle):
        try:
            self.User=CSA(handle)
            self.Profile=self.User()
            return True
        except:
            self.User=None
            self.Profile=None
            return False
    def current():
        if User is not None:
            return check(getData,User)
        else:
            return None
            
        
        
    check(getData("ladder.html"))
