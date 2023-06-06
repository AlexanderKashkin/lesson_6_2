from selene.support.shared import browser
from selene import be, have


def test_search_selene(set_window_size_height, set_window_size_width):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_smth(set_window_size_height, set_window_size_width):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fsdlkjfsfdjlkdflsdf').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
