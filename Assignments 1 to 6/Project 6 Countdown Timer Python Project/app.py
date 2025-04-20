import time

# Function to perform countdown
def countdown_timer(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # \r to overwrite the line
        time.sleep(1)
        seconds -= 1
    
    print("00:00")
    print("Time's up! ⏰")

# Main function
def main():
    print("=== Countdown Timer ===")
    try:
        total_time = int(input("Enter the countdown time in seconds: "))
        countdown_timer(total_time)
    except ValueError:
        print("Please enter a valid number.")

# Run the program
main()
