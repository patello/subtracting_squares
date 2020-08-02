from flask import Flask, Markup, render_template, redirect
from minmax import Game

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/Square/34')

@app.route('/<string:fun>/<int:end>')
def game_res(end,fun):
    game=Game(span=[0,end],sub_fun=fun)
    result=game.calculate()
    table_data = ""
    for x in range(1,end+1):
        if result[x] == True:
            cssclass = "reswin"
        else:
            cssclass = "resloss"
        if (x-1)%10 == 0:
            table_data += "<tr>"
        table_data += "<td class=\""+cssclass+"\">"+str(x)+"</td>"
        if (x-1)%10 == 9 or x == end+1:
            table_data += "</tr>"
    return render_template('result.html',table_data=Markup(table_data),end=end,selected=["selected" if fun=="Square" else "","selected" if fun=="Odd" else "","selected" if fun=="Even" else "","selected" if fun=="Logarithm" else ""])