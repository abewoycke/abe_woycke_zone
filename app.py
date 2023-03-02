from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from dates import sandwich_dates_to_poll, taustin_dnd_dates_to_poll, comm_601_dates_to_poll
from socket import gethostname
from poll_response import poll_response
import re
from datetime import datetime as dt
from dbsetup import db_setup
from datetime import timedelta

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db_setup()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sandwich')
def sandwich():
    return render_template('sandwich.html', options=sandwich_dates_to_poll())

@app.route('/taustin_dnd')
def taustin_dnd():
    return render_template('taustin_dnd.html', options=taustin_dnd_dates_to_poll())

@app.route('/comm_601')
def comm_601():
    return render_template('comm_601.html', options=comm_601_dates_to_poll())

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/submit_poll',methods=['POST'])
def submit_poll():
    if request.method == 'POST':
        for key in request.form.keys():
            # filter by keys that are poll options (containing "day")
            day_key_match = re.search(r".*day.*", key)
            if day_key_match:
                response = poll_response(group_name=request.form['group_name'],
                                         submitted_name=request.form['name'].lower().replace(" ",""),
                                         month = re.compile('(\d\d)').findall(key)[0],
                                         year = (dt.today() + timedelta(days=30)).year,
                                         poll_option=key,
                                         response=request.form[key])
                response.record_votes()
    return redirect('/thanks')

# html in deb
# @app.comm_601_results():
    # return render_template('comm_601_results.html')

if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run(debug=True)