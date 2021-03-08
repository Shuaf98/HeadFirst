from flask import Flask, render_template, request, redirect

def search4letters(phrase:str, letters:str='aeiou') -> set:
    vowels = set('aeiou')
    return set(letters).intersection(set(phrase))

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/search4', methods=['Post'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results"
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
            the_phrase= phrase,
            the_letters= letters,
            the_title = title,
            the_results = results)
@app.route('/entry')
def entry_page() -> 'html ':
    return render_template('entry.html', the_title = 'Welcometo search4letters on the web!')

app.run(debug=True)
    #run with py vsearch4web.py.
    #debugger allows us to make changes without doing CTRL C everytime.