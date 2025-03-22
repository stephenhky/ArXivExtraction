
import urllib.request

import feedparser


base_url = 'http://export.arxiv.org/api/query?'



class ArXivExtractor:
    def retrieve_articles(self, dts, start=0, max_results=100):
        query = 'search_query=submittedDate:[{dts:}0000+TO+{dts:}2359]&start={start:}&max_results={max_results:}&sortBy=submittedDate&sortOrder=ascending'.format(
            dts=dts,
            start=start,
            max_results=max_results
        )

        url = base_url + query

        response = urllib.request.urlopen(url).read()
        feed = feedparser.parse(response)

        articles = []
        for entry in feed.entries:
            article = {
                'title': entry.title,
                'authors': [author.name for author in entry.authors],
                'published': entry.published,
                'summary': entry.summary,
                'arxiv_url': entry.link
            }
            articles.append(article)

        return articles
            