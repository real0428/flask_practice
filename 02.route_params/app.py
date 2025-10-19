from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/news_list')
def news():
  return render_template('news/news_list.html')

@app.route('/news_detail')
def news_detail():
  news_id = request.args.get('news_id') # query parameter
  return render_template('news/news_detail.html', news_id=news_id)

@app.route('/article_list')
def articles():
  return render_template('article/article_list.html')

@app.route('/article_detail/<int:article_id>') # route parameter
def article_detail(article_id):
  return render_template('article/article_detail.html', article_id=article_id)

@app.route('/course_list')
def courses():
  return render_template('course/course_list.html')

@app.route('/course_detail/<int:course_id>')
def course_detail(course_id):
  return render_template('course/course_detail.html', course_id=course_id, title="課程詳情")

if __name__ == '__main__':
  app.run(debug=True)
