from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
  recipes = ['Starter', 'Meal', 'Dessert']
  return render_template('index.html', recipes=recipes), 200

@app.route('/starter/')
def starter():
  starter = ['Chicken ceasar salad', 'French onion soup', 'Halloumi wrap', 'Guacamole']
  return render_template('starter.html')

@app.route('/meal/')
def meal():
  return render_template('meal.html')

@app.route('/dessert/')
def dessert():
  return render_template('dessert.html')

@app.errorhandler(404)
def page_not_found(error):
  return "We couldn't answer you request. Please try again later or this page might not exist.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
