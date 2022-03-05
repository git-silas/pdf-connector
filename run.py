from flask import Flask, render_template

from forms import FileForm

app = Flask(__name__)


@app.route('/')
def index():

    file_form = FileForm()

    return render_template('index.html', file_form=file_form)


if __name__ == '__main__':
    app.run(debug=True)