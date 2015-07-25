import requests

def dweetSender(myName, myKeys):
    dweetIO = "https://dweet.io/dweet/for/"
    rqsString = dweetIO + myName + '?'

    for key, value in myKeys.items():
        rqsString = rqsString + key + '=' + str(value) + '&'

    print(rqsString)

    rqs = requests.get(rqsString)
    return rqs.status_code