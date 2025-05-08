
import yake

from ..keywords import AbstractKeywordExtractor


class YakeKeywordExtractor(AbstractKeywordExtractor):
    def __init__(self):
        self._yake_extractor = yake.KeywordExtractor()

    def extract_keywords(self, text: str) -> list[tuple[str, float]]:
        return self._yake_extractor.extract_keywords(text)
