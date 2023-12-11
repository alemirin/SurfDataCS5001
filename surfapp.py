from flask import Flask, render_template
from buoydatareader import *

app = Flask(__name__)

ocean_data = Waves('buoydata.txt')
wave_data = ocean_data.get_wave_heights()
period_data = ocean_data.get_wave_periods()
direction_data = ocean_data.get_wave_directions()

wind_data = Winds('winddata.txt')
wind_speed = wind_data.get_wind_speed()
wind_gusts = wind_data.get_gusts()
wind_direction = wind_data.get_wind_direction()



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',
                           wave_data=wave_data,
                           period_data=period_data,
                           direction_data=direction_data,
                           wind_speed=wind_speed,
                           wind_gusts=wind_gusts,
                           wind_direction=wind_direction)




if __name__ == '__main__':
    app.run(debug=True)
