from flask import Flask, render_template
from emmys_data import EMMYS
app = Flask(__name__)

def get_shows(source):
    shows = []
    for row in source:
        show = row["Show"]
        shows.append([show])
    return shows

def get_showdata(source, show):
    for row in source:
        if id == str( row["ID"] ):
            show == row["Show"]
            network = row["Network"]
            category = row["Category"]
    return id, show, network, category


@app.route('/')
@app.route('/index/')
def index():
    shows = get_shows(EMMYS)
    return render_template('index.html', id=id)

@app.route('/index/<show>')
def detail(show):
    # the URL will have underscores in place of spaces - fix that
    fixed_title = show.replace("_", " ")
    # get variables for the book detail page: pass title with spaces restored
    # to the function that will find that book's record
    show, network, category = get_showdata(EMMYS, fixed_title)
    # pass the data for the selected book to the template
    return render_template('detail.html', id=id, show=show, network=network,
    category=category)

if __name__ == '__main__':
    app.run(debug=True)
