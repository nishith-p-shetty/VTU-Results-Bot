import requests
import html
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from collections import Counter

exam = "5 Semester"
college = {"CS": 3, "CI": 2, "IS": 3, "AD": 3, "EC": 3}

def grade_point(m, c):
    if m >= 90:
        return (c * 10)
    elif m >= 80:
        return (c * 9)
    elif m >= 70:
        return (c * 8)
    elif m >= 60:
        return (c * 7)
    elif m >= 45:
        return (c * 6)
    elif m >= 40:
        return (c * 4)
    else :
        return (c * 0)

def sgpa (marks):
    credits = [3, 3, 3, 3, 3, 1, 1, 2, 1]
    points = 0

    for x in range(len(marks)):
        points += grade_point(marks[x], credits[x])
    
    return (points / sum(credits))

TOKEN = input("Token  : ")
COOKIE = input("Cookie : ")
CAPCHA = input("Captcha : ")

URL = "https://results.vtu.ac.in/DJcbcs24/resultpage.php"
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
    'Dnt': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://results.vtu.ac.in/DJcbcs24/index.php',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close'
}

with pd.ExcelWriter(exam+".xlsx", engine='openpyxl') as writer:
    for course, nos in college.items():
        usn_array=[]
        name_array = []
        result_array = []
        sgpa_array = []
        total_array = []
        percentage_array = []
        for n in range(0,nos):
            usn = '1DB21' + course + str(n+1).zfill(3)
            PAYLOAD = 'Token='+TOKEN+'&lns='+usn+'&captchacode='+CAPCHA
            response = requests.post(url = URL, headers= HEADERS, data=PAYLOAD, verify=False)
            sleep(1)
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
            frequency = Counter(response)
            frequency = dict(frequency)
            result = ("PASS" if frequency['P'] == 8  else "FAIL")
            # result = "0"
            usn_array.append(response[1])
            name_array.append(response[3])
            result_array.append(result)
            total = 0
            pos = 16
            marks = []
            for i in range(8):
                total = total + int(response[pos])
                marks.append(int(response[pos]))
                pos = pos+7
            
            total_array.append(total)
            percentage_array.append(total/9)
            if result == "PASS":
                sgpa_array.append(sgpa(marks))
            else:
                sgpa_array.append(0)
        df = pd.DataFrame({
            'USN':usn_array,
            'Name':name_array,
            'Result':result_array,
            'SGPA':sgpa_array,
            'Total':total_array,
            '%':percentage_array
        })
        df.to_excel(writer, sheet_name=course, index=False)
        sleep(5)