from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from dates import three_moi, options
from socket import gethostname
from poll_response import poll_response
import re
from dbsetup import db_setup
from datetime import datetime as dt
from view_poll_results import vpr
from find_year import find_year

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db_setup()

# three months of interest
previous_month, current_month, next_month = three_moi()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote/<crew>')
def vote(crew):
    moi = [current_month,next_month]
    if crew in ['sandwich','comm_601','taustin_dnd']:
        options_current, options_next = options(crew)
    return render_template('vote.html',crew=crew,moi=moi,options=[options_current,options_next])

@app.route('/submit_poll',methods=['POST'])
def submit_poll():
    if request.method == 'POST':
        for key in request.form.keys():
            # filter by keys that are poll options (containing "day")
            day_key_match = re.search(r".*day.*", key)
            if day_key_match:
                response = poll_response(crew=request.form['crew'],
                                         participant=request.form['name'].lower().replace(" ",""),
                                         month = re.compile('(\d\d)').findall(key)[0].strip(),
                                         day = re.compile('(\d\d)').findall(key)[1].strip(),
                                         year = find_year(key),
                                         time_description=re.compile("\d{1,2}/\d{1,2}\s(.+)").findall(key.replace("-"," "))[0].strip(),
                                         response=request.form[key],
                                         submitted_dt=dt.now().strftime("%Y-%m-%d %H:%M:%S"))
                response.insert_responses()
    return redirect('/thanks')

@app.route('/view/<crew>')
def view(crew):
    moi = [current_month,next_month]
    vpr_cur = vpr(crew, dt.strptime(current_month,"%b %Y").month, dt.strptime(current_month,"%b %Y").year)
    html_cur = vpr_cur.vpr_html()
    vpr_next = vpr(crew, dt.strptime(next_month,"%b %Y").month, dt.strptime(current_month,"%b %Y").year)
    html_next = vpr_next.vpr_html()
    return render_template('view.html',crew=crew,moi=moi,html=[html_cur,html_next])

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run(debug=True)