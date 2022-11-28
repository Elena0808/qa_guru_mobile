from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step


def test_search():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'BrowserStack'
        )
    with step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))


def test_open_settings():
    with step('Open page settings'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/menu_overflow_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/explore_overflow_settings")).click()
    with step('Check settings'):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.text('Settings'))