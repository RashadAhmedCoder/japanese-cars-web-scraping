from flask import Flask, render_template
from main import honda_all_msrps, honda_all_names, toyota_all_msrps, toyota_all_names, toyota_all_years

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', honda_all_names = honda_all_names, honda_all_msrps = honda_all_msrps, toyota_all_msrps = toyota_all_msrps, toyota_all_names = toyota_all_names, toyota_all_years = toyota_all_years)

if __name__ == '__main__':
    app.run(debug=False)