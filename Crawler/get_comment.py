from bs4 import BeautifulSoup as bs
import requests
import time
import random
import pymysql


def get_html(url):
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                   '73.0.3683.103 Safari/537.36'
               }
    cookies = {'cookie':
                        *** #cookie信息
               }
    res = requests.get(url, headers=headers, cookies=cookies)
    return res


def get_comment(html):
    movie_name = '复仇者联盟'
    connect = pymysql.connect(host='localhost', user='kilo', passwd='839211046', db='practice_database')
    cursor = connect.cursor()
    sql = """insert ignore into movie_comments(movie_name, user_name, watched, rating, rating_time, comment, 
    votes, user_url) values(%s, %s, %s, %s, %s, %s, %s, %s)"""
    soup = bs(html.text, 'html.parser')
    contents = soup.find_all('div', class_='comment')
    for content in contents:
        # 用户名
        name = content.find('a', class_='').string
        # 是否看过
        watched = content.find('span', class_=False).string
        # 评分
        if content.find('span', class_='rating') == None:
            rating = ''
        else:
            rating = content.find('span', class_='rating').get('title')
        # 评论时间
        comment_time = content.find('span', class_='comment-time').get('title')
        # 点赞数
        votes = content.find('span', class_='votes').string
        # 评论内容
        comment = content.find('span', class_='short').string
        # 用户链接
        user_url = content.find('a', class_='').get('href')
        values = (movie_name, name, watched, rating, comment_time, comment, votes, user_url)
        cursor.execute(sql, values)
    cursor.close()
    connect.commit()
    connect.close()


# def save_file(content_list):pe
#     with open('movie_comment.csv', 'w+',encoding='utf-8-sig',newline='') as f:
#         spamwriter = csv.writer(f, dialect='excel')
#         #spamwriter.writerow(['name', 'watched', 'rate', 'comment time', 'comment'])
#         for item in content_list:
#             spamwriter.writerow(item)

start = 0
while start < 25:
    url = 'https://movie.douban.com/subject/26100958/comments?start=' + str(start * 20) + \
          '&limit=20&sort=new_score&status=P'
    html = get_html(url)
    print("正在从第" + str(start + 1) + "页抓取评论")
    print(url)
    get_comment(html)
    time.sleep(random.randint(5, 10))
    start += 1
# save_file(content_list)
