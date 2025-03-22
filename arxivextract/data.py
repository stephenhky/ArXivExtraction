
from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass

from feedparser.util import FeedParserDict


class AbstractArticleEntry(ABC):
    pass


@dataclass
class BasicArticleEntry(AbstractArticleEntry):
    title: str
    authors: List[str]
    publish_time: str
    abstract: str
    arxiv_url: str

    def to_dict(self) -> dict:
        return {
            'title': self.title,
            'authors': self.authors,
            'publish_time': self.publish_time,
            'abstract': self.abstract,
            'arxiv_url': self.arxiv_url
        }

    @property
    def summary(self) -> str:
        return self.abstract

    @classmethod
    def make_entry_from_feed(cls, feed_entry: FeedParserDict) -> AbstractArticleEntry:
        return BasicArticleEntry(
            title=feed_entry.title,
            authors=[author.name for author in feed_entry.authors],
            publish_time=feed_entry.published,
            abstract=feed_entry.summary.replace('\n', ' '),
            arxiv_url=feed_entry.link
        )

