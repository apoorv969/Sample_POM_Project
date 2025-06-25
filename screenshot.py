import os
from datetime import datetime

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    path = os.path.join(os.getcwd(), "Screenshots", filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    driver.save_screenshot(path)
    return path
