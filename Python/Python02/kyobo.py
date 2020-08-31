#-*- coding: utf-8 -*-

import time
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoAlertPresentException

"""
0.준비물
python 설치
Firefox 설치 및 해당 버전에 맞는 geckodriver 다운로드
C드라이브에 'kyobo' 폴더 생성
geckodriver.exe와 kyobo.py를 C:/kyobo 로 이동
[cmd]
pip install bs4
pip install selenium

1.실행방법
kyobo_id와 kyobo_pw에 id, pw 작성 및 저장
[cmd]
cd /kyobo
python kyobo.py
"""
############### Add Information ###############
kyobo_id = ''
kyobo_pw = ''
driver_path = 'C:/kyobo/geckodriver.exe'
###############################################

print('교보문고 자동 출석 시작')
print('id : ' + kyobo_id)

# kyobo accept
options = Options()
options.headless = True
browser = Firefox(options=options, executable_path=driver_path)
browser.get('http://www.kyobobook.co.kr/index.laf')
print('kyobobook.co.kr 접속')

# 첫 화면 popup 우회
# print(browser.window_handles)
browser.switch_to.window(browser.window_handles[0])
print('popup 우회')

# login
browser.find_elements_by_css_selector('#gnbLoginInfoList > li')[0].click()
browser.find_element_by_id('memid').send_keys(kyobo_id)
browser.find_element_by_id('pw').send_keys(kyobo_pw)
browser.find_element_by_class_name('btn_submit').click()
print('login')

# 로그인 후 popup 우회
browser.switch_to.window(browser.window_handles[0])
browser.find_elements_by_css_selector('#gnbLoginInfoList > li')[2].click()

# 처음 출석 시 alert : enter
try:
    browser.switch_to.alert.accept()
    print('check')
except NoAlertPresentException:
    print('aleady check')

time.sleep(1)

html_source = browser.page_source
# 현재 출석 일수
soup = BeautifulSoup(html_source, 'html.parser')
ul = soup.select('.daily_stamp_list')
checked_day = ul[0].select('.on')+ul[0].select('.complete')

for day in checked_day:
    print(day.text)

# 전체 출석했다면, 2000원 교환권 응모
if len(ul) == len(checked_day):
    print('all check!')
    browser.find_element_by_css_selector('.benefits_stamp>li:last-child').click()

# popup부터 차례로 close
cnt = len(browser.window_handles)
for i in range(cnt,0,-1):
    browser.switch_to.window(browser.window_handles[i-1])
    browser.close()
    time.sleep(0.5)
print('총', str(len(checked_day)), '일 출석했습니다.')
