import pyyoutube
from time import *
#webscraping libary

from selenium import webdriver

# variables
api = pyyoutube.Api(api_key='AIzaSyC52css0A3UeTZme1tHj0BRWT1JET-eUuM')
api.get_authorization_url()
id = 'UCC7fJamx8-ycCtcCHyjWDnA'
url = 'https://www.youtube.com/'
driverPath = '/Users/kavinselvaraj/Own_Projects/automation/youtube-alert/chromedriver'


def WebScraping():
    channel_by_id = api.get_channel_info(channel_id=id)
    data = channel_by_id.items[0].to_dict()
    print(data)
    sleep(3)


WebScraping()
