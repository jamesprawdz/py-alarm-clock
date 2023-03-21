Alarm Clock Mini-Project
========================

This is a simple command-line alarm clock program written in Python. The program takes user input for minutes and seconds and then starts a countdown. Once the countdown reaches zero, it plays an audio file named `alarm.mp3`.

Requirements
------------

-   Python 3.6+
-   `playsound` package: Install it using `pip install playsound`

Files
-----

-   `alarm_clock.py`: The main Python script that runs the alarm clock program.
-   `alarm.mp3`: The audio file that is played when the countdown reaches zero.

How to Run
----------

1.  Ensure you have Python 3.6+ installed on your system.
2.  Install the `playsound` package using `pip install playsound`.
3.  Place the `alarm_clock.py` script and the `alarm.mp3` file in the same directory.
4.  Run the `alarm_clock.py` script using `python alarm_clock.py` or `python3 alarm_clock.py`, depending on your system configuration.
5.  Enter the desired number of minutes and seconds for the countdown when prompted.
6.  The program will display the remaining time and play the `alarm.mp3` file when the countdown reaches zero.

Customizing the Alarm Sound
---------------------------

To use a different alarm sound, replace the `alarm.mp3` file with your desired audio file in MP3 format. Ensure that the new file is also named `alarm.mp3`, or update the `playsound()` function call in the `alarm()` function in the `alarm_clock.py` script to use the new file name.
