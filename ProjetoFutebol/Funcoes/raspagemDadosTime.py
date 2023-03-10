import requests

def raspagemDados():
    url = "https://webws.365scores.com/web/games/results"

    querystring = {"appTypeId":"5","langId":"31","timezoneName":"America/Sao_Paulo","userCountryId":"21","competitors":"1218","showOdds":"true","":""}

    payload = ""
    headers = {"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"}

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return response