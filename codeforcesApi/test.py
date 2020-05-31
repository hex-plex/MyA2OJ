import requests
def generate_url( method_name, **fields):
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
def check_return_code(response):
    if response["status"] != "OK":
        raise Exception(
            "Request returned not OK status",
            response["status"],
            response["comment"],
            )

def get_response(request):
    response = request.json()
    check_return_code(response)
    return response


def user_status( handle, start=-1, count=-1):
    parameters = {
            "handle": str(handle),
            }
    if start != -1:
        parameters["start"] = str(start)
    if count != -1:
        parameters["count"] = str(count)
    request_url = generate_url("user.status", **parameters)
    request = requests.get(request_url)
    return get_response(request)


print(user_status("Hex-Plex0xff")['result'][:2])
