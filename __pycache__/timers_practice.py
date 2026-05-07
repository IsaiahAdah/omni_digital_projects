import time

countdown = 10
while countdown > 0:
    print(f"Countdown: {countdown} seconds remaining")
    time.sleep(1)  # Wait for 1 second
    countdown -= 1

print("Time's up!")

