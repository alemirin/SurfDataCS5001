"""
Final Project: Surf App
Student: Alejandro Miranda
Class: CS5001 Fall 2023
"""
from urllib.request import urlopen


class Waves:
    def __init__(self, url):
        """
        Initializing the class automatically routes to the webpage for the Arecibo NOAA buoy data and pulls
        the information from the webpage text relevant to wave height, wave period and direction.

        Args:
            None.
        Returns:
            None, but assigns the values from the webpage to variables within the Waves class.
        """

        data = urlopen(url)

        next(data)
        line_string2 = str(data.readline())
        if '#yr' in line_string2:
            units_list = line_string2.split()
            self.height_units = units_list[8]
            self.period_units = units_list[9]
            self.direction_units = 'deg'

        wave_conditions_filtered = [0, 0, 0]
        for _ in range(0, 6):
            line_string = str(data.readline())
            data_list = line_string.split()
            wave_conditions_raw = self.collect_recent_wave_values(data_list)
            # Code below checks to see whether a recent value has already been recorded
            # If it hasn't been found and there exists a new value, then assign that value to our
            # filtered wave conditions list.
            if wave_conditions_filtered[0] == 0 and wave_conditions_raw[0] != '':
                wave_conditions_filtered[0] = wave_conditions_raw[0]
            if wave_conditions_filtered[1] == 0 and wave_conditions_raw[1] != '':
                wave_conditions_filtered[1] = wave_conditions_raw[1]
            if wave_conditions_filtered[2] == 0 and wave_conditions_raw[2] != '':
                wave_conditions_filtered[2] = wave_conditions_raw[2]

        if wave_conditions_filtered[0] == 0:
            self.swell_height = 'Missing data from National Data Buoy Center.'
        else:
            self.swell_height = wave_conditions_filtered[0]
        if wave_conditions_filtered[1] == 0:
            self.swell_period = 'Missing data from National Data Buoy Center.'
        else:
            self.swell_period = wave_conditions_filtered[1]
        if wave_conditions_filtered[2] == 0:
            self.swell_direction = 'Missing data from National Data Buoy Center.'
        else:
            self.swell_direction = wave_conditions_filtered[2]

        data.close()

    def __str__(self):
        conditions = [
                'swell height: ' + str(self.swell_height) + ' ' + self.height_units,
                'swell period: ' + str(self.swell_period) + ' ' + self.period_units,
                'swell direction: ' + self.swell_direction_general]
        for item in conditions:
            # uncomment to print items in a readable way
            # print(str(item))
            pass
        return 'Data list: ' + str(conditions)

    def collect_recent_wave_values(self, data_list):
        """
        Function checks the data list to ensure that relevant data is filled in and then returns a list
        with wave data.

        Args:
        data_list (list): List of data pertaining to one line of buoy data.

        Returns:
            list : List with wave height, wave period and wave direction.
        """
        wave_height = ''
        wave_period = ''
        wave_direction = ''
        if data_list[8] != "MM":
            wave_height = data_list[8]
        if data_list[9] != "MM":
            wave_period = data_list[9]
        if data_list[11] != "MM":
            wave_direction = data_list[11]

        return [wave_height, wave_period, wave_direction]

    def get_wave_heights(self):
        """
        Returns the wave height in meters.

        Args:
            None.
        Returns:
            self.swell_height (float): Swell height in meters
        """
        try:
            swell_height = float(self.swell_height)
            return str(swell_height) + ' ' + f'{self.height_units}'
        except ValueError:
            return self.swell_height

    def get_wave_periods(self):
        """
        Returns the wave period in seconds.

        Args:
            None.
        Returns:
            self.swell_period (float): Swell period in seconds.
        """
        try:
            swell_period = float(self.swell_period)
            return str(swell_period) + ' ' + f'{self.period_units}'
        except ValueError:
            return self.swell_period

    def get_wave_direction(self):
        """
        Returns the direction the waves are coming from in degrees. 0 degrees is North, increasing
        clockwise.

        Args:
            None.
        Returns:
            self.swell_height (int): Swell direction in degrees.
        """
        try:
            swell_direction = int(self.swell_direction)
            return str(swell_direction) + f'{self.direction_units}'
        except ValueError:
            return self.swell_direction


class Winds:
    def __init__(self, url):
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

        data = urlopen(url)

        next(data)
        line_string2 = str(data.readline())
        if '#yr' in line_string2:
            units_list = line_string2.split()
            self.wind_speed_units = units_list[6]
            self.gust_units = units_list[7]
            self.direction_units = 'degrees'

        wind_conditions_filtered = [0, 0, 0]
        for _ in range(0, 6):
            line_string = str(data.readline())
            data_list = line_string.split()
            wind_conditions_raw = self.collect_recent_wind_values(data_list)
            # Code below checks to see whether a recent value has already been recorded
            # If it hasn't been found and there exists a new value, then assign that value to our
            # filtered wave conditions list.
            if wind_conditions_filtered[0] == 0 and wind_conditions_raw[0] != '':
                wind_conditions_filtered[0] = wind_conditions_raw[0]
            if wind_conditions_filtered[1] == 0 and wind_conditions_raw[1] != '':
                wind_conditions_filtered[1] = wind_conditions_raw[1]
            if wind_conditions_filtered[2] == 0 and wind_conditions_raw[2] != '':
                wind_conditions_filtered[2] = wind_conditions_raw[2]

        if wind_conditions_filtered[0] == 0:
            self.wind_speed = 'Missing data from National Data Buoy Center.'
        else:
            self.wind_speed = wind_conditions_filtered[0]
        if wind_conditions_filtered[1] == 0:
            self.gusts = 'Missing data from National Data Buoy Center.'
        else:
            self.gusts = wind_conditions_filtered[1]
        if wind_conditions_filtered[2] == 0:
            self.wind_direction = 'Missing data from National Data Buoy Center.'
        else:
            self.wind_direction = wind_conditions_filtered[2]

        data.close()

    def __str__(self):
        if isinstance(self.wind_speed, float) and isinstance(self.gusts, float):
            conditions = ['wind speed: ' + str(self.wind_speed) + ' ' + self.windspeed_units,
                          'wind gusts: ' + str(self.gusts) + ' ' + self.gust_units,
                          'wind direction: ' + self.wind_direction]
        elif isinstance(self.wind_speed, float) and isinstance(self.gusts, str):
            conditions = ['wind speed: ' + str(self.wind_speed) + ' ' + self.windspeed_units,
                          'wind gusts: ' + str(self.gusts),
                          'wind direction: ' + self.wind_direction]
        elif isinstance(self.wind_speed, str) and isinstance(self.gusts, float):
            conditions = ['wind speed: ' + str(self.wind_speed),
                          'wind gusts: ' + str(self.gusts) + ' ' + self.gust_units,
                          'wind direction: ' + self.wind_direction]
        else:
            conditions = ['wind speed: ' + str(self.wind_speed),
                          'wind gusts: ' + str(self.gusts),
                          'wind direction: ' + self.wind_direction]
        for item in conditions:
            # uncomment to print items in a readable way
            # print(str(item))
            pass
        return 'Data list: ' + str(conditions)

    def collect_recent_wind_values(self, data_list):
        """
        Function checks the data list to ensure that relevant data is filled in and then returns a list
        with wind data.

        Args:
        data_list (list): List of data pertaining to one line of buoy data.

        Returns:
            list : List with wind speed, wind gust speed and wind direction.
        """
        wind_speed = ''
        wind_gusts = ''
        wind_direction = ''
        if data_list[6] != "MM":
            wind_speed = data_list[8]
        if data_list[7] != "MM":
            wind_gusts = data_list[9]
        if data_list[5] != "MM":
            wind_direction = data_list[11]

        return [wind_speed, wind_gusts, wind_direction]

    def get_wind_speed(self):
        """
        If wind data is found online, it returns a string with the wind speed and units. Else,
        it returns the string "Missing data from National Data Buoy Center." to display on the webpage.

        Args:
            None.
        Returns:
            self.wind_speed (string): with either the units if a value is found or a message to the user if not.
        """
        try:
            wind_speed = float(self.wind_speed)
            return str(wind_speed) + ' ' + f'{self.wind_speed_units}'
        except ValueError:
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

        try:
            wind_gusts = float(self.gusts)
            return str(wind_gusts) + ' ' + f'{self.gust_units}'
        except ValueError:
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

        try:
            direction = int(self.wind_direction)
            return str(direction) + ' ' + f'{self.direction_units}'
        except ValueError:
            return self.wind_direction
