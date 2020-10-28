from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.DevConfig')
print(app.config['FLASK_ENV'])

@app.route('/')
def index():
    data = "almarcano.us"
    return render_template('index.html', data=data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()