"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
from time import sleep

import pytest
from selene.support.shared import browser as selene_browser


@pytest.fixture(params=[('1080', '1920'), ('300', '300')])
def browser(request):
    selene_browser.config.base_url = 'https://github.com/'
    selene_browser.config.browser_name = 'chrome'
    selene_browser.config.window_height = request.param[0]
    selene_browser.config.window_width = request.param[1]


def test_github_desktop(browser):
    sleep(1)
    if int(selene_browser.config.window_width) < 1012 and int(selene_browser.config.window_width) < 500:
        pytest.skip("Not Desktop params")
    selene_browser.open('')
    selene_browser.element("//a[contains(text(),'Sign in')]").click()
    sleep(1)


def test_github_mobile(browser):
    sleep(1)
    if int(selene_browser.config.window_width) >= 1012 and int(selene_browser.config.window_width) >= 500:
        pytest.skip("Not Mobile params")
    selene_browser.open('')
    selene_browser.element("//button[@aria-label='Toggle navigation'][@aria-expanded='false']").click()

    selene_browser.element("//a[contains(text(),'Sign in')]").click()
    sleep(1)
