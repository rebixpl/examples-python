#! /usr/bin/python3

from selenium import webdriver
import os
import time

import configparser

class InstagramBot:

    def __init__(self, username, password):
        """
        Initializes an instance of the InstagramBot class. 
        Calls the login method to authenticate the user with IG.

        Args:
            username:str: The Instagram username for a user
            password:str: The Instagram password for a user

        Attributes:
            driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions
        """

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver')

        self.login()

        
    def login (self): 
        self.driver.get('{}/accounts/login/'.format(self.base_url))

        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        
        time.sleep(2)


    def nav_user(self, user):
        """
        Args:
            user:str: The username of the instagram user

        Navigate to the users page
        """
        self.driver.get('{}/{}/'.format(self.base_url, user))


    def follow_user(self, user):
        """
        Args:
            user:str: The username of the instagram user

        Follows user
        """
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()


    def unfollow_user(self, user):
        """
        Args:
            user:str: The username of the instagram user

        Unfollows user
        """
        self.nav_user(user)
        unfollow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Following')]")[0]
        #print(clear)
        #print(unfollow_button)
        unfollow_button.click()

        #unfollow_button_confirm = self.driver.find_elements_by_xpath()



if __name__ == '__main__':

    config_path = './config.ini'
    cparser = configparser.ConfigParser()
    cparser.read(config_path)
    username = cparser['AUTH']['USERNAME']
    password = cparser['AUTH']['PASSWORD']

    ig_bot = InstagramBot(username, password)
    # ig_bot.nav_user('willsmith')
    ig_bot.follow_user('willsmith')