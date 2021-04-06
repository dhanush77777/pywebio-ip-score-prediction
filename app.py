from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *

import pickle
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


def predict():
    bat_team= select('Select the batting team',['Kolkata Knight Riders','Chennai Super Kings','Rajasthan Royals','Mumbai Indians','Kings XI Punjab','Royal Challengers Bangalore','Delhi Daredevils','Sunrisers Hyderabad'])
    if (bat_team == 'Kolkata Knight Riders'):
        bat_team=3
    elif(bat_team == 'Chennai Super Kings'):
        bat_team = 0
    elif(bat_team == 'Rajasthan Royals'):
        bat_team = 5
    elif(bat_team == 'Mumbai Indians'):
         bat_team =4
    elif(bat_team == 'Kings XI Punjab'):
        bat_team = 2
    elif(bat_team == 'Royal Challengers Bangalore'):
        bat_team = 6
    elif(bat_team == 'Delhi Daredevils' ):
        bat_team = 1
    else:
        bat_team = 7
    bowl_team= select('Select the bowling team',['Kolkata Knight Riders','Chennai Super Kings','Rajasthan Royals','Mumbai Indians','Kings XI Punjab','Royal Challengers Bangalore','Delhi Daredevils','Sunrisers Hyderabad'])
    if (bowl_team == 'Kolkata Knight Riders'):
        bowl_team=3
    elif(bowl_team == 'Chennai Super Kings'):
        bowl_team = 0
    elif(bowl_team == 'Rajasthan Royals'):
        bowl_team = 5
    elif(bowl_team == 'Mumbai Indians'):
         bowl_team =4
    elif(bowl_team == 'Kings XI Punjab'):
        bowl_team = 2
    elif(bowl_team == 'Royal Challengers Bangalore'):
        bowl_team = 6
    elif(bowl_team == 'Delhi Daredevils' ):
        bowl_team = 1
    else:
        bowl_team = 7   
     
    runs = input("Enter the runs scored", type=NUMBER)
    wickets= input("Enter the wickets lost", type=NUMBER)
    overs= input("Enter the overs completed", type=FLOAT)
    runs_last_5=input("enter the runs in previous 5 overs",type=NUMBER)
    wickets_last_5=input("enter the wickets lost in previous 5 overs",type=NUMBER)

    prediction = model.predict([[bat_team, bowl_team, runs, wickets,overs, runs_last_5, wickets_last_5]])
    output = prediction[0]

    if output < 0:
        put_text("Sorry You can't sell this Car")

    else:
        put_text('Your predicted score is:',output)

app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])


#if __name__ == '__main__':
    #predict()

app.run(host='localhost',port=5000)

