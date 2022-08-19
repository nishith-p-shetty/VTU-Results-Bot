from bs4 import BeautifulSoup
import requests
import os
import html
college = {"CS": 1}
CAPCHA = 'Xpaecu'
COOKIE = 'skbmpilpjum62jfs34k2obdn080amqk7f6fecfackul9e9udkn5dkpuf1qf0jlo0e5dlt73revv9lqedas0mj1mb7g23t5672o32cd1'
TOKEN = '99a7221e9b64fbaa389f976c45444c6881adee24'
URL = "https://results.vtu.ac.in/FMEcbcs22/resultpage.php"
HEADERS = {
    'Host': 'results.vtu.ac.in',
    'Cookie': 'VISRE='+COOKIE,
    'Content-Length': '80',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="96"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://results.vtu.ac.in',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://results.vtu.ac.in/FMEcbcs22/index.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
}
exam = str(1)+ " Semester"
path = os.getcwd()
for course, nos in college.items():
    for n in range(0,nos):
        usn = '1DB21' + course + str(n+1).zfill(3)
        PAYLOAD = 'Token='+TOKEN+'&lns='+usn+'&captchacode='+CAPCHA
        response = requests.post(url = URL, headers= HEADERS, data=PAYLOAD, verify=False)
        response = html.unescape(response.text)
        response = BeautifulSoup(response, 'html.parser').text
        response = response.replace("\t", "")
        response = response.strip()
        response = response.replace("\n\n\n", "\n")
        response = response.replace("\n\n", "\n")
        response = response.replace("\n\n\n", "\n")
        response = response.replace("\n\n", "\n")
        response = response.replace(" : ", "")
        response = response.replace(": ", "")
        response = response.split("\n")
        del response[78:]
        del response[:3]
        #print(response)
        i = 0
        for l in response:
            print(i, l)
            i=i+1