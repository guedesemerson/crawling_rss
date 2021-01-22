import requests
from bs4 import BeautifulSoup
from database import post_feed, connect_db, list_feed

link_parameter = 'https://g1.globo.com/rss/g1/tecnologia/'
db_collection = connect_db()
db_collection.delete_many({})


def get_rss_feed_content():
    try:
        r = requests.get(link_parameter)
        soup = BeautifulSoup(r.content, features='xml')
        tag = soup.findAll('item')
        for content in tag:
            title = content.find('title').text
            link = content.find('link').text
            guid = content.find('guid').text
            description = content.find('description').text
            media = content.find('media:content')
            category = content.find('category').text
            pub_date = content.find('pubDate').text

            content_dict = {
                'title': title,
                'link': link,
                'guid': guid,
                'description': description,
                'media': str(media),
                'category': category,
                'pubDate': pub_date
            }
            post_feed(db_collection, content_dict, guid)


    except Exception as e:
        print(e)


get_rss_feed_content()
list_feed(db_collection)
