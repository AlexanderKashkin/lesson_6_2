import pytest
from selene.support.shared import browser


@pytest.fixture(params=['2400', '1920'])
def set_window_size_height(request):
    browser.config.window_height = request.param


@pytest.fixture(params=['1080', '720'])
def set_window_size_width(request):
    browser.config.window_width = request.param
