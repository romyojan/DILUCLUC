import requests

def IP_API_COM(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"

    response = requests.get(url)
    
    if response.status_code == 200:
        if '{"status":"success",' in response.text:
            responseData = response.json()
            country = responseData['country']
            regionName = responseData['regionName']
            city = responseData['city']
            isp = responseData['isp']
            as_repsonse = responseData['as']

            return "SUCCESS", country, regionName, city, isp, as_repsonse
        else:
            return "FAILED ON RESPONSE DATA", response.text
    
    else:
        return "FAILED ON STATUS CODE", f"{response.status_code}|{response.text}"
