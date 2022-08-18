from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os
import html
import gpa
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
    'Upresult-Insecure-Requests': '1',
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
        total = [np.nan]*nos
        per = [np.nan]*nos
        m = [np.nan]*nos
        p = [np.nan]*nos
        e = [np.nan]*nos
        c = [np.nan]*nos
        ev = [np.nan]*nos
        pl = [np.nan]*nos
        el = [np.nan]*nos
        en = [np.nan]*nos
        id = [np.nan]*nos
        result = [np.nan]*nos
        for n in range(0,nos):
            usn = '1DB21' + course + str(n+1).zfill(3)
            PAYLOAD = 'Token='+TOKEN+'&lns='+usn+'&captchacode='+CAPCHA
            #r = requests.post(url = URL, headers= HEADERS, data=PAYLOAD, verify=False)
            #htl = html.unescape(r.text)
            htl = "b'VTU Result 2022\n\t\t\t\t\t\t\t\t\t\t\t\xe0\xb2\xb5\xe0\xb2\xbf.\xe0\xb2\xa4\xe0\xb2\xbe.\xe0\xb2\xb5\xe0\xb2\xbf \xe0\xb2\xb8\xe0\xb2\xbe\xe0\xb2\xae\xe0\xb2\xaf\xe0\xb2\xbf\xe0\xb2\x95 \xe0\xb2\xab\xe0\xb2\xb2\xe0\xb2\xbf\xe0\xb2\xa4\xe0\xb2\xbe\xe0\xb2\x82\xe0\xb2\xb6.  VTU PROVISIONAL RESULT.\n  \xe0\xb2\xb5\xe0\xb2\xbf.\xe0\xb2\xa4\xe0\xb2\xbe.\xe0\xb2\xb5\xe0\xb2\xbf \xe0\xb2\xaa\xe0\xb2\xa6\xe0\xb2\xb5\xe0\xb2\xbf / \xe0\xb2\xb8\xe0\xb3\x8d\xe0\xb2\xa8\xe0\xb2\xbe\xe0\xb2\xa4\xe0\xb2\x95\xe0\xb3\x8b\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb2\xb0 \xe0\xb2\xaa\xe0\xb2\xa6\xe0\xb2\xb5\xe0\xb2\xbf \xe0\xb2\xaa\xe0\xb2\xb0\xe0\xb3\x80\xe0\xb2\x95\xe0\xb3\x8d\xe0\xb2\xb7\xe0\xb3\x86\xe0\xb2\xaf \xe0\xb2\xb8\xe0\xb2\xbe\xe0\xb2\xae\xe0\xb2\xaf\xe0\xb2\xbf\xe0\xb2\x95 \xe0\xb2\xab\xe0\xb2\xb2\xe0\xb2\xbf\xe0\xb2\xa4\xe0\xb2\xbe\xe0\xb2\x82\xe0\xb2\xb6 \xe0\xb2\xab\xe0\xb3\x86\xe0\xb2\xac\xe0\xb3\x8d\xe0\xb2\xb0\xe0\xb2\xb5\xe0\xb2\xb0\xe0\xb2\xbf / \xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xb0\xe0\xb3\x8d\xe0\xb2\x9a\xe0\xb3\x8d - \xe0\xb3\xa8\xe0\xb3\xa6\xe0\xb3\xa8\xe0\xb3\xa8.   VTU PROVISIONAL RESULTS OF UG / PG FEBRUARY / MARCH - 2022 EXAMINATION.\nUniversity Seat Number\n : 1DB21CS001\nStudent Name\n: AAYUSH P NAIR\nSemester : 1\nSubject Code\nSubject Name\nInternal Marks\nExternal Marks\nTotal\nResult\nAnnounced / Updated on\n21MAT11\nCALCULUS AND DIFFERENTIAL EQUATIONS\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t48\n34\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t82\nP\n2022-07-15\n21PHY12\nENGINEERING PHYSICS\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t43\n29\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t72\nP\n2022-07-15\n21ELE13\nBASIC ELECTRICAL ENGINEERING\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t47\n20\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t67\nP\n2022-07-15\n21CIV14\nELEMENTS OF CIVIL ENGINEERING AND MECHANICS\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t44\n41\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t85\nP\n2022-07-15\n21EVN15\nENGINEERING VISUALIZATION\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t37\n48\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t85\nP\n2022-07-15\n21PHYL16\nENGINEERING PHYSICS LABORATORY\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t48\n46\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t94\nP\n2022-07-15\n21ELEL17\nBASIC ELECTRICAL ENGINEERING LABORATORY\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t44\n47\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t91\nP\n2022-07-15\n21EGH18\nCOMMUNICATIVE ENGLISH\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t45\n42\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t87\nP\n2022-07-15\n21IDT19\nINNOVATION AND DESIGN THINKING\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t48\n27\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t75\nP\n2022-07-15\n \xe0\xb2\xa8\xe0\xb2\xbe\xe0\xb2\xae\xe0\xb2\x95\xe0\xb2\xb0\xe0\xb2\xa3 / \xe0\xb2\xb8\xe0\xb2\x82\xe0\xb2\x95\xe0\xb3\x8d\xe0\xb2\xb7\xe0\xb3\x87\xe0\xb2\xaa\xe0\xb2\xa3\xe0\xb2\x97\xe0\xb2\xb3\xe0\xb3\x81   Nomenclature / Abbreviations\nP -> PASS\nF -> FAIL\nA -> ABSENT\nW -> WITHHELD\nX, NE -> NOT ELIGIBLE\nNote :  1) Results of some subjects of some students are not appearing due to reasons such as,\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ta) CIE not Availableb) SEE not available because of technical reasons etc, however they will be updated shortly.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2) Withheld results to be announced later\n\xe0\xb2\xb8\xe0\xb2\xb9\xe0\xb2\xbf/-Sd/-\n\xe0\xb2\x95\xe0\xb3\x81\xe0\xb2\xb2\xe0\xb2\xb8\xe0\xb2\x9a\xe0\xb2\xbf\xe0\xb2\xb5\xe0\xb2\xb0\xe0\xb3\x81 (\xe0\xb2\xae\xe0\xb3\x8c\xe0\xb2\xb2\xe0\xb3\x8d\xe0\xb2\xaf\xe0\xb2\xae\xe0\xb2\xbe\xe0\xb2\xaa\xe0\xb2\xa8) REGISTRAR (EVALUATION)\n \xc2\xa9 \xe0\xb3\xa8\xe0\xb3\xa6\xe0\xb3\xa8\xe0\xb3\xa8 \xe0\xb2\xb5\xe0\xb2\xbf\xe0\xb2\xa8\xe0\xb3\x8d\xe0\xb2\xaf\xe0\xb2\xbe\xe0\xb2\xb8 \xe0\xb2\xae\xe0\xb2\xa4\xe0\xb3\x8d\xe0\xb2\xa4\xe0\xb3\x81 \xe0\xb2\x85\xe0\xb2\xad\xe0\xb2\xbf\xe0\xb2\xb5\xe0\xb3\x83\xe0\xb2\xa6\xe0\xb3\x8d\xe0\xb2\xa7\xe0\xb2\xbf\xe0\xb2\xaa\xe0\xb2\xa1\xe0\xb2\xbf\xe0\xb2\xb8\xe0\xb2\xbf\xe0\xb2\xa6\xe0\xb2\xb5\xe0\xb2\xb0\xe0\xb3\x81 \xe0\xb2\xaf\xe0\xb3\x8b\xe0\xb2\x9c\xe0\xb2\xa8\xe0\xb2\xbe \xe0\xb2\xa8\xe0\xb2\xbf\xe0\xb2\xb0\xe0\xb3\x8d\xe0\xb2\xb5\xe0\xb2\xb9\xe0\xb2\xa3\xe0\xb3\x86 \xe0\xb2\xb5\xe0\xb2\xbf\xe0\xb2\xad\xe0\xb2\xbe\xe0\xb2\x97 (\xe0\xb2\xaa\xe0\xb2\xbf. \xe0\xb2\x8e\xe0\xb2\xae\xe0\xb3\x8d. \xe0\xb2\xb8\xe0\xb2\xbf), \xe0\xb2\xb5\xe0\xb2\xbf.\xe0\xb2\xa4\xe0\xb2\xbe.\xe0\xb2\xb5\xe0\xb2\xbf, \xe0\xb2\xac\xe0\xb3\x86\xe0\xb2\xb3\xe0\xb2\x97\xe0\xb2\xbe\xe0\xb2\xb5\xe0\xb2\xbf. \xe0\xb2\x95\xe0\xb2\xb0\xe0\xb3\x8d\xe0\xb2\xa8\xe0\xb2\xbe\xe0\xb2\x9f\xe0\xb2\x95. \xe0\xb2\xad\xe0\xb2\xbe\xe0\xb2\xb0\xe0\xb2\xa4. \xc2\xa9 2022 Designed & Developed by Project Management Cell (PMC), VTU, Belagavi. Karnataka. India.'"
            soup = BeautifulSoup(htl, 'html.parser')
            a = soup.prettify()
            a = a.replace("\t", "")
            text = a.split("\n")
            name[n] = (text[6][2:])
            usno[n] = (text[4][3:])
            #cr[n] = int(text[8])
            #co[n] = int(text[10])
            #sgpa[n] = float(text[12])
            m = int(text[19])
            p = int(text[26])
            e = int(text[33])
            c = int(text[40])
            ev = int(text[47])
            pl = int(text[54])
            el = int(text[61])
            en = int(text[68])
            id = int(text[75])
            total[n] = int(text[19])+int(text[26])+int(text[33])+int(text[40])+int(text[47])+int(text[54])+int(text[61])+int(text[68])+int(text[75])
            per[n] = float(total[n] / 9)
            result[n] = ("PASS" if (text[20] == "P" and text[27] == "P" and text[34] == "P" and text[41] == "P" and text[48] == "P" and text[55] == "P" and text[62] == "P" and text[69] == "P" and text[76] == "P") else "FAIL")
        df = pd.DataFrame({
            'USN':usno,
            'Name':name,
            #'Credits Required':cr,
            #'Credits Obtained':co,
            '%':per,
            'Total':total,
            'Result':result,
            'Maths':m,
            'Physics':p,
            'Electrical':e,
            'Cicil':c,
            'CAED':ev,
            'Phy Lab':pl,
            'Ele Lab':el,
            'English':en,
            'IDT':id
        })
        df.to_excel(writer, sheet_name=course, index=False,)