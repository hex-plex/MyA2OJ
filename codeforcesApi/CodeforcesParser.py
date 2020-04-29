import requests
class CodeforcesSemiApi:
    Submissions={}
    Username=""
    def generate_url(self, method_name, **fields):
        request_url = "https://codeforces.com/api/" + str(method_name) + "?"
        for i in fields:
            request_url += str(i) + "="
            if isinstance(fields[i], list):
                for j in fields[i]:
                    request_url += str(j) + ";"
            else:
                request_url += str(fields[i])
                request_url += "&"
        request_url = request_url[:-1]
        return request_url
    
    def check_return_code(self,response):
        if response["status"] != "OK":
            raise Exception(
                "Request returned not OK status",
                response["status"],
                response["comment"],
                )
        

    def get_response(self,request):
        response = request.json()
        self.check_return_code(response)
        return response


    def user_status(self, handle, start=-1, count=-1):
        if handle=="":
            raise Exception("Please input a username")
            return None
        parameters = {
                "handle": str(handle),
                }
        if start != -1:
            parameters["start"] = str(start)
        if count != -1:
            parameters["count"] = str(count)
        request_url = self.generate_url("user.status", **parameters)
        request = requests.get(request_url)
        return self.get_response(request)
    def __init__(self, Username):
        self.Submissions = self.user_status(Username)
        self.Username = Username
    def refresh(self):
        self.Submissions = self.user_status(self.Username)
        return self.Submissions
    
    def __call__(self):
        return "https://codeforces.com/profile/"+self.Username

    def __repr__(self):
        return "<"+self.Username+"-"+str(len(self.Submissions))+">"




