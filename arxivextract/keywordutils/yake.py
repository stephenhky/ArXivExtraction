
from typing import Tuple

import yake

from ..keywords import AbstractKeywordExtractor


class YakeKeywordExtractor(AbstractKeywordExtractor):
    def __init__(self):
        self._yake_extractor = yake.KeywordExtractor()

    def _get_keyword_extraction_info(self, text: str) -> list[Tuple[str, float]]:
        return self._yake_extractor.extract_keywords(text)

    def extract_keywords(self, text: str) -> list[str]:
        info = self._get_keyword_extraction_info(text)
        return [keyword for keyword, _ in info]