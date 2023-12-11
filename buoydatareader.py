"""
Final Project: Surf App
Student: Alejandro Miranda
Class: CS5001 Fall 2023
"""
from urllib.request import urlopen


class Waves:
    def __init__(self):
        """
        Initializing the class automatically routes to the webpage for the Arecibo NOAA buoy data and pulls
        the information from the webpage text relevant to wave height, wave period and direction.

        Args:
            None.
        Returns:
            None, but assigns the values from the webpage to variables within the Waves class.
        """

        data = urlopen('https://www.ndbc.noaa.gov/data/realtime2/41121.txt')

        next(data)
        line_string2 = str(data.readline())
        if '#yr' in line_string2:
            units_list = line_string2.split()
            self.height_units = units_list[8]
            self.period_units = units_list[9]
            self.direction_units = 'degrees'
        line_string3 = str(data.readline())
        data_list = line_string3.split()
        self.swell_height = float(data_list[8])
        self.swell_period = float(data_list[9])
        self.swell_direction = int(data_list[11])

        data.close()

    def __str__(self):
        conditions = [
                'swell height: ' + str(self.swell_height) + ' ' + self.height_units,
                'swell period: ' + str(self.swell_period) + ' ' + self.period_units,
                'swell direction: ' + self.swell_direction_general]
        for item in conditions:
            print(str(item))
        return 'Data list: ' + str(conditions)

    def get_wave_heights(self):
        """
        Returns the wave height in meters.

        Args:
            None.
        Returns:
            self.swell_height (float): Swell height in meters
        """
        return self.swell_height

    def get_wave_periods(self):
        """
        Returns the wave period in seconds.

        Args:
            None.
        Returns:
            self.swell_period (float): Swell period in seconds.
        """
        return self.swell_period

    def get_wave_directions(self):
        """
        Returns the direction the waves are coming from in degrees. 0 degrees is North, increasing
        clockwise.

        Args:
            None.
        Returns:
            self.swell_height (int): Swell direction in degrees.
        """
        return self.swell_direction


class Winds:
    def __init__(self):
        """
        Initializing the class automatically routes to the webpage for the Arecibo NOAA buoy data and pulls
        the information from the webpage text relevant to wind speed, wind gust speed and direction.
        NOTE: The buoy seems to not be collecting wind data at the moment, unfortunately. Which is why within the
        url you can see these fields are marked with "MM". In this case, the value is set to the string
        "Missing data from National Data Buoy Center" which is displayed on the webpage html.

        Args:
            None.
        Returns:
            None, but assigns the values from the webpage to variables within the Waves class.
        """

        data = urlopen('https://www.ndbc.noaa.gov/data/realtime2/41121.txt')

        next(data)
        line_string2 = str(data.readline())
        if '#yr' in line_string2:
            units_list = line_string2.split()
            self.wind_speed_units = units_list[6]
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
            self.wind_direction = int(data_list[5])
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
        """
        If wind data is found online, it returns a string with the wind speed and units. Else,
        it returns the string "Missing data from National Data Buoy Center." to display on the webpage.

        Args:
            None.
        Returns:
            self.wind_speed (string): with either the units if a value is found or a message to the user if not.
        """

        if isinstance(self.wind_speed, float):
            return str(self.wind_speed) + f'{self.wind_speed_units}'
        else:
            return self.wind_speed

    def get_gusts(self):
        """
        If wind data is found online, it returns a string with the wind gust speed and units. Else,
        it returns the string "Missing data from National Data Buoy Center." to display on the webpage.

        Args:
            None.
        Returns:
            self.gusts (string): with either the units if a value is found or a message to the user if not.
        """

        if isinstance(self.gusts, float):
            return str(self.gusts) + f'{self.gust_units}'
        else:
            return self.gusts

    def get_wind_direction(self):
        """
        If wind data is found online, it returns a string with the wind direction in degrees. Else,
        it returns the string "Missing data from National Data Buoy Center." to display on the webpage.

        Args:
            None.
        Returns:
            self.wind_direction (string): with either the units if a value is found or a message to the user if not.
        """

        if isinstance(self.wind_direction, int):
            return str(self.wind_direction) + f'{self.direction_units}'
        else:
            return self.wind_direction
