from html.parser import HTMLParser
import requests

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.img_url = []
    def handle_starttag(self, tag, attrs):
        my_attrs = dict(attrs)
        if('class' in list(my_attrs.keys())):
            if(my_attrs['class'] == "ProfileAvatar-image " ):
                self.img_url.append(my_attrs['src'])


def get_twitter_avatar_img_url(twitter_homepage_url):
	my_req = requests.get(twitter_homepage_url)   
	parser = MyHTMLParser()
	parser.feed(my_req.text)
	return(parser.img_url[0])