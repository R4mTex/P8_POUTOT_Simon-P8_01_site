import string
import unidecode


class Parser:

    def remove_upper_case(text_to_parse):
        return str(text_to_parse).lower()

    def remove_ponctuation(text_to_parse):
        return text_to_parse.translate(str.maketrans('', '', string.punctuation))

    def remove_accent(text_to_parse):
        return unidecode.unidecode(text_to_parse)

    def remove_space(text_to_parse):
        return text_to_parse.replace(" ", "")

    def parse(text_to_parse):
        text_removed_upper_case = Parser.remove_upper_case(text_to_parse)
        text_removed_ponctuation = Parser.remove_ponctuation(text_removed_upper_case)
        text_removed_accent = Parser.remove_accent(text_removed_ponctuation)
        text_removed_space = Parser.remove_space(text_removed_accent)
        text_parsed = text_removed_space
        return text_parsed
