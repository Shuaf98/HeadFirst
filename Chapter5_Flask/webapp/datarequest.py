from flask import Flask, render_template, request, escape
    #In the webapp folder, we have 3 HTML templates: base, entry, results.


def log_request(req: 'flask_request', res: str) -> None:
    with open('datareq.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
    

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
    log_request(request, results)
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

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('datareq.log') as log:
       for line in log:
           contents.append([])
           for item in line.split('|'):
               contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', 
                           the_title = 'View Log',
                           the_row_titles=titles,
                           the_data=contents)
                           


if __name__ == '__main__':
    #This is important if we were to run this on the web, as opposed to a local host
    app.run(debug=True)
        #run with py vsearch4web.py.
        #debugger allows us to make changes without doing CTRL C everytime.