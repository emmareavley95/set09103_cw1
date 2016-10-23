from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def root():
  recipes = ['Starter', 'Meal', 'Dessert']
  return render_template('index.html', recipes=recipes), 200

@app.route('/test-image/')
def test():
  start = '<h2>Pasta</h2><img src="'
  url = url_for('static', filename='img/pasta.jpg')
  end = '">'
  return  start+url+end, 200

@app.route('/starter/')
def starter():
  starter = [dict(salad='Chicken caesar salad', img=url_for('static', filename='img/pasta.jpg')), 
            dict(salad='French onion soup', img=url_for('static', filename='img/pasta.jpg')), 
            dict(salad='Halloumi wrap', img=url_for('static', filename='img/pasta.jpg')), 
            dict(salad='Guacamole', img=url_for('static', filename='img/pasta.jpg'))
  ]
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
