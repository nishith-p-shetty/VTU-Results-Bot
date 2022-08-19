#from calendar import c
import requests
import html
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from collections import Counter

exam = "1 Semester"
college = {"CI": 18}
college = {"CS": 2, "CI": 2, "IS": 2, "AD": 2, "EC": 2, "CV": 2, "ME": 2, "EE": 2}

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

def sgpa(marks):
    credits = [3, 3, 3, 3, 3, 1, 1, 2, 1]
    points = 0

    for x in range(len(marks)):
        points += grade_point(marks[x], credits[x])
    
    return (points / sum(credits))


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
with pd.ExcelWriter(exam+".xlsx") as writer:
    for course, nos in college.items():
        for err in range(19):

            usn_arresult_percentage_array=[]
            name_arresult_percentage_array = []
            result_percentage_array = []
            sgpa_percentage_array = []
            total_percentage_array = []
            percentage_percentage_array = []

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

                frequency = Counter(response)
                frequency = dict(frequency)

                result = ("PASS" if frequency['P'] == 9  else "FAIL")

                usn_arresult_percentage_array.append(response[1])
                name_arresult_percentage_array.append(response[3])
                result_percentage_array.append(result)

                total = 0
                pos = 16
                marks = []
                for i in range(9):
                    total = total + int(response[pos])
                    marks.append(int(response[pos]))
                    pos = pos+7
                
                total_percentage_array.append(total)
                percentage_percentage_array.append(total/9)

                if result == "PASS":
                    sgpa_percentage_array.append(sgpa(marks))
                else:
                    sgpa_percentage_array.append(0)

            df = pd.DataFrame({
                'USN':usn_arresult_percentage_array,
                'Name':name_arresult_percentage_array,
                'Result':result_percentage_array,
                'SGPA':sgpa_percentage_array,
                'Total':total_percentage_array,
                '%':percentage_percentage_array
            })
            df.to_excel(writer, sheet_name=course, index=False)