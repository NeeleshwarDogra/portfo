from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/<string:name>')
def name_page(name='index.html'):
    return render_template(name)


def write_to_database(data):
    with open('database.csv', 'a', newline='' ) as datafile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file_csv = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_csv.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_database(data)
        return redirect('/thanks.html')
    else:
        return 'not working'



# @app.route('/index.html')
# def home_page():
#     return render_template('index.html')
#
#
# @app.route('/works.html')
# def work_page():
#     return render_template('works.html')
#
#
# @app.route('/about.html')
# def about_page():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')
# def contact_page():
#     return render_template('contact.html')
#
#
# @app.route('/components.html')
# def components_page():
#     return render_template('/components.html')
