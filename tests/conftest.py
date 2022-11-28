import os
import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from dotenv import load_dotenv
from selene.support.shared import browser

from qa_guru_mobile.utils import attach


@pytest.fixture(scope='function', autouse=True)
def driver_management():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities({
        "app": os.getenv('app'),
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": os.getenv('userName'),
            "accessKey": os.getenv('accessKey'),
        }
    })
    browser.config.driver = webdriver.Remote(
    "http://hub.browserstack.com/wd/hub", options=options)

    yield
    attach.add_video(browser)
    browser.quit()