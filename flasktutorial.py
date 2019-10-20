from flask import Flask,render_template
app = Flask(__name__)

pitches = [
    {
        'author' : 'Tyra Hans' ,
        'title' : 'Pitch 1',
        'content' : 'First pitch content',
        'date_posted' : 'April 20,2019'
    },
    {
        'author' : 'Trevor TheTrev' ,
        'title' : 'Pitch 2',
        'content' : 'Second pitch content',
        'date_posted' : 'May 6,2019'
    },
]

@app.route('/')
def home():
    return render_template('index.html', posts = pitches)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)