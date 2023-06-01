import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
from selenium.webdriver.chrome.options import Options

ch_options = Options()
ch_options.add_argument("--headless")  # => for headless mode

# 在启动浏览器时加入配置
cucnSys = webdriver.Chrome(chrome_options=ch_options) # time sys


cucnSys.implicitly_wait(10)

cucnSys.get("http://58.213.148.137/jwglxt/xtgl/login_slogin.html")


#WebElement
#用户输入
usname = cucnSys.find_element(By.ID, "yhm")
passkey = cucnSys.find_element(By.ID, "mm")

'''
"20220819124"
"wjx20041230"
'''

UesrName = "20220819132"
UesrKey = "Wjsd2004"
#UesrName = input("请输入用户名:")
#UesrKey = input("请输入密码:")

# 浏览器输入 use name and key
usname.send_keys(UesrName)
passkey.send_keys(UesrKey)

cucnSys.find_element(By.ID, 'dl').click()




#进入课表
cucnSys.get("http://58.213.148.137/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?gnmkdm=N253508&layout=default&su=20220819132")
cucnSys.find_element(By.XPATH, '//*[@id="tb"]/button[4]').click()
time.sleep(5)
table = cucnSys.find_element(By.ID, "ylkbTable")

# flag
row_use = []
# 获取表格中的所有行和列，并打印它们的值
for row in table.find_elements(By.TAG_NAME, "tr"):
    row_values = []
    for cell in row.find_elements(By.TAG_NAME, "td"):
        row_values.append(cell.text)
    row_use.append(row_values)




# demo

# find the index of the day
Monday = row_use.index(["星期一"])
Tuesday = row_use.index(["星期二"])
Wednesday = row_use.index(["星期三"])
Thursday = row_use.index(["星期四"])
Friday = row_use.index(["星期五"])
Saturday = row_use.index(["星期六"])
Sunday = row_use.index(["星期日"])


# 获取当前日期
today = datetime.date.today()

# 获取当前日期的月份
month = str(today.month)
day = str(today.day)
year = str(today.year)
date = year + '-' + month + '-' + day



# 返回当前天的总课表list
def weeekday(day):
    lisindex = []
    if day == 1:
        for i in range(Monday, Tuesday):
            lisindex.append(row_use[i])
    if day == 2:
        for i in range(Tuesday, Wednesday):
            lisindex.append(row_use[i])
    if day == 3:
        for i in range(Wednesday, Thursday):
            lisindex.append(row_use[i])
    if day == 4:
        for i in range(Thursday, Friday):
            lisindex.append(row_use[i])
    if day == 5:
        for i in range(Friday, Saturday):
            lisindex.append(row_use[i])
    if day == 6:
        for i in range(Saturday, Sunday):
            lisindex.append(row_use[i])
    if day == 7:
        for i in range(Sunday, len(row_use) - 1):
            lisindex.append(row_use[i])
    return lisindex


# 返回起始时间
def reStartTime(T):
    if T == 1:
        return '08:30'
    if T == 3:
        return '10:25'
    if T == 5:
        return '14:00'
    if T == 7:
        return '15:55'
    if T == 9:
        return '18:30'
    if T == 11:
        return '20:15'

# 返回结束时间
def reEndTime(T):
    if T == 2:
        return '10:05'
    if T == 4:
        return '12:00'
    if T == 6:
        return '15:30'
    if T == 8:
        return '17:30'
    if T == 10:
        return '20:05'
    if T == 12:
        return '21:50'


# 返回总时间
def reTime(txt):
    indexJ = txt.index('-')
    Start = int(txt[0 : indexJ])
    end = int(txt[(indexJ + 1) : len(txt)])
    F = reStartTime(Start) + '~' + reEndTime(end)
    return F

# 返回单个课程名信息
def reSnamelession(list):
    index = list[1].index('\n')
    lsname = list[1][0:index]
    return lsname

# 返回单个课程上课周数
def reSweeklession(list):
    index = list[1].index('周数')
    index1 = list[1].index('校区')
    lweek = list[1][(index + 3):(index1 - 1)]
    return lweek

# 返回上课地点
def reSlocationlession(list):
    index = list[1].index('上课地点')
    llocation = list[1][(index + 5):(index + 10)]
    return llocation

# 返回上课教师
def reSteacherlession(list):
    index = list[1].index('教师')
    index1 = list[1].index('教学班')
    lteacher = list[1][(index + 3):(index1 - 1)]
    return lteacher


def sysDitance(list):
    print(date)

    for i in range(1, len(list)):
        
        time = reTime(list[i][0])
        lsname = reSnamelession(list[i])
        lweek = reSweeklession(list[i])
        llocation = reSlocationlession(list[i])
        lteacher = reSteacherlession(list[i])
        print(time, lsname, lweek, llocation, lteacher, sep='  ')



today = 1
print(today)
list1 = weeekday(today)
sysDitance(list1)


'''
print()
# 参考
print(list1)
print(row_use)
'''