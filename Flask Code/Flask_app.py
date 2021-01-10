from flask import Flask
#imporing the flask repository
app = Flask(__name__)
#configuring a variable named the same as my file name
@app.route("/", methods=["GET"])
#defining the app route or url
def hello():
    return "Hello from Flask!"
#defining function
app.run()
#leaves the app running until i quit it
