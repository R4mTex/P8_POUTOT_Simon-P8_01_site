from product.scripts.downloader import Downloader


def test_should_return_a_list_empty_of_dict(monkeypatch):
    sut = Downloader
    
    def mockreturn():
        return [{}]

    monkeypatch.setattr(sut, 'get_products', mockreturn)

    expected_value = [{}]
    assert sut.main_function() == expected_value


"""
from product.management.commands.populate_bdd import Command

class MockResponse:

    @staticmethod
    def get_products():
        return [{}]

def test_command_handle(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr('downloader.Downloader', mock_get)

    expected_value = [{}]
    assert Command.handle() == expected_value"
"""