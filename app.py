from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'London, United Kingdom',
    'salary': '£30,000'
  },
  {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'San Francisco, United States',
    'salary': '$120,000'
  },
  {
    'id': 3,
    'title': 'Backend Engineer',
    'location': 'Delhi, India',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Data Scientist',
    'location': 'New York, United States',
    
  }
  
]



@app.route('/')
def index():
  return render_template('home.html', jobs=Jobs)

@app.route('/api/jobs')
def list_all_jobs():
  return jsonify(Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)