from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
driver = webdriver.Firefox()


def login():
    driver.get("http://htql.ctump.edu.vn/quanly/phonghoc/quanlylichmuonphong")
    driver.find_element_by_id("quanly").click()
    driver.find_element_by_class_name("selected").find_element_by_id("txt_Login_ten_dang_nhap").send_keys("00457")
    driver.find_element_by_class_name("selected").find_element_by_id("pw_Login_mat_khau").send_keys("thuc tap")
    driver.find_element_by_class_name("selected").find_element_by_id("pw_Login_mat_khau").submit()


login()


