from product.scripts.parser import Parser

# Create your tests here.
def test_should_remove_upper_case():
    assert Parser.remove_upper_case('ABC') == 'abc'

def test_should_remove_ponctuation():
    assert Parser.remove_ponctuation('a.b!c?') == 'abc'

def test_should_remove_accent():
    assert Parser.remove_accent('áôè') == 'aoe'

def test_should_remove_space():
    assert Parser.remove_space(' a  b   c    ') == 'abc'

def test_should_parse():
    assert Parser.parse('Á  B ? c .') == 'abc'