'''
Final Project: Surf App
Student: Alejandro Miranda
Class: CS5001 Fall 2023
'''



class Waves:
    def __init__(self, file):

        filename = file

        data = open(filename, "r")

        next(data)
        line_string2 = str(data.readline())
        if '#yr' in line_string2:
            units_list = line_string2.split()
            self.height_units = units_list[6]
            self.period_units = units_list[7]
            self.direction_units = 'degrees'
        line_string3 = str(data.readline())
        data_list = line_string3.split()
        self.swell_height = float(data_list[6])
        self.swell_period = float(data_list[7])
        self.swell_direction_general = data_list[10]
        self.swell_direction_specific = data_list[-1]
        self.wind_swell_height = float(data_list[8])
        self.wind_swell_period = float(data_list[9])
        self.wind_swell_direction = data_list[11]
        self.overall_wave_height = float(data_list[5])

        data.close()

    def __str__(self):
        conditions = ['wind swell height: ' + str(self.wind_swell_height) + ' ' + self.height_units,
                'wind swell period: ' + str(self.wind_swell_period) + ' ' + self.period_units,
                'wind swell direction: ' + self.wind_swell_direction,
                'swell height: ' + str(self.swell_height) + ' ' + self.height_units,
                'swell period: ' + str(self.swell_period) + ' ' + self.period_units,
                'swell direction: ' + self.swell_direction_general,
                'overall wave height: ' + str(self.overall_wave_height) + ' ' + self.height_units,
                'average wave direction: ' + str(self.swell_direction_specific) + ' ' + self.direction_units]
        for item in conditions:
            print(str(item))
        return 'Data list: ' + str(conditions)


    def get_wave_heights(self):
        return [self.wind_swell_height,
                self.swell_height,
                self.overall_wave_height]

    def get_wave_periods(self):
        return [self.wind_swell_period,
                self.swell_period]

    def get_wave_directions(self):
        return [self.wind_swell_direction,
                self.swell_direction_general,
                self.swell_direction_specific]

class Winds:
    def __init__(self, file):

        filename = file

        data = open(filename, "r")

        next(data)
        line_string2 = str(data.readline())
        if '#yr' in line_string2:
            units_list = line_string2.split()
            self.windspeed_units = units_list[6]
            self.gust_units = units_list[7]
            self.direction_units = 'degrees'
        line_string3 = str(data.readline())
        data_list = line_string3.split()
        if data_list[6] != "MM":
            self.wind_speed = float(data_list[6])
        else:
            self.wind_speed = 'Missing data from National Data Buoy Center.'
        if data_list[7] != "MM":
            self.gusts = float(data_list[7])
        else:
            self.gusts = 'Missing data from National Data Buoy Center.'
        if data_list[5] != "MM":
            self.wind_direction = data_list[5]
        else:
            self.wind_direction = 'Missing data from National Data Buoy Center.'


        data.close()

    def __str__(self):
        if isinstance(self.wind_speed, float) and isinstance(self.gusts, float):
            conditions = ['wind speed: ' + str(self.wind_speed) + ' ' + self.windspeed_units,
                'wind gusts: ' + str(self.gusts) + ' ' + self.period_units,
                'wind direction: ' + self.wind_direction]
        elif isinstance(self.wind_speed, float) and isinstance(self.gusts, str):
            conditions = ['wind speed: ' + str(self.wind_speed) + ' ' + self.windspeed_units,
                          'wind gusts: ' + str(self.gusts),
                          'wind direction: ' + self.wind_direction]
        elif isinstance(self.wind_speed, str) and isinstance(self.gusts, float):
            conditions = ['wind speed: ' + str(self.wind_speed),
                          'wind gusts: ' + str(self.gusts) + ' ' + self.period_units,
                          'wind direction: ' + self.wind_direction]
        else:
            conditions = ['wind speed: ' + str(self.wind_speed),
                          'wind gusts: ' + str(self.gusts),
                          'wind direction: ' + self.wind_direction]
        for item in conditions:
            print(str(item))
        return 'Data list: ' + str(conditions)


    def get_wind_speed(self):
        if isinstance(self.wind_speed, float):
            return str(self.wind_speed) + f'{self.windspeed_units}'
        else:
            return self.wind_speed

    def get_gusts(self):
        if isinstance(self.gusts, float):
            return str(self.gusts) + f'{self.gust_units}'
        else:
            return self.gusts

    def get_wind_direction(self):
        return self.wind_direction