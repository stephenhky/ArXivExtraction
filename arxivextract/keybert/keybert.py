
from keybert import KeyBERT

from ..keywords import AbstractKeywordExtractor, DEFAULT_SENTENCEEMBED


class KeywordBertKeywordExtractor(AbstractKeywordExtractor):
    def __init__(self, config: dict, embed_model=DEFAULT_SENTENCEEMBED):
        self._keyword_model = KeyBERT(model=embed_model)
        self._config = config

    def extract_keywords(self, text: str) -> list[str]:
        return self._keyword_model.extract_keywords(text, **self._config)

    @property
    def keywordbertmodel(self) -> KeyBERT:
        return self._keyword_model
