from mainlist import getData
from check import *
from codeforcesApi.CodeforcesParser import CodeforcesSemiApi as CSA

class MyA2OJ:
    
    def __init__(self):
        self.User = None
        self.Profile = None

    def assignName(self,handle):
        try:
            self.User=CSA(handle)
            self.Profile=self.User()
            return True
        except:
            self.User=None
            self.Profile=None
            return False

    def current(self):
        if self.User is not None:
            return check(getData,self.User)#return a json file with link
        else:
            return None
            
    def fetch(self,json):
        if self.User is not None:
            return check(json,self.User,jsonform=True,debug=True)#return a json file with link
        else:
            return None

    def __repr__(self):
        return ">>>"+str(self.User.Username)+"<<<"

    def __call__(self):
        return self.Profile
    
        
    def refresh(self):
        self.User.Submissions=self.User.refresh()
    ### These are after addition of SQL so Later
    def skip(self):
        pass #to be able to mark a question done when not done 
    def search(self):
        pass #search editorial of json file google

    def Add(self):
        pass #add a new question or set of questions with priority
    def skipped(self):
        pass #This is set of questions which is skipped and sorted based on difficult
        # in reverse or based on recently skipped should be better
        
    
        
    #check(getData("ladder.html"))
