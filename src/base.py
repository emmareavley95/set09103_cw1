from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html'), 200

def upload():
    if request.method == 'POST':
      f = request.files['datafile'],
      f.save('static/uploads/recipe.png')
      return "File uploaded"
    else:
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
  starter = {'Chicken caesar salad': 'img/starter/caesar.png',
             'Halloumi wrap': 'img/starter/halloumi.png',
             'French onion soup': 'img/starter/frenchonionsoup.png',
             'Guacamole': 'img/starter/guacamole.png'
  }
  return render_template('starter.html', starter=starter)

@app.route('/meal/')
def meal():
  meal = {'Quiche lorraine': 'img/meal/quiche.png', 
          'Fish casserole': 'img/meal/fishcasserole.png', 
          'Sweet potato delight': 'img/meal/sweetpotato.png', 
          'Buckwheat pancakes': 'img/meal/galettes.png'
  }
  return render_template('meal.html', meal=meal)

@app.route('/dessert/')
def dessert():
  dessert = { 'Crepes': 'img/dessert/crepes.png', 
              'American pancakes': 'img/dessert/pancakes.png', 
              'Yogurt cake': 'img/dessert/cake.png', 
              'Sunday caramel': 'img/dessert/sunday.png'
  }
  return render_template('dessert.html', dessert=dessert)

@app.errorhandler(404)
def page_not_found(error):
  return "We couldn't answer you request. Please try again later or this page might not exist.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
