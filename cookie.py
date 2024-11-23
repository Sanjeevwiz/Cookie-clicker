import pyautogui as p 
import time 
p.moveTo(1120,1065)
p.click()
p.hotkey("ctrl","t")
p.sleep(1)
p.write('cookie clicker')
p.hotkey("enter")
p.sleep(2)
p.doubleClick(325,306)
p.click
try:
    # Continuous clicking loop
    while True:
        p.click(299,481)  # Click the cookie
        time.sleep(0.01)  # Adjust delay for faster or slower clicking

except KeyboardInterrupt:
    print("Bot stopped!")
