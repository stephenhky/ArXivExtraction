
import urllib.request


base_url = 'http://export.arxiv.org/api/query?'



class ArXivExtractor:
    def retrieve_articles(date, start=0, max_results=100):
        query = f'search_query=submittedDate:[{date}0000+TO+{date}2359]&start={start}&max_results={max_results}&sortBy=submittedDate&sortOrder=ascending'

        url = base_url + query

        response = urllib.request.urlopen(url).read()
        feed = feedparser.parse(response)

        for entry in feed.entries:
            article = {
                'title': entry.title,
                'authors': [author.name for author in entry.authors],
                'published': entry.published,
                'summary': entry.summary,
                'arxiv_url': entry.link
            }
            