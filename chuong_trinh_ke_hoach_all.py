import csv

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
driver.implicitly_wait(10)


def login():
    driver.get("http://htql.ctump.edu.vn")
    driver.find_element_by_id("quanly").click()
    driver.find_element_by_class_name("selected").find_element_by_id("txt_Login_ten_dang_nhap").send_keys("")
    driver.find_element_by_class_name("selected").find_element_by_id("pw_Login_mat_khau").send_keys("")
    driver.find_element_by_class_name("selected").find_element_by_id("pw_Login_mat_khau").submit()


def index_page():
    driver.get("http://htql.ctump.edu.vn/quanly/ctdt/ctdtkhoilop")


def link_tung_nganh():
    link_nganh = list()
    rows = driver.find_element_by_xpath('//*[@id="tb_list"]/tbody').find_elements_by_tag_name("tr")
    try:
        for row in rows:
            link_nganh.append(row.find_element_by_css_selector('.center.pointer').find_elements_by_tag_name("img")[0])
    finally:
        return link_nganh

def get_links(list_of_link):
    links = list()
    for link in list_of_link:
        links.append(link.get_attribute("name"))
    return links

def save_data(link):
    driver.get("http://htql.ctump.edu.vn/quanly/ctdt/ctdtkhoilop")
    driver.find_element_by_name(link).click()
    outputFile = open('output.csv', 'a', encoding='utf-8', newline='')
    outputWriter = csv.writer(outputFile)
    he_nganh_khoa = driver.find_element_by_xpath('//*[@id="lb_ThemKHDT_info"]')
    for r in driver.find_element_by_xpath('//*[@id="tb_list"]/tbody').find_elements_by_tag_name("tr"):
        try:
            mmh = r.find_elements_by_tag_name("td")[0]
            tmh = r.find_elements_by_tag_name("td")[1]
            print(mmh.text + "," + tmh.text + "," + he_nganh_khoa.text + "," + "\n")
        except:
            pass
        outputWriter.writerow([mmh.text, tmh.text, he_nganh_khoa.text])
    outputFile.close()
    driver.find_element_by_xpath('//*[@id="btTroVe"]').click()


if __name__ == '__main__':
    login()
    index_page()
    links = get_links(link_tung_nganh())
    for link in links:
        save_data(link)
    driver.close()
