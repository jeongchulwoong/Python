import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import math
import numpy as np
from sklearn.preprocessing import normalize
from datetime import datetime
import bs4
from konlpy.tag import *
from time import *
import json


def date_form(x):
    if (x > 0) & (x < 10):
        return '0' + str(x)
    elif x > 10:
        return str(x)


def get_soup(url):  # soup 객체를 가져옴
    res = requests.get(url)
    if res.status_code == 200:
        return bs(res.text, 'html.parser')
    else:
        print(f"Super big fail! with {res.status_code}")


def get_newslist(t):  # 한 시간 동안(X시 대)의 뉴스 목록 가져오기 ex) 4시 48분일 경우 3:00~3:59의 기사를 가져옴
    time_now = gmtime(t + 28800)  # 현재 시간보다 한 시간 전 GMT + 8
    time_bef = gmtime(t + 25200)  # 현재 시간보다 두 시간 전 GMT + 7
    datetime_now = [time_now.tm_year, time_now.tm_mon, time_now.tm_mday, time_now.tm_hour]
    datetime_bef = [time_bef.tm_year, time_bef.tm_mon, time_bef.tm_mday, time_bef.tm_hour]

    print(time_now)

    metadatas_tuple = read_json(datetime_now, datetime_bef)
    metadatas = []
    for metadata in metadatas_tuple:
        temp_dict = dict()
        temp_dict['oid'] = metadata[0]
        temp_dict['aid'] = metadata[1]
        temp_dict['datetime'] = metadata[2]
        metadatas.append(temp_dict)

    data_frame = pd.DataFrame(metadatas)
    print(data_frame)

    return metadatas


def get_newsdata(metadatas):
    news_in_hour = []
    for metadata in metadatas:
        news_URL = 'https://sports.news.naver.com/news?oid=' + metadata['oid'] + '&aid=' + metadata['aid']
        soup = get_soup(news_URL)
        article = soup.find('div', attrs={"id": "newsEndContents"})
        for child in article.children:
            if isinstance(child, bs4.element.Tag):
                child.decompose()
        title = soup.select_one('.title').get_text()
        news_content = article.get_text()  # 기사 내용만 가져오기
        print(f"Title: {title}")
        print(f"Article: {news_content}")
        print("\n---\n")
    return news_in_hour


def read_json(now, bef):  # json 형식의 파일을 한 시간 단위로 긁어오기
    page = 1
    dup_cnt = 0
    metadatas = []
    while dup_cnt < 10:
        dup = 0
        news_list_URL = 'https://sports.news.naver.com/wfootball/news/list?isphoto=N&date=' + date_form(now[0]) \
                        + date_form(now[1]) + date_form(now[2]) + '&page=' + str(page)
        soup = str(get_soup(news_list_URL))
        news_metadata = json.loads(soup)
        for metadata in news_metadata['list']:  # 뉴스 메타데이터 한 건 당
            for i in metadatas:
                if (i[0] == metadata['oid']) & (i[1] == metadata['aid']):  # 메타데이터 중복 시
                    dup_cnt += 1
                    dup = 1
                    break
            if dup == 1: continue  # 데이터가 중복일 경우 다음 메타데이터로 바로 넘어감
            datetime = re.split("[ .:]", metadata['datetime'])
            # 시간 단위들을 int형으로 변환
            for i in range(0, len(datetime)):
                datetime[i] = int(datetime[i])
            # 지금보다 한 시간 전일 경우 수집
            if (datetime[0] == now[0]) & (datetime[1] == now[1]) & (datetime[2] == now[2]) & (datetime[3] == now[3]):
                metadata_tuple = (metadata['oid'], metadata['aid'], metadata['datetime'])
                metadatas.append(metadata_tuple)
                print(metadata_tuple)
            elif (datetime[0] == bef[0]) & (datetime[1] == bef[1]) & (datetime[2] == bef[2]) & (
                    datetime[3] == bef[3]):  # 두 시간 전 기사 만날 경우 끝
                return set(metadatas)
        page += 1
    return set(metadatas)


def quotation_preprocess(sen):  # 인용절 속 종결 기호를 마킹, 대괄호 삭제
    alphabet_list = []
    in_quotation = 0  # 문장 마침 기호가 인용문에 있는지
    in_SB = 0  # 문자가 대괄호 안에 있는지

    for a in sen:
        if ((a == '\"') | (a == '\'')) & (in_quotation == 0):  # 쿼테이션 열림
            in_quotation = 1
        elif ((a == '\"') | (a == '\'')) & (in_quotation == 1):  # 쿼테이션 닫힘
            in_quotation = 0
        if a == '[':  # 대괄호 열림
            in_SB = 1
        elif a == ']':  # 대괄호 닫힘
            a = ""
            in_SB = 0

        if in_SB == 1:  # 대괄호 안에 있는 문자 삭제
            a = ""
        if (a == '.') & (in_quotation == 1):
            a = '<spot>'
        if (a == '!') & (in_quotation == 1):
            a = '<exclamation>'
        if (a == '?') & (in_quotation == 1):
            a = '<question>'
        if (a == ';') & (in_quotation == 1):
            a = '<semicolon>'
        if (a == '\\') & (in_quotation == 1):
            a = '<backslash>'

        alphabet_list.append(a)

    return ''.join(alphabet_list)


def quotation_postprocess(sen):  # 마킹한 종결 기호를 원래대로
    sen = sen.replace("<spot>", '.')
    sen = sen.replace("<exclamation>", '!')
    sen = sen.replace("<question>", '?')
    sen = sen.replace("<semicolon>", ';')
    sen = sen.replace("<backslash>", '\\')

    return sen

if __name__ == '__main__':
    data = get_newslist(time() - 3600)
    get_newsdata(data)