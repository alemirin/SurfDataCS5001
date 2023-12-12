# Final Project Report

* Student Name: Alejandro Miranda
* Github Username: alemirin
* Semester: Fall 2023
* Course: CS5001



## Description
General overview of the project, what you did, why you did it, etc.

• The project's aim is to take raw data from the National Data Buoy Center (NOAA) and display the data that surfers would find important/ relevant in a neat and concise way.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on.

• The project reads the raw buoy data and extracts the relevant information in order to concisely portray the information to surfers. I am proud of my use of classes to neatly separate the buoy data into types of data and read the websites to organize the important data so that it is easy to display and connect to the html script.


## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features.

• Once all of the things are downloaded, open a terminal window at the directory where surfapp.py, buoydatareader.py and the static and templates folder are located and run the webpage within terminal using python3 surfapp.py. Once the terminal gives a message that the app is running on your IP address, go to your browser on the device and access the webpage using the url localhost:5000 . I've also included screenshots of how the page appeared on my device. You can also access the data for San Juan by adding "/sanjuan" to the localhost url.



## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

• To run the project, you must download all of the files in the Github repository and make sure to download flask using pip install flask. Something that I had to do to get the webpage with real time data capture to work was go in Mac to Applications > Python > CertificatesInstall.command.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did.

```python
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
```

The code block above was challenging to create as I had to find a way for the program to sift through multiple recent lines of data to find values for different conditions. Yet, if a value had already been found previously then we would not want to rewrite it, as subsequent lines in the file refer to earlier data entries, which is not the most recent data available. Furthermore, if no valid values are found then we need to display to the user that data regarding that condition is not available. The code block above works together alongside the collect_recent_wave_values() function within the Waves class. There is also a version of this in the Winds() class.

I learned a lot about html and css as well during this project but since this class is on Python I will refrain from going into detail about those languages.

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

• One large part of what made this project special to me was learning how to interface python with online data and leverage its classes and flexibility to create an appealing webpage that portrays real time data in an easy to digest way. Working with realtime unfiltered data can be tough and in this case the challenges were mainly missing data or data that was being collected at longer intervals than just one line on the webpage. This meant it was necessary to account for these possibilities by reading multiple lines to look for values and to be able to display these issues to the user. Although the course is not on front-end development, I found the process of building and styling a website challenging and rewarding, and am proud of my arrow that dynamically changes direction with the current wave direction data in degrees.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

• In the github repository I included a screenshot of the working webpage for Arecibo. The Arecibo buoy is currently not collecting relevant wind data thus it was also a practice in accounting for this data issue and being able to relate the issue to users. I also created a webpage for the San Juan buoy, which fortunately has the current wind conditions available.



## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission.

• The running of the project and almost all of the changes were made by running the webpage on localhost on google chrome through flask on debug mode. This allowed for real time changes to show up on the screen and made creating the webpage a very rewarding experience as you get to see the page develop over time.


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future.

• There's still so much to do with this, naturally I can continue adding locations to the webpage, and add a navigation bar that displays different beaches or areas from which to gather buoy data. Also, I could add more specific beach locations and offer information on how deep the water is, what the ground below the water is like (sand, reef, cobblestones, etc.), information on currents, and much more. Also, I hoped to implement a user system and this way users can favorite locations or get alerts when preferred conditions arise. Also, the forecast data could be implemented to see how the conditions will change in the future.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

• This program has been very useful to deepen my knowledge  ofand gain a sense of proper solid footing with Python. Some of the most important things I learned were techniques to organize and format code for clarity, how to read and filter/ process data within Python and of course all of the fundamentals of data structures and the flexibility of Python. To continue my learning process I plan on creating more projects and expanding on the ones I've created in the course, to gain a deeper understanding of libraries and of the possibilities with Python. One key lesson I've learned is that Python is an incredibly versatile tool that can be used not only for data analysis and computation but also  creating games and webpages.
