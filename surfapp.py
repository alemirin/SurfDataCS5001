from flask import Flask, render_template
from buoydatareader import *

app = Flask(__name__)



arecibo_wave_data = Waves('https://www.ndbc.noaa.gov/data/realtime2/41121.txt')
arecibo_wave_conditions = [arecibo_wave_data.get_wave_heights(),
                           arecibo_wave_data.get_wave_periods(),
                           arecibo_wave_data.get_wave_direction()]

arecibo_wind_data = Winds('https://www.ndbc.noaa.gov/data/realtime2/41121.txt')
arecibo_wind_conditions = [arecibo_wind_data.get_wind_speed(),
                           arecibo_wind_data.get_gusts(),
                           arecibo_wind_data.get_wind_direction()]

sanjuan_wave_data = Waves('https://www.ndbc.noaa.gov/data/realtime2/41053.txt')
sanjuan_wave_conditions = [sanjuan_wave_data.get_wave_heights(),
                           sanjuan_wave_data.get_wave_periods(),
                           sanjuan_wave_data.get_wave_direction()]

sanjuan_wind_data = Winds('https://www.ndbc.noaa.gov/data/realtime2/41053.txt')
sanjuan_wind_conditions = [sanjuan_wind_data.get_wind_speed(),
                           sanjuan_wind_data.get_gusts(),
                           sanjuan_wind_data.get_wind_direction()]


@app.route("/")
@app.route("/home")
@app.route("/arecibo")
def home():
    return render_template('home.html',
                           arecibo_wave_conditions=arecibo_wave_conditions,
                           arecibo_wind_conditions=arecibo_wind_conditions)

@app.route("/sanjuan")
def sanjuan():
    return render_template('sanjuan.html',
                           sanjuan_wave_conditions=sanjuan_wave_conditions,
                           sanjuan_wind_conditions=sanjuan_wind_conditions)

if __name__ == '__main__':
    app.run(debug=True)
