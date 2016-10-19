from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html'), 200

@app.route('/#starter')
def starters():
  recipes = ['Mozzarella&Tomato salad', 'Chicken&Avocado wrap', 'French onion soup', 'Chicken Caesar salad']
  return render_templates('starter.html', recipes=recipes)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
