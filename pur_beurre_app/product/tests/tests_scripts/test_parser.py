from product.scripts.parser import Parser


# Create your tests here.
def test_should_remove_upper_case():
    sut = Parser
    text = 'ABC'
    expected_value = 'abc'
    assert sut.remove_upper_case(text) == expected_value


def test_should_remove_ponctuation():
    sut = Parser
    text = 'a.b!c?'
    expected_value = 'abc'
    assert sut.remove_ponctuation(text) == expected_value


def test_should_remove_accent():
    sut = Parser
    text = 'áôè'
    expected_value = 'aoe'
    assert sut.remove_accent(text) == expected_value


def test_should_remove_space():
    sut = Parser
    text = ' a  b   c    '
    expected_value = 'abc'
    assert sut.remove_space(text) == expected_value


def test_should_parse():
    sut = Parser
    text = 'Á  B ? c .'
    expected_value = 'abc'
    assert sut.parse(text) == expected_value
