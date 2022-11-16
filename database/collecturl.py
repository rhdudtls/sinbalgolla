import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
cardcnt=[]
driver = webdriver.Chrome(r'C:\Users\rhdud\OneDrive\바탕 화면\chromedriver_win32\chromedriver.exe')
url=r"https://www.nbkorea.com/product/productList.action?cateGrpCode=250110&cIdx=1280"
driver.implicitly_wait(1)
driver.get(url)
for i in range(6,100):
    try:
        cardcnt.append(driver.find_element_by_xpath('//*[@id="prodList"]/li['+str(i)+"]/div/div[2]/div[2]/p").text)
    except:
        print(len(cardcnt))
        continue
url=[]
fo=open('url.txt','w')
for i in cardcnt:
    url.append('https://www.nbkorea.com/product/productDetail.action?styleCode='+i)
    fo.write('https://www.nbkorea.com/product/productDetail.action?styleCode='+i)
    fo.write('\n')

print(url)