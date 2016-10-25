from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
  recipes = ['Starter', 'Meal', 'Dessert']
  return render_template('index.html', recipes=recipes), 200

@app.route('/signup/', methods=['GET','POST'])
def signup():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return render_template('index.html', name=name, email=email)
  else:
    return render_template('signup.html')

@app.route('/test-image/')
def test():
  start = '<h2>Pasta</h2><img src="'
  url = url_for('static', filename='img/caesar.jpg')
  end = '">'
  return  start+url+end, 200

@app.route('/starter/')
def starter():
  starter = {'Chicken caesar salad': 'img/caesar.jpg',
             'French onion soup': 'img/caesar.jpg',
             'Halloumi wrap': 'img/caesar.jpg', 
             'Guacamole': 'img/caesar.jpg'
  }
  return render_template('starter.html', starter=starter)

@app.route('/meal/')
def meal():
  meal = ['Quiche lorraine', 'Fish casserole', 'Sweet potato delight', 'Buckwheat pancakes']
  return render_template('meal.html', meal=meal)

@app.route('/dessert/')
def dessert():
  dessert = ['Crepes', 'American pancakes', 'Yogurt cake', 'Sunday caramel']
  return render_template('dessert.html', dessert=dessert)

@app.errorhandler(404)
def page_not_found(error):
  return "We couldn't answer you request. Please try again later or this page might not exist.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
