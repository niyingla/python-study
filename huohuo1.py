import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

class PopulationCrawler:

    @staticmethod
    def fetch_content(get_data_url):
        try:
            response = requests.get(get_data_url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"请求失败: {e}")
            return None

    @staticmethod
    def parse_content( get_data_url):
        html_content = PopulationCrawler.fetch_content(get_data_url)
        soup = BeautifulSoup(html_content, 'html.parser')
        cur_population_data = {}

        # 假设每个县的信息在一个特定的表格中
        table = soup.find('table')  # 根据实际情况调整选择器
        rows = table.find_all('tr')

        for row in rows[1:]:  # 跳过表头
            cols = row.find_all('td')
            if len(cols) >= 2:  # 假设县名在第一列，人口数在第二列
                county_name = cols[1].get_text().strip()
                population = cols[2].get_text().strip()
                cur_population_data[county_name] = population

        # #翻页
        next_page = soup.find('li', {'class': 'next-page'})
        if next_page:
            # <li class="next-page"><a href="https://www.hongheiku.com/ccategory/xianjirank/xianjirank/page/2">下一页</a></li>>
            # 获取href的链接
            find = next_page.find('a')
            if find:
                next_page_url = find.get("href")
                if next_page_url:
                    next_page_url =  next_page_url
                    cur_population_data.update(PopulationCrawler.parse_content(next_page_url))

        return cur_population_data

    @staticmethod
    def get_data_to_excel(data, p_name):
        merge_row_list = []
        row_list = list(data.items())
        for row in row_list:
            city_name = row[0]
            # [深圳]宝安区 通过正则，读取[]内的内容
            area_name  = ''
            if '[' in city_name:
                city_name = city_name.split(']')[0]
                city_name = city_name[1:]
                area_name = row[0].split(']')[1]

            merge_row_list.append((p_name,city_name, area_name, row[1]))
        return merge_row_list

    @staticmethod
    def get_data(cur_url,p_name):
        cur_crawler = PopulationCrawler()
        print(f'正在拉取{p_name}数据')
        cur_population_data = cur_crawler.parse_content(cur_url)
        cur_excel = cur_crawler.get_data_to_excel(cur_population_data, p_name)
        print(f'拉取{p_name}数据完成')
        return cur_excel


if __name__ == "__main__":
    excel_data=[]
    url = 'https://www.hongheiku.com/category/xianjirank/hunanrank' 
    excel_data.append(PopulationCrawler.get_data(url, '湖南'))

    url = 'https://www.hongheiku.com/category/xianjirank/hbsxsqrk' 
    excel_data.append(PopulationCrawler.get_data(url, '湖北'))

    url = 'https://www.hongheiku.com/category/xianjirank/gdxsqpm' 
    excel_data.append(PopulationCrawler.get_data(url, '广东'))

    url = 'https://www.hongheiku.com/category/xianjirank/gxxsq'
    excel_data.append(PopulationCrawler.get_data(url, '广西'))
    
    row_list_new=[]

    for excel_datum in excel_data:
        for population_datum in excel_datum:
            row_list_new.append(population_datum)

    print('开始生成excel')
    df = pd.DataFrame(row_list_new, columns=['省','市', '县', '人口数'])
    df.to_excel("县人口统计.xlsx", index=False)
    print('生成excel完成')
    #3s后关闭窗口
    time.sleep(3)