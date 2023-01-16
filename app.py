from flask import Flask, render_template, request, redirect
from flask_cors import CORS

from dates import sandwich_dates_to_poll
from dbsetup import create_connection, update_item

app = Flask(__name__)
cors= CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

database = "./awz_sqlite.db"
conn = create_connection(database)
c = conn.cursor()

def main():
    global conn, c

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sandwich')
def sandwich():
    return render_template('sandwich.html', options=sandwich_dates_to_poll())

@app.route('/sandwich_results',methods=['POST'])
def sandwich_results():
    if request.method == 'POST':
        for name in sandwich_dates_to_poll():
            update = request.form.get(name.replace(" ","-"))
            if update == "1":
                update_item(c,[name])
        return redirect('/')

if __name__ == '__main__':
    main()
    app.run(debug=True)