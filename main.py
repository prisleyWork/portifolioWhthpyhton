from flask import Flask, render_template

app = Flask(__name__)

# route ----> (o link/algo)
# função --> o que quero mostrar 

@app.route("/")
def homepage():
    return render_template("homepage.html")

# colocando o site no ar
if __name__ == "__main__": 
    app.run(debug=True)
