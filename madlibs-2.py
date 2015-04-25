from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    hel_o = render_template("hello.html")
    print hel_o
    return hel_o

@app.route('/game')
def show_game_form():

  player = request.args.get("person")
  print player
  answer = request.args.get("playPreference")
  print answer

  if answer == "Yes":
    gam_e = render_template("game.html")
    print gam_e
    return gam_e
        
  else:
    goo_d = render_template("goodbye.html")
    print goo_d
    return goo_d


@app.route('/greet')
def greet_person():
    player = request.args.get("person")
  

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    
    compl = render_template("compliment.html", person=player, compliment=compliment)
    print compl
    return compl
#GLOBAL_COMPL = compl

@app.route('/madlib')
def show_madlib():
  color=request.args.get("userInput1")
  print color
  noun= request.args.get("userInput2")
  adjective=request.args.get("userInput3")
  player = request.args.get("person")

  mad_l=render_template("madlibs.html", color=color, noun=noun, person=player, adjective=adjective)
  print mad_l
  return mad_l

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
