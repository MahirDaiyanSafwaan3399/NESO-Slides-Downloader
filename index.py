import time
import pyautogui
from pynput.keyboard import Controller, Key

keyboard = Controller()

# Number of slides to save
slide_count = 62  # Adjust based on total slides

# Small delay before starting (so you can move the cursor manually)
time.sleep(3)

for i in range(42, slide_count + 1):
    # Right-click on the image
    pyautogui.click(button="right")
    time.sleep(0.5)  # Wait for the context menu

    # Navigate to "Save image as..." using Down Arrow (adjust if needed)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.5)  # Small delay for menu navigation

    # Press Enter to open the "Save As" dialog
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)  # Wait for the save dialog to open

    # Type the filename (ensure an extension like .jpg or .png)
    pyautogui.write(f"{i}")
    time.sleep(0.5)

    # Press Enter to save
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)  # Wait for the saving process

    # Press Right Arrow to move to the next slide
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.5)  # Wait for slide transition

print("✅ All slides saved successfully!")
