import os
from time import sleep
import requests
import html
from collections import Counter
from bs4 import BeautifulSoup
college = {"CI": 110}
CAPCHA = 'bVXXud'
COOKIE = 'v0541a7t43h7o4ifst2hgp79e3f577hf5n8q2p8iu1esihkh1o9hk1opspvn0ak7va4nk45rfe3ni4bfn9qgu8k63agtjuk0n4h1k31'
TOKEN = '90db35af85ef1a49409eb551347be8acf335cd97'
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
    for err in range(19):
        for n in range(0,nos):
            if(err == 18):
                sleep(5)
            usn = '1DB21' + course + str(n+1).zfill(3)
            PAYLOAD = 'Token='+TOKEN+'&lns='+usn+'&captchacode='+CAPCHA
            response = requests.post(url = URL, headers= HEADERS, data=PAYLOAD, verify=False)
            response = html.unescape(response.text)
            #print(response)
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
            frequency = Counter(response)
            frequency = dict(frequency)
            result = ("PASS" if frequency['P'] == 9  else "FAIL")
            name = response[3]
            total = 0
            c = 16
            for i in range(9):
                total = total + int(response[c])
                c = c+7



            print(usn)
            print(response[3])
            print(result)
            print(total)
            print()

            #i = 0
            #for l in response:
            #    print(i, l)
            #    i=i+1