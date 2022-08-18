from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os
import html
#college = {"AI": 63, "AD": 62, "CS": 187, "IS": 191, "ME": 17, "CV": 43, "AE": 54, "EE": 47, "EC": 179}
#college = {"AI": 3, "AD": 2, "CS": 1, "IS": 2, "ME": 2, "CV": 2, "AE": 2, "EE": 2, "EC": 2}
college = {"CS": 1}
CAPCHA = 'nPgtXr'
COOKIE = 'sr1um848a53sd0odvcjtfoo779r0qrlt3uqklue71ar05fb24v76dn16f1u8e8rheun0jtbudo1a1l3cv52ctqogu94fj513n3rncd3'
TOKEN = '0e7543fbc9d2111bcd55b95f33b65b6a7ce61430'
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
#exam = input("Enter Semester Number : ") + " Semester"
exam = str(1)+ " Semester"
path = os.getcwd()
with pd.ExcelWriter(exam+".xlsx") as writer:
    for course, nos in college.items():
        name = [np.nan]*nos
        usno = [np.nan]*nos
        #cr = [np.nan]*nos
        #co = [np.nan]*nos
        sgpa = [np.nan]*nos
        #grade = [np.nan]*nos
        for n in range(0,nos):
            usn = '1DB21' + course + str(n+1).zfill(3)
            PAYLOAD = 'Token='+TOKEN+'&lns='+usn+'&captchacode='+CAPCHA
            r = requests.post(url = URL, headers= HEADERS, data=PAYLOAD, verify=False)
            htl = html.unescape(r.text)
            soup = BeautifulSoup(htl, 'html.parser')
            a = soup.prettify()
            text = a.replace("\t", "")
            name[n] = (text[6][2:])
            usno[n] = (text[4][3:])
            #cr[n] = int(text[8])
            #co[n] = int(text[10])
            #sgpa[n] = float(text[12])
            sgpa[n] = text[19]+text[26]+text[33]+text[40]+text[47]+text[54]+text[61]+text[68]+text[75]
            #grade[n] = ("PASS" if text[10] == "21" else "FAIL")
        df = pd.DataFrame({
            'USN':usno,
            'Name':name,
            #'Credits Required':cr,
            #'Credits Obtained':co,
            'SGPA':sgpa,
            #'Grade':grade,
        })
        df.to_excel(writer, sheet_name=course, index=False,)