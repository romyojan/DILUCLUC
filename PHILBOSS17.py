import sys
from GENERATOR import *
from ConvertToBold import *
from IPINFO import *

def RegisterPHLBoss17(email_address, password, invitation_code, serialNumber, user_agent):
    url = "https://www.phlboss17.com/api/v1/user/register"

    payload = {
        "username": email_address,
        "password": password,
        "recommend": invitation_code,
        "areacode": 63,
        "type": 2,
        "serialNumber": serialNumber
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": "",
        "Content-Length": str(len(payload)),
        "Content-Type": "application/json",
        "Cookie": f"SWOFT_SESSION_ID={RandomStringGenerator(26)}",
        "From": "2",
        "Language": "en",
        "Net": "wifi",
        "Origin": "https://www.phboss8.com",
        "Os": "v2.0",
        "Referer": "https://www.phboss8.com/home",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": user_agent,
        "Version": "2.0",
    }

    response = requests.post(url, json=payload, headers=headers)

    try:
        if response.status_code == 200:
            if '{"result":200000,"message":"Success"' in response.text:
                responseData = response.json()
                uidData = responseData['data']['uid']
                usernameData = responseData['data']['username']
                balanceData = responseData['data']['balance']
                used_code = responseData['data']['recommend']
                authorization = responseData['data']['token']
                return "SUCCESS|REGISTRATION",  uidData, usernameData, balanceData, used_code, authorization
            else:
                return "FAILED|REGISTRATION", response.text
        else:
            return "FAILED|REGISTRATION", f"{response.status_code}|{response.text}"
    except Exception as RegisterPHLBoss17Error:
        return "FAILED|REGISTRATION", RegisterPHLBoss17Error

def DepositPHILBoss17(authorization, user_agent):
    # Set the standard output encoding to UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    url = "https://www.phlboss17.com/api/v1/Pay/order/add/online"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Authorization": authorization,
        "Content-Type": "application/json",
        "Cookie": f"G_ENABLED_IDPS=google; SWOFT_SESSION_ID={RandomStringGenerator(26)}",
        "From": "2",
        "Language": "en",
        "Net": "wifi",
        "Origin": "https://www.phlboss17.com",
        "Os": "v2.0",
        "Referer": "https://www.phlboss17.com/home",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": user_agent,
        "Version": "2.0",
    }
    body = {
        "platformId": 93,
        "platformTypeId": 324,
        "settingId": 672,
        "categoryId": 11,
        "amount": "200",
        "isParticipating": "0" #0 IF  NOT PARTICIPATING, 1 IF PARTICIPATING
    }

    response = requests.post(url, headers=headers, json=body)
    content = response.text

    try:
        json_content = response.json()
    except UnicodeDecodeError:
        json_content = response.json()

    if 'Successful operation' in content:
        payment_link = json_content['data']['content']
        return "SUCCESS|DEPOSIT", payment_link
    else:
        return "FAILED|DEPOST", json_content

def CheckDepositPHILBoss17(referer_url, user_agent, ip_address):
    id_data = referer_url.replace("https://h5.cecopay365.com/gcashPay/", "")
    url = "https://h5.cecopay365.com/api/pay/pay_info"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Length": "110",
        "Content-Type": "application/json; charset=utf-8",
        "Origin": "https://h5.cecopay365.com",
        "Referer": referer_url,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": user_agent,
    }
    data = {
        "id": id_data,
        "href": referer_url,
        "referrer": "https://www.phlboss17.com/"
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        if response.status_code == 200:
            if '{"status":0,"time"' in response.text:
                responseData = response.json()
                if 'bankAccountNo' in response.text:
                    status = responseData['model']['status']
                    amount = responseData['model']['amount']
                    payData = responseData['model']['payData']
                    name = responseData['model']['cardInfo']['name']
                    bankAccountNo = responseData['model']['cardInfo']['bankAccountNo']
                    return "SUCCESS|DEPOSIT", status, amount, payData, name, bankAccountNo
            else:
                return "FAILED|DEPOSIT", response.text
        else:
            return "FAILED|DEPOSIT", f"{response.status_code}|{response.text}"
    except:
        return "FAILED|DEPOSIT", f"{response.status_code}|{response.text}"
    
def StartPHLBoss17(invitation_code):
    retries_count = 0
    while True:
        ip_address = IPAddressGenerator()
            
            if "SUCCESS" in IP_API_COMResult:
                country = IP_API_COMResult[1]
                regionName = IP_API_COMResult[2]
                city = IP_API_COMResult[3]
                isp = IP_API_COMResult[4]
                as_repsonse = IP_API_COMResult[5]
                ip_info = f"{ConvertToBold('IP Address')} ↯ `{ip_address}`\n{ConvertToBold('Country')} ↯ `{country}`\n{ConvertToBold('Region')} ↯ `{regionName}`\n{ConvertToBold('City')} ↯ `{city}`\n{ConvertToBold('ISP')} ↯ `{isp}`\n{ConvertToBold('AS')} ↯ `{as_repsonse}`"
                break
            else:
                retries_count += 1
            
    email_address = RandomEmailAddressGenerator()
    password = f'{email_address.replace("@gmail.com","")}_{RandomDigitGenerator(4)}'
    serialNumber = RandomCharacterGenerator(32).lower()
    user_agent = UserAgentGenerator()
    if RegisterPHLBoss17Result[0].startswith("SUCCESS|REGISTRATION"):
        uidData = RegisterPHLBoss17Result[1]
        usernameData = RegisterPHLBoss17Result[2]
        balanceData = RegisterPHLBoss17Result[3]
        invite_code = RegisterPHLBoss17Result[4]
        authorization = RegisterPHLBoss17Result[5]
        DepositPHILBoss17Result = DepositPHILBoss17(authorization, user_agent)
        if 'SUCCESS|DEPOSIT' in DepositPHILBoss17Result:
            payment_link = DepositPHILBoss17Result[1]
            CheckDepositPHILBoss17Result = CheckDepositPHILBoss17(payment_link, user_agent)
            if 'SUCCESS|DEPOSIT' in CheckDepositPHILBoss17Result:
                deposit_amount = CheckDepositPHILBoss17Result[2]
                qr_value = CheckDepositPHILBoss17Result[3]
                gcash_name = CheckDepositPHILBoss17Result[4]
                gcash_no = CheckDepositPHILBoss17Result[5]
                personal_info =f"{ConvertToBold('Email')} ↯ `{email_address}`\n{ConvertToBold('Password')} ↯ `{password}`\n{ConvertToBold('Serial')} ↯ `{serialNumber}`\n{ConvertToBold('UserInfo')} ↯ `{usernameData}|{uidData}`\n{ConvertToBold('Balance')} ↯ `{balanceData}`\n{ConvertToBold('Invite Code')} ↯ `{invite_code}`"
                deposit_info = f"{ConvertToBold('GCash')} ↯ `{gcash_name}`\n{ConvertToBold('GCash NO')} ↯ `{gcash_no}`\n{ConvertToBold('Amount')} ↯ `{deposit_amount}`\n{ConvertToBold('QRData')} ↯ `{qr_value}`\n{ConvertToBold('Payment Link')} ↯ {payment_link}"
                return "SUCCESS|REGISTRATION", f"{ConvertToBold('PHILBOSS ACCOUNT DETAILS')}\n{personal_info}\n\n{ConvertToBold('IP ADDRESS DETAILS')}\n{ip_info}\n\n{ConvertToBold('DEPOSIT ACCOUNT DETAILS')}\n{deposit_info}\n{ConvertToBold('Retries')} ↯ {retries_count}"
            else:
                return "FAILED|DEPOSIT", CheckDepositPHILBoss17Result[1] 
        else:
            return "FAILED|DEPOSIT", DepositPHILBoss17Result[1]
    elif 'Username format error' in RegisterPHLBoss17Result:
        return StartPHLBoss17(invitation_code)
    else:
        return "FAILED|REGISTRATION", f"{RegisterPHLBoss17Result[1]}"
