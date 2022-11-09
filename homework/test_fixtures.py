"""
Сделайте разные фикстуры для каждого теста
"""
from time import sleep

import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def desktop_browser_management():
    browser.config.base_url = 'https://github.com/'
    browser.config.browser_name = 'chrome'
    browser.config.window_height = '1080'
    browser.config.window_width = '1920'


@pytest.fixture(scope='function')
def mobile_browser_management():
    browser.config.base_url = 'https://github.com/'
    browser.config.browser_name = 'chrome'
    browser.config.window_height = '300'
    browser.config.window_width = '300'


def test_github_desktop(desktop_browser_management):
    sleep(1)
    browser.open('')
    browser.element("//a[contains(text(),'Sign in')]").click()
    sleep(1)


def test_github_mobile(mobile_browser_management):
    sleep(1)
    browser.open('')
    browser.element("//button[@aria-label='Toggle navigation'][@aria-expanded='false']").click()

    browser.element("//a[contains(text(),'Sign in')]").click()
    sleep(1)
