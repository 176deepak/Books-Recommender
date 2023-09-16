from src.books_recommender.pipeline.prediction_pipeline import recommender
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        name = request.form['book-name']
        books = recommender(name)
        print(books[1][0])
        return render_template('index.html', book_name=name, data=books)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)