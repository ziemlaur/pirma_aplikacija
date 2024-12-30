import pyautogui
import pygetwindow
# b = pyautogui.locateOnScreen(r"C:\Users\Gustavas\Desktop\submit.png")
# print(b)


# pyautogui.click(100, 200); pyautogui.write('Hello, world!', 0.1)
# # pyautogui.move(100, 200, duration = 0.4)

# pyautogui.alert('labas') ok
# pyautogui.confirm('bbd') ok cancel
# pyautogui.prompt('text') inputas
# pyautogui.password('text') zvaigzdutes




# 1. How can you trigger PyAutoGUI’s fail-safe to stop a program?
# ctrl alt del, throw mouse in to corner

# 2. What function returns the current resolution()?
# pyautogui.size()

# 3. What function returns the coordinates for the mouse cursor’s current position?
# pyautogui.position()

# 4. What is the difference between pyautogui.moveTo() and pyautogui.move()?
# move to moves to specific coordinate, move moves from current position

# 5. What functions can be used to drag the mouse?
# .drag(), .dragTo(), .move() .moveTo()

# 6. What function call will type out the characters of "Hello, world!"?
# pyautogui.write()

# 7. How can you do keypresses for special keys such as the keyboard’s left arrow key?
# press(key)


# 8. How can you save the current contents of the screen to an image file named screenshot.png?
# pyautogui.screenshot()
# screenshot.save(screenshot.png)


# 9. What code would set a two-second pause after every PyAutoGUI function call?

# sleep(2)

# 10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?
# ?????????

# 11. What makes PyAutoGUI error-prone?
    #   Image Recognition, Mouse Coordinates


# 12. How can you find the size of every window on the screen that includes the text Notepad in its title?

# import pygetwindow as gw

# all_windows = gw.getAllTitles()

# print("All open windows:")
# print(all_windows)

# notepad_windows = [window for window in gw.getWindowsWithTitle('Notepad')]

# if notepad_windows:
#     for window in notepad_windows:
#         print(f"Window Title: {window.title}")
#         print(f"Size: Width={window.width}, Height={window.height}")
# else:
#     print("No Notepad windows found.")


# 13. How can you make, say, the Firefox browser active and in front of every other window on the screen?
# import pygetwindow as gw
# windows = gw.getWindowsWithTitle('Firefox')
# if windows:
#     firefox_window = windows[0]
#     firefox_window.activate()




# 1.	Write a script that opens a text editor, types "Hello, World!" and saves the file using `pyautogui`.  

# import pyautogui
# import time
# import os


# os.system("notepad")

# time.sleep(2)

# pyautogui.write("Hello, World!", interval=0.2)

# pyautogui.hotkey("ctrl", "s")  
# time.sleep(1) 

# pyautogui.write("hello_world.txt", interval=0.1)
# pyautogui.press("enter") 

# time.sleep(2)




# 2.	Create a program that takes a screenshot and locates a specific image on the screen.  

# import pyautogui
# import time
# import os

# def take_screenshot_and_locate_image(image_path, output_screenshot='screenshot.png'):
#     try:
#         output_dir = os.path.dirname(output_screenshot)
#         if output_dir and not os.path.exists(output_dir):
#             print(f"Directory does not exist. Creating directory: {output_dir}")
#             os.makedirs(output_dir)

#         screenshot = pyautogui.screenshot()
#         screenshot.save(r'C:\Users\Gustavas\Desktop\screenshot.png')
#         print(f"Screenshot saved as {output_screenshot}")

#         location = pyautogui.locateOnScreen(image_path)
#         if location:
#             print(f"Image found at {location}")
#             return location
#         else:
#             print("Image not found on the screen.")
#             return None

#     except Exception as e:
#         print(f"An error occurred: {e}")

# take_screenshot_and_locate_image(r"C:\Users\Gustavas\Desktop\sub.png", 'screenshot.png')



# 3.	Write a script that automates opening a website and navigating through a few pages.  
# import pyautogui
# import time
# import webbrowser
# import os

# def open_browser_and_navigate():
    
#     webbrowser.open("https://pigu.lt/lt/")
#     print("Browser opened and website loaded.")

    
#     time.sleep(5)



#     pyautogui.moveTo(500, 300)  
#     pyautogui.click()            

#     print("Navigating to Electronics category...")
#     time.sleep(3)  

#     pyautogui.moveTo(600, 400) 
#     pyautogui.click()            
#     print("Navigating to product page...")
#     time.sleep(3) 


#     pyautogui.press('backspace')  
#     time.sleep(3)  

#     pyautogui.moveTo(600, 500)  
#     pyautogui.click()            
#     print("Navigating to Fashion category...")
#     time.sleep(3)  

#     pyautogui.hotkey('ctrl', 'w')
#     print("Browser tab closed.")


# open_browser_and_navigate()


# 4.	Record an SAP script and modify it to navigate through multiple transactions.  
# ....

# 5.	Write a Python script that logs into SAP, navigates to a specific transaction, and inputs data.  
# .....

# 6.	Create a script that extracts data from an SAP report and saves it to a CSV file.  
# ....