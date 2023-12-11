from flask import Flask, render_template
from buoydatareader import *

app = Flask(__name__)

ocean_data = Waves()
wave_data = ocean_data.get_wave_heights()
period_data = ocean_data.get_wave_periods()
wave_direction = ocean_data.get_wave_directions()

wind_data = Winds()
wind_speed = wind_data.get_wind_speed()
wind_gusts = wind_data.get_gusts()
wind_direction = wind_data.get_wind_direction()


@app.route("/")
@app.route("/home")
@app.route("/arecibo")
def home():
    return render_template('home.html',
                           wave_data=wave_data,
                           period_data=period_data,
                           wave_direction=wave_direction,
                           wind_speed=wind_speed,
                           wind_gusts=wind_gusts,
                           wind_direction=wind_direction)


if __name__ == '__main__':
    app.run(debug=True)
