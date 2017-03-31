from flask import Flask, render_template, redirect, url_for
from emmys_data import EMMYS
app = Flask(__name__)

app.config['SECRET_KEY'] = 'abcd?efgh#-string'

def get_ids_and_shows(source):
    ids_and_shows = []
    for row in source:
        id = row["ID"]
        show = row["Show"]
        ids_and_shows.append([id, show])
    return ids_and_shows

def get_showdata(source, id):
    for row in source:
        if id == str( row["ID"] ):
            show == row["Show"]
            network = row["Network"]
            category = row["Category"]
            id = str(id)
    return id, show, network, category


@app.route('/')
@app.route('/index/')
def index():
    ids_and_shows = get_ids_and_shows(EMMYS)
    return render_template('index.html', pairs=ids_and_shows)


@app.route('/detail/<id>')

def detail(id):
    id, show, network, cateogry = get_showdata(EMMYS,id)
    return render_template('detail.html', show=show, network=network, category=category )

if __name__ == '__main__':
    app.run(debug=True)
