from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'Location': 'Mumbai, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'Location': 'Delhi, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'Location': 'Remote',
}]


@app.route("/")
def Index():
  return render_template("index.html", jobs=JOBS)


@app.route("/api/jobs")
def listjobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
