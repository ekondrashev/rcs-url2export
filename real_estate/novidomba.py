from selenium import webdriver
import pprint
import xlwt
pp = pprint.PrettyPrinter()

proxyHost = "212.210.138.140"
proxyPort = "53281"

fp = webdriver.FirefoxProfile()
fp.set_preference("network.proxy.type", 1)
fp.set_preference("network.proxy.http", proxyHost) #HTTP PROXY
fp.set_preference("network.proxy.http_port", int(proxyPort))
fp.set_preference("network.proxy.ssl", proxyHost) #SSL PROXY
fp.set_preference("network.proxy.ssl_port", int(proxyPort))
fp.set_preference('network.proxy.socks', proxyHost) #SOCKS PROXY
fp.set_preference('network.proxy.socks_port', int(proxyPort))
fp.update_preferences()

driver = webdriver.Firefox(firefox_profile=fp)
#driver = webdriver.Firefox()
driver.get('http://novidom.ba/')

b = []
link1 = []
name1 = []
price = []
page = 2
while page < 6:
    body = driver.find_elements_by_xpath('/html/body/div[5]/div/div[2]/div/div[3]')
    for body_1 in body:
        search_el = body_1.find_elements_by_class_name('idk_realtestate5padding')
        for elements in search_el:
            main_img = elements.find_elements_by_class_name('img-responsive')
            for link in main_img:
                attr_link = link.get_attribute('src')
                a = attr_link
                link1.append(a)
            name = elements.find_elements_by_tag_name('h2')
            for name_res in name:
                name_result = name_res.text
                name1.append(name_result)
                #pp.pprint(nae.text)
            search_price = elements.find_elements_by_class_name('idk_realestate_info-price')
            for pric in search_price:
                result_price = pric.text
                price.append(result_price)
            id_state = elements.find_elements_by_class_name('realestate_more_info')
            for link_id in id_state:
                href_link = link_id.get_attribute('href')
                id_result = href_link[-3:]
                b.append(id_result)
    driver.get("http://novidom.ba/page/%d" % page)
    page += 1

wb = xlwt.Workbook()
ws = wb.add_sheet('Test Sheet')
i = 0
iw = 0
ip = 0
io = 0
for row in range(len(b)):
    col = 0
    if row == 0:
        ws.write(row, col , b[i])
    else:
        i = i + 1
        ws.write(row, col, b[i])
for rows in range(len(link1)):
    col = 1
    if rows == 0:
        ws.write(rows, col , link1[iw])
    else:
        iw = iw + 1
        ws.write(rows, col, link1[iw])
for row_name in range(len(name1)):
    col = 2
    if row_name == 0:
        ws.write(row_name, col , name1[ip])
    else:
        ip = ip + 1
        ws.write(row_name, col, name1[ip])
for row_price in range(len(price)):
    col = 3
    if row_price == 0:
        ws.write(row_price, col , price[io])
    else:
        io = io + 1
        ws.write(row_price, col, price[io])
wb.save('tes.xls')




