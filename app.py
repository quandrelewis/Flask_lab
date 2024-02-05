from flask import Flask, render_template, request           # import flask framework
app = Flask(__name__)             # create an app instance

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)  

if __name__ == "__main__":        # when running python app.py
    app.run(debug=True)                     # run the flask app