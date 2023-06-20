from selenium import webdriver
import csv


def get_info():  # 获取到每个城市每天的天气情况,并写入CSV文件
    infos = driver.find_elements_by_xpath('//div[@id="content"]/table/tbody/tr[position()>1]')
    for info in infos:
        date_city = info.find_element_by_xpath('./td[1]/a').get_attribute("title")  # 定位日期和城市
        weather = info.find_element_by_xpath('./td[2]').text  # 定位天气
        temperature = info.find_element_by_xpath('./td[3]').text.split('/')  # 定位温度
        highest_temperature = temperature[0]  # 得到日最高温度
        lowest_temperature = temperature[-1]  # 得到日最低温度
        wind = info.find_element_by_xpath('./td[4]').text.split('/')[0]  # 定位风向风力
        if '中雨' in weather or '大雨' in weather or '暴雨' in weather or '雷阵雨' in weather or '霾' in weather or '扬沙' in weather or '冰雹' in weather or '雪' in weather or '6' in wind:
            severe_weather = '是'  # 通过天气情况是否为中雨,大雨,暴雨,雷阵雨,霾,扬沙,冰雹,雪,风力达到6级来判断天气是否恶劣,若有则该城市当天天气为恶劣天气
        else:
            severe_weather = '否'  # 若无以上天气情况,则该城市当天不是恶劣天气
        print(date_city, weather, highest_temperature, lowest_temperature, wind, severe_weather, sep="|")
        with open("广州历史天气数据.csv", 'a', newline="", encoding='utf-8') as f:
            csvwriter = csv.writer(f, delimiter=',')
            csvwriter.writerow([date_city, weather, highest_temperature, lowest_temperature, wind, severe_weather])
            # 将获取到的'日期/城市', '天气', '最高温', '最低温', '风向风力', '是否为恶劣天气'这些数据写入文件


def main():  # 月份组合构造url

    months = ['201805', '201806', '201807', '201808', '201809', '201810', '201811', '201812',
              '201901', '201902', '201903', '201904', '201905', '201906', '201907', '201908', '201909', '201910',
              '201911', '201912',
              '202001', '202002', '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010',
              '202011', '202012',
              '202101', '202102', '202103', '202104', '202105', '202106', '202107', '202108', '202109', '202110',
              '202111', '202112',
              '202201', '202202', '202203', '202204', '202205', '202206', '202207', '202208', '202209', '202210',
              '202211', '202212',
              '202301', '202302', '202303', '202304', '202305']
    for month in months:
        url = "http://www.tianqihoubao.com/lishi/guangzhou/month/{}.html".format(month)  # 构造url
        driver.get(url)

        driver.maximize_window()
        driver.implicitly_wait(5)
        get_info()
        print('*' * 100)
        print("广州{}的天气数据爬取完成".format(month))
        print('*' * 100)


if __name__ == '__main__':
    url = "http://www.tianqihoubao.com/lishi/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)
    with open("广州历史天气数据.csv", 'a', newline="", encoding='utf-8') as f:
        csvwriter = csv.writer(f, delimiter=',')
        csvwriter.writerow(['日期/城市', '天气', '最高温', '最低温', '风向风力', '是否为恶劣天气'])
    main()
