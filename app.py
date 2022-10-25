
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
        if not db.search_db(keyword):
            wiki_dict=wiki_get_summary_img(keyword)
            db.insert_row(wiki_dict["title"],wiki_dict["summary"],wiki_dict["img_link"])
        else:
            print(db.search_db(keyword))


    return render_template('search_form.html', title = wiki_dict["title"], summary= wiki_dict["summary"], img_link= wiki_dict["img_link"])


if __name__ == '__main__':
    app.run()