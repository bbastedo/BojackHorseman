# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__, static_url_path='/static')


# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stock")
def stock():
    return render_template("netflix_stock.html")

@app.route("/ratings")
def ratings():
    return render_template("ratings.html")

@app.route("/Season1")
def s1():
    return render_template("Season_1.html")

@app.route("/Season2")
def s2():
    return render_template("Season_2.html")

@app.route("/Season3")
def s3():
    return render_template("Season_3.html")

@app.route("/Season4")
def s4():
    return render_template("Season_4.html")

@app.route("/Season5")
def s5():
    return render_template("Season_5.html")

@app.route("/S1")
def stock1():
    return render_template("s1.html")    

@app.route("/S2")
def stock2():
    return render_template("s2.html")    

@app.route("/S3")
def stock3():
    return render_template("s3.html")    

@app.route("/S4")
def stock4():
    return render_template("s4.html")    

@app.route("/S5")
def stock5():
    return render_template("s5.html")    

if __name__ == "__main__":
    app.run(debug=True)
