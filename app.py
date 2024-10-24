from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/',)
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']
    try:
        matches = re.findall(regex_pattern, test_string)
    except re.error:
        matches = ['Invalid Regex']

    return render_template('index.html', test_string=test_string, regex=regex_pattern, matches=matches)

@app.route('/validate_email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        email_regex = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    
        is_valid = re.match(email_regex, email) is not None
        
        return render_template('email_validate.html', email=email, is_valid=is_valid)
    
    return render_template('email_validate.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
