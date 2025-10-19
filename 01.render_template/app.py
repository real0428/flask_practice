from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/news_list')
def news():
  return render_template('news/news_list.html')


if __name__ == '__main__':
  app.run(debug=True)
