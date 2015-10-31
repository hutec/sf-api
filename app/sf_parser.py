import requests
from bs4 import BeautifulSoup

POSTS_PER_PAGE = 15
url = "http://www.styleforum.net/t/"

def get_thread(id, page_number):
    posts = []
    thread_url = url + str(id) + '/' + str(page_number*POSTS_PER_PAGE)
    print("Fetching " + thread_url)
    soup = BeautifulSoup(requests.get(thread_url).content)
    for post in soup.findAll('div', id=lambda x: x and x.startswith('content_')):
        posts.append(post.text)
    return posts
    

def test():
    #url = "http://www.styleforum.net/t/222059/"
    url = "http://www.styleforum.net/t/394687/"
    site_index = 15
    posts = []
    number_of_pages = 20 
    for site_index in range(0, 15*number_of_pages, 15):
        print("Reading " + url+str(site_index))
        soup = BeautifulSoup(requests.get(url+str(site_index)).content)
        for post in soup.findAll('div', id=lambda x: x and x.startswith('content_')):
            posts.append(post)
    return posts
