from flask import Flask, render_template, redirect, url_for, request

from todo_app.flask_config import Config

from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/index')
def index():
	todolists = get_items()
	return render_template('index.html', todolists = todolists)


@app.route('/addtodoitem', methods=['POST'])
def addtodoitem():
	add_item(request.form['item_title'])
	todolists = get_items()
	return render_template('index.html', todolists = todolists)

if __name__ == '__main__':
    app.run()
