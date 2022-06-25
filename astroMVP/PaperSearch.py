#### Created 22 06 2022
## This file should be where all ADS functions are stored
import ads
import json

class PaperSearch(object):
    """
    Class encapsulates paper search queries and returns. 
    """

    def __init__(self, keyword):
        """
        Initializes a keyword search in research paper abstracts based on the input by user.

        Parameters
        ----------
        keyword : str
                Keyword input by the user.
    
        token : str
                ADS provided token for searching (note: not required for users to input).

        """

        # saving input
        self.keyword = 'abs:'+keyword
        ads.config.token = 'otQVJT3lALRZhXC4T7sRFrIF3HTtMf4xOlQ3SDpc'
        #this a token from a fake ads account I made with a temporary email. Should need to refresh token, but if necessary... 
        #LOGIN -- 
        #email: beyebi6100@syswift.com
        #password: luv2code 
        self.keywordSearch(self.keyword)

    def keywordSearch(self, keyword):
        """
        Searches for the keyword in abstracts of research papers and returns the first paper with the highest citation count.
        
        Parameters
        ----------
        keyword : str
                Keyword input by user.

        Returns
        -------
        paper : str
                An ADS provided bibcode for the top cited paper found with keyword input.
        """
        self.keyword=keyword
        papers = list(ads.SearchQuery(q=keyword, sort="citation_count",  fl=['id', 'bibcode', 'title', 'citation_count', 'author', 'abstract', 'citation']))


        if len(papers) > 0:
            self.paper = papers[0].bibcode
        else:
            self.paper = None
        return self.paper

    def returnPaper(self):
       """
       Returns the search's paper title, first author, and abstract.
       
       Parameters
       ----------
       keyword : str
            Keyword input by user.
        
       Returns
       -------
       title : str
            Title of research paper with highest citation count.
       author : str
            First author of research paper with highest citation count.
       abstract : str
            Abstract of research paper with highest citation count.
        """
       paper = list(ads.SearchQuery(bibcode=self.paper, fl=['title', 'first_author', 'abstract','links_data']))[0]
       urls = [] #takes the link_data that's given and spits out just the url
       for i in paper.links_data:
            urls.append(json.loads(i)["url"]) 
        
       import requests

       return [paper.title, paper.first_author, paper.abstract,urls]

    def returnCitation(self, n=5):
        """
        Returns the first *n* papers that cite the initial paper, ordered by citation count.

        Parameters
        ---------- 
        n : int
                Number of articles that are returned (default is 5).

        Returns
        -------
        list : list
                n nested lists of citation information of articles.
        list[n, 0] : str
                nth article's title.
        list[n, 1] : str
                nth article's first author.
        """
        paper = list(ads.SearchQuery(bibcode=self.paper, fl=['title', 'first_author', 'abstract', 'citation']))[0]

        if not paper.citation:
            print("No citations for this article")
            return [None]*n

        cite_bibcodes=paper.citation
        cite_articles=[list(ads.SearchQuery(bibcode=bib, fl=['title','first_author', 'citation_count']))[0] for bib in cite_bibcodes]
        cite_sorted=sorted(cite_articles, key=lambda x: x.citation_count, reverse=True)
        cite_cut=cite_sorted[:n]
        return [[article.title, article.first_author] for article in cite_cut]

    def returnReference(self, n=5):
        """
        Returns the first n papers that the initial paper references, ordered by citation count.

        Parameters
        ----------
        n : int
                Number of articles to return (default is 5).

        Returns
        -------
        list : list
                n nested lists of citation information of articles.
        list[n, 0] : str
                nth article's title.
        list[n, 1] : str
                nth article's first author.

        """
        paper = list(ads.SearchQuery(bibcode=self.paper, fl=['title', 'author', 'abstract', 'reference']))[0]

        if not paper.reference:
            print("No reference for this article")
            return [None]*n

        ref_bibcodes=paper.reference[:n]
        ref_articles=[list(ads.SearchQuery(bibcode=bib, fl=['title','first_author', 'citation_count']))[0] for bib in ref_bibcodes]
        ref_sorted=sorted(ref_articles, key=lambda x: x.citation_count, reverse=True)
        ref_cut=ref_sorted[:n]
        return [[article.title, article.first_author] for article in ref_cut]


# search = PaperSearch('supernova').returnPaper()

# print (search)