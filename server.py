from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:indicated_route>')
def html_page(indicated_route):
    return render_template(indicated_route)

def data_collecting(data):
	with open("database.txt", "a") as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		database.write(f'\n{email}, {subject}, {message}')

def data_collecting_csv(data):
	with open("database.csv", "a", newline="") as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_w = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)		
		csv_w.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	data_collecting_csv(data)
    	return redirect('thanks.html')
    else:
    	return 'Uuups Sorry'