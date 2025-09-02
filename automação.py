import mouseinfo, pyautogui



mouseinfo.mouseInfo()
pyautogui.moveTo(654,1057, duration=1)
pyautogui.click()
pyautogui.moveTo(915,940, duration=1)
pyautogui.click()

pyautogui.write("Eevee")
pyautogui.press("Enter")

pyautogui.moveTo(543,114, duration=1)
pyautogui.click()
pyautogui.press("Blackspace")
pyautogui.write("Pokemon")
