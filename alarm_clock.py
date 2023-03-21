from playsound import playsound
import time

# ANSI escape codes for clearing the terminal screen and resetting the cursor position
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Function to format the time left as a string in the format "MM:SS"
def format_time_left(time_left):
    minutes_left = int(time_left // 60)
    seconds_left = int(time_left % 60)
    return f"{minutes_left:02d}:{seconds_left:02d}"

# Function to print the time left on the terminal with a clear screen and reset cursor position
def print_time_left(time_left):
    print(f"{CLEAR}{CLEAR_AND_RETURN}Alarm will sound in: {format_time_left(time_left)}")

# Function to run the alarm countdown and play the alarm sound when the time is up
def alarm(seconds):
    start_time = time.time()

    while True:
        time_elapsed = time.time() - start_time
        time_left = seconds - time_elapsed

        if time_left <= 0:
            break

        print_time_left(time_left)
        time.sleep(1)

    playsound("alarm.mp3")

# Prompt the user to input the number of minutes and seconds for the alarm countdown
minutes = int(input("How many minutes? "))
seconds = int(input("How many seconds? "))
total_seconds = minutes * 60 + seconds

# Run the alarm function with the user-defined total_seconds
alarm(total_seconds)
