import mediawiki
from mediawiki import MediaWiki
wikipedia = MediaWiki()
wiki_dict = {"title":'',"summary":'', "img_link":''}
def wiki_get_summary_img(keyword):
        wiki_dict = {"title": '', "summary": '', "img_link": ''}
        try:
            p = wikipedia.page(keyword)
            wiki_dict["title"] = p.title
            wiki_dict["summary"] = p.summary
            if p.images:
                wiki_dict["img_link"] = p.images[0]
            else:
                wiki_dict["img_link"] = "No images for this keyword"

        except mediawiki.DisambiguationError as e:
            #wiki_dict = None
            raise e

        except mediawiki.PageError as e:
            #wiki_dict = None
            raise e
            #wiki_dict["title"] = e

        return None

#def keyword_db_search(keyword):








