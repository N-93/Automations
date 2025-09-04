import pyautogui
import time

# Step 1: Read your code from a file
file_path = r'C:\Users\nisch\OneDrive\Documents\sctipt.txt'
with open(file_path, "r", encoding="utf-8") as f:
    code_lines = f.readlines()

# Step 2: Give you time to click in the input area
print("You have 5 seconds to click where the code should be typed...")
time.sleep(5)

# Step 3: Type the code line by line
for line in code_lines:
    pyautogui.write(line)  # Adjust speed if needed






# #generate a code that types the text "Hello, World!"in a editor
# import pyautogui
# import time

# # Give you 5 seconds to click into the website input field
# print("You have 5 seconds to click in the website's text box...")
# time.sleep(5)

# # Type the message
# pyautogui.write("Hello, World!", interval=0.1)
