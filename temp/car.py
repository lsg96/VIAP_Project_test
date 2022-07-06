from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


URL = 'https://www.cyberts.kr/cp/pvr/cpr/readCpPvrCarPrsecResveMainView.do'

#options = Options() # 옵션을 조정하기 위한셋팅
#options.add_argument('--blink-settings=imagesEnabled=false') # 이미지 로딩안하게 옵션셋팅

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#driver.implicitly_wait(time_to_wait=5) # 로딩대기 (암묵적) 최대 5초까지

driver.get(url=URL)
tabs = driver.window_handles
driver.implicitly_wait(time_to_wait=5)

# 차량검색
driver.switch_to.window(driver.window_handles[0])
keyword = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/table/tbody/tr[1]/td/ul/li/input") # 검색 속성 찾기
#keyword.send_keys("28어2384")  # 검색어 입력
keyword.send_keys("27고0144")  # 검색어 입력

keyword = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/table/tbody/tr[2]/td/ul/li/input") # 검색 속성 찾기
#keyword.send_keys("960324")  # 검색어 입력
keyword.send_keys("790227")  # 검색어 입력

keyword.send_keys("\ue007") # 검색후 enter키 입력

msg = (driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[1]/div").text)
#print(driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[1]/div/span/p[1]/span"))

if msg == '검사예약 진행 가능합니다. \
※ 추가정보 \
- 검사 당일 기준 보험 미가입자는 검사를 받으실 수 없습니다.' :
    keyword = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[2]/button") # 계속진행
    keyword.send_keys("\ue007")  # 검색후 enter키 입력 -- 다음페이지 이동

    #data1 = driver.find_element("/html/body/div[1]/div[4]/div[1]/form/table/tbody/tr[1]/td")  # 검사구분 ex)종합검사, 부하검사 같이 받아올수 있지 확인해야 하는 영역
    #data1 = driver.find_element("/html/body/div[1]/div[4]/div[1]/form/table/tbody/tr[1]/td/ul[2]/li/p/span")  # 검사구분 ex)부하검사영역 받아올수 있는지 확인해야 함


    data1 = driver.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div[1]/form/table/tbody/tr[1]/td/ul[1]/li") # 검사구분 ex)종합검사 영역
    data2 = driver.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div[1]/form/table/tbody/tr[3]/td[1]/ul/li/input[1]") # 검사기간1 (검사 만료일)
    data3 = driver.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div[1]/form/table/tbody/tr[3]/td[1]/ul/li/input[2]") # 검사기간2 (검사 만료일)
    data4 = driver.find_element(By.XPATH, f"/html/body/div[2]/div[4]/div[1]/form/table/tbody/tr[3]/td[2]") # 차명

    print(data1.text,data2.text,data3.text,data4.text)

else:# 차량 검사 일자가 아닐시
    fdata = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[1]")
    edata = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[2]")
    pdata = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[1]/div/span/span[3]")

    print(fdata.text)
    print(edata.text)
    print(pdata.text)

