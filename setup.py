import requests
import time
import subprocess

subprocess.run(["python", "action.py"])

url = "https://homelesspigeon.vercel.app/core/pigeonbrain.js"  # Replace with the URL of the code
file_path = "code.txt"  # Path to save the code
# Fetch the code from the website
response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful
    # Write the content to the .txt file
    with open(file_path, "w") as file:
        file.write(response.text)
    print(f"Code from {url} has been saved to {file_path}")
else:
    print(f"Failed to fetch code. Status code: {response.status_code}")
#-----------------------------
print("--------------------")
print("")
print("")
print("")

def print_title(title):

    print("*" * (len(title) + 4))
    print(f"* {title} *")
    print("*" * (len(title) + 4))

print_title("CozmoXcel")

print("---")
print("V1")
print("---")

time.sleep(0.5)
print("""
This process will always go through an update check, even if no update is available. 
This is a critical step, so please ensure that you have a stable Wi-Fi connection with internet.

Follow the instructions carefully, and connect to the Cozmo robot's Wi-Fi when prompted to do so. 
This is essential for the successful setup of the system.
""")
print("--------------------")

print("""
An offline version will be available soon. 
This version will not require an internet connection, 
only the Cozmo robot's Wi-Fi will be needed to operate it.
""")

# Example with colored text
print("\033[31mThis is red text\033[0m")  # Red text
print("\033[32mThis is green text\033[0m")  # Green text
print("\033[33mThis is yellow text\033[0m")  # Yellow text
