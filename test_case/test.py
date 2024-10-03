


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # 创建 WebDriver 对象，指明使用chrome浏览器驱动
# wd = webdriver.Chrome(service=Service(r'D:\DevTools\webdrivier\chromedriver-win64\chromedriver.exe'))

# # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.baidu.com')

# # 等待页面加载
# time.sleep(2)

# # 找到搜索框元素
# search_box = wd.find_element(By.ID, 'kw')  # 使用ID定位搜索框

# # 输入搜索内容"鱼香肉丝"
# search_box.send_keys('鱼香肉丝')

# # 提交搜索，点击"百度一下"按钮
# search_button = wd.find_element(By.ID, 'su')  # 使用ID定位搜索按钮
# search_button.click()  # 点击提交按钮

# # 等待搜索结果加载
# time.sleep(3)

# # 这里可以添加进一步的操作，比如处理搜索结果

# # 等待用户输入，防止程序结束后浏览器闪退
# input('等待回车键结束程序')

# # 关闭浏览器
# wd.quit()

import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
# 初始化 WebDriver（记得替换路径）
driver = webdriver.Chrome(service=Service(r'D:\DevTools\webdrivier\chromedriver-win64\chromedriver.exe'))


def test_baidu_search():
    try:
        # 打开百度首页
        driver.get("https://www.baidu.com")

        # 查找搜索框元素
        search_box = driver.find_element(By.ID, "kw")

        # 输入搜索内容
        search_box.send_keys("Selenium Python")

        # 提交搜索表单
        search_box.send_keys(Keys.RETURN)

        # 等待搜索结果加载
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "content_left"))
        )

        # 打印页面标题
        print("页面标题是:", driver.title)
        assert  "Selenium Python_百度搜索111"==driver.title

    finally:
        # 关闭浏览器
        driver.quit()



def f():
    raise ExceptionGroup(
        "Group message",
        [
            RuntimeError(),
        ],
    )


def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        f()
    assert excinfo.group_contains(RuntimeError)
    assert not excinfo.group_contains(TypeError)


def test_jsk():
    assert 1==1




# 定义测试用例
def test_value_in_excel():
    # 加载 Excel 文件
    workbook = openpyxl.load_workbook('assets/abc.xlsx')
    sheet = workbook.active  # 获取活动的工作表
    
    # 获取第 10 行 D 列的值
    cell_value = sheet['D10'].value
    
    # 断言检查
    assert cell_value == "abcde", f"Expected value 'abcde', but got '{cell_value}'"

# 如果你希望直接运行测试，可以在此添加如下代码：
if __name__ == "__main__":
    pytest.main()