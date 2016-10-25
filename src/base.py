from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html'), 200

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

@app.route('/starter/')
def starter():
  starter = {'Chicken caesar salad': 'img/salad.png',
             'French onion soup': 'img/salad.png',
             'Halloumi wrap': 'img/salad.png', 
             'Guacamole': 'img/salad.png'
  }
  return render_template('starter.html', starter=starter)

@app.route('/meal/')
def meal():
  meal = {'Quiche lorraine': 'img/caesar.jpg', 
          'Fish casserole': 'img/caesar.jpg', 
          'Sweet potato delight': 'img/caesar.jpg', 
          'Buckwheat pancakes': 'img/caesar.jpg'
  }
  return render_template('meal.html', meal=meal)

@app.route('/dessert/')
def dessert():
  dessert = { 'Crepes': 'img/caesar.jpg', 
              'American pancakes': 'img/caesar.jpg', 
              'Yogurt cake': 'img/caesar.jpg', 
              'Sunday caramel': 'img/caesar.jpg'
  }
  return render_template('dessert.html', dessert=dessert)

@app.errorhandler(404)
def page_not_found(error):
  return "We couldn't answer you request. Please try again later or this page might not exist.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
