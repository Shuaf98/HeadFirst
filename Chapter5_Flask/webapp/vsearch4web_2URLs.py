from flask import Flask, render_template, request
#In the webapp folder, we have 3 HTML templates: base, entry, results.


def search4letters(phrase:str, letters:str='aeiou') -> set:
    vowels = set('aeiou')
    return set(letters).intersection(set(phrase))

app = Flask(__name__)
    #Assigned the Flask framework to a variable.

@app.route('/search4', methods=['Post'])
    #the route decorator from flask associates a an inputted url web path to a python function.
    #methods=['post'] allows a web browser to send data to the server over HTTP
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

@app.route('/')
@app.route('/entry')
#This app has 2 URL's associated with it.
def entry_page() -> 'html ':
    return render_template('entry.html', the_title = 'Welcometo search4letters on the web!')

if __name__ == '__main__':
    #This is important if we were to run this on the web, as opposed to a local host
    app.run(debug=True)
        #run with py vsearch4web.py.
        #debugger allows us to make changes without doing CTRL C everytime.