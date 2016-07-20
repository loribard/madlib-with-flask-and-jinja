
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/compliment')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    return render_template("compliment.html",
                           person=player,
                           )

@app.route('/game')
def show_madlib_form():
    response = request.args.get("response")
    if response == "yes":

        return render_template("game.html")
    else:
        return "Goodbye party pooper"

@app.route("/madlib")
def show_madlib():
    color_choice = request.args.get("color")
    noun_choice = request.args.get("noun")
    person_choice = request.args.get("person")
    adjective_choice = request.args.get("adjective")

    return render_template("madlib.html", color=color_choice,
     noun=noun_choice, person=person_choice, adjective=adjective_choice)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
