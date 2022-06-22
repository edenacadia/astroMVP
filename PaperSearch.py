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
        papers = list(ads.SearchQuery(q=keyword, rows=5, sort="citation_count", fld=['title', "authors", "abs", 'citations', 'reference'])) 
        self.paper = papers[0]
        return self.paper

    def returnPaper(self):
        """
        This function returns the search's paper title, author list, and abstract
        """
        return [self.paper.title, self.paper.authors, self.paper.abstract]


