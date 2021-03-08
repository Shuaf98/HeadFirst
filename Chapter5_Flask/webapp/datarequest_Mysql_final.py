

from flask import Flask, render_template, request, escape

    #In the webapp folder, we have 3 HTML templates: base, entry, results.

from DBCm import UseDatabase

app = Flask(__name__)
    #Assigned the Flask framework to a variable. 
app.config['dbconfig'] = {'host': '127.0.0.1',
                            'user': 'root',
                            'password': 'root',
                            'database': 'datarequestDB'
                            }

def log_request(req: 'flask_request', res: str) -> None:
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """show tables"""
        cursor.execute(_SQL)
        data = cursor.fetchall()
        
       
        _SQL = """insert into log
                 (phrase, letters, ip, browser_sring, results) 
                 values 
                 (%s, %s, %s, %s, %s)"""
          #I mispelled "string" in browser_string, when making the log in sql. Couldn't
            #figure out how to change the log though, so kept mispelling here.
        cursor.execute(_SQL, 
                       (req.form['phrase'], 
                        req.form['letters'], 
                        req.remote_addr, 
                        req.user_agent.browser, 
                        res, ))
               
def search4letters(phrase:str, letters:str='aeiou') -> set:
    vowels = set('aeiou')
    return set(letters).intersection(set(phrase))


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
    #Display the contents of the log file as a HTML table.
    with  UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_sring, results from log"""
        
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', 
                           the_title = 'View Log',
                           the_row_titles=titles,
                           the_data=contents)
                           


if __name__ == '__main__':
    #This is important if we were to run this on the web, as opposed to a local host
    app.run(debug=True)
    #open with
    #C:\Users\sfrie\Python\.HeadFirst_python\Chapter5_Flask\webapp>py datarequest_Mysql_final.py
    
    #debugger allows us to make changes without doing CTRL C everytime.






