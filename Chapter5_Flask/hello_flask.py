from flask import Flask, render_template

def search4letters(phrase:str, letters:str='aeiou') -> set:
    vowels = set('aeiou')
    return set(letters).intersection(set(phrase))

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('the life the universe, and everything', 'eiru,!'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template ('entry.html', the_title = 'Welcome to search4letters on the web')

app.run()
    #this lets us edit and refresh the url without having to CTRL C

