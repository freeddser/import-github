#!/usr/bin/env python
# encoding: utf-8
"""
@version: 0.1
@author: gavin.li
@license: Apache Licence 
@contact: scpman@live.com gavin@01.work
@site: https://www.01.work
"""

from selenium import webdriver
from config import *
import time
browser = webdriver.Chrome()
# login
browser.get('https://github.com/new/import')
browser.find_element_by_id("login_field").send_keys(github_accout_id)
browser.find_element_by_id("password").send_keys(github_account_password)
browser.find_element_by_name("commit").click()

# start import
repos=[
    'gitlab.01.work/golang/kf.git,gavin/golang/kf',

    ]

for repo in repos:
    time.sleep(3)
    data=repo.split(",",-1)
    vcs_url="http://"+git_account_id+":"+git_account_password+"@"+data[0]
    repository_name=data[1]
    print(vcs_url,"~~~~~",repository_name)
    browser.get('https://github.com/new/import')
    browser.find_element_by_id("vcs_url").send_keys(vcs_url)
    browser.find_element_by_id("repository_name").send_keys(repository_name)
    browser.find_element_by_id("repository_visibility_private").click()
    from selenium.webdriver.common.action_chains import ActionChains
    www01work =browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
    ActionChains(browser).double_click(www01work).perform()
