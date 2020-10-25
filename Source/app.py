from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('page1.html')

@app.route('/get_data', methods=["GET","POST"])
def get_data():
    data_dict = {
                 "names":['jhon','shown','rami','nofar','benni'],
                 "towns":['NY','JER','MEX','WAS','HAR'],
                 "hobbies":['BEER','BARS','BEACH','SKI','ROCKETS']
                 }
    return jsonify(data=data_dict)
if __name__ == "__main__":
    app.run(port="5000")