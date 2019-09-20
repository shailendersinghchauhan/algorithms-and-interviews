from selenium import webdriver
from selenium.webdriver.common import keys
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#import selenium
#selenium.webdriver.common.keys
import time
import os

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
#       binary = FirefoxBinary('C:\Python37-32\Lib\site-packages\selenium')
#       self.bot = webdriver.Firefox(firefox_binary=binary)
        self.bot = webdriver.Firefox()
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_element_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                # try:
                #     bot.find_element_by_class_name('HeartAnimation').click()
                #     time.sleep(10)

if __name__ == '__main__':
    ed = TwitterBot('username','test')
    ed.login()
    ed.like_tweet('webdevelopment')