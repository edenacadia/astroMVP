#### Created 22 06 2022
## This file should be where all ADS functions are stored
import ads


class PaperSearch(object):

    def __init__(self, keyword, token):
        # saving input
        ads.config.token = token
        self.keyword = keyword
        self.keywordSeach(self.keyword)

    def keywordSeach(self, keyword):
        """
        Searches for the keyword and returns the first paper that matched with the highest citation count
        """
        self.keyword = keyword
        papers = list(ads.SearchQuery(q=keyword, rows=5, sort="citation_count", fld=['title', "author", "abs", 'citation', 'reference'])) 
        self.paper = papers[0]
        return self.paper

    def returnPaper(self):
        """
        This function returns the search's paper title, author list, and abstract
        """
        return [self.paper.title, self.paper.authors, self.paper.abstract]

    def returnCitation(self, n=5):
        """
        This function returns the first five citations and returns title and author for each citations
        """
        cite_bibcodes=self.paper.citations[:n]
        cite_articles=[list(ads.SearchQuery(bibcode=bib, fl=['title','author']))[0] for bib in cite_bibcodes]

        return [[article.title, article.author] for article in cite_articles]
