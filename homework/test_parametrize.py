"""
Переопределите параметр с помощью indirect
"""
from time import sleep

import pytest
from selene.support.shared import browser as selene_browser


@pytest.fixture(params=[])
def browser(request):
    selene_browser.config.base_url = 'https://github.com/'
    selene_browser.config.browser_name = 'chrome'
    selene_browser.config.window_height = request.param[0]
    selene_browser.config.window_width = request.param[1]


@pytest.mark.parametrize('browser', [('1080', '1920')], indirect=True)
def test_github_desktop(browser):
    sleep(1)
    selene_browser.open('')
    selene_browser.element("//a[contains(text(),'Sign in')]").click()
    sleep(1)


@pytest.mark.parametrize('browser', [('300', '300')], indirect=True)
def test_github_mobile(browser):
    sleep(1)
    selene_browser.open('')
    selene_browser.element("//button[@aria-label='Toggle navigation'][@aria-expanded='false']").click()

    selene_browser.element("//a[contains(text(),'Sign in')]").click()
    sleep(1)
