
from abc import ABC, abstractmethod
from typing import List

from keybert import KeyBERT


class AbstractKeywordExtractor(ABC):
    @classmethod
    def extract_keywords(text: str) -> List[str]:
        pass

