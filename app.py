import mediawiki
from flask import Flask, render_template, request
from wikipedia_search  import wiki_get_summary_img
import db_funcs as db
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_keyword',methods=['GET','POST'])
def search_keyword():
    if request.method == 'POST':
        keyword = request.form['keyword']
        wiki_dict = db.search_db(keyword)
        print(wiki_dict)
        if not wiki_dict:
            try:
                wiki_dict=wiki_get_summary_img(keyword)
                print(wiki_dict,"wiki_dict after getting from wikipedia")
            except mediawiki.DisambiguationError as e:
                print(e)
                return render_template('search_form.html', title = e, summary= '', img_link= '')
            except mediawiki.PageError as e:
                print(e)
                return render_template('search_form.html', title = e, summary= '', img_link= '')
            db.insert_row(wiki_dict["title"],wiki_dict["summary"],wiki_dict["img_link"])



    return render_template('search_form.html', title = wiki_dict["title"], summary= wiki_dict["summary"], img_link= wiki_dict["img_link"])


if __name__ == '__main__':
    app.run()