from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
driver = None
def perform_browser_action(command: str , debug: bool = False):
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    
    # if driver is None:   # this part is for headless browser 
    #     chrome_options = Options()
    

    # if not debug:
    #     chrome_options.add_argument("--headless")
    #     chrome_options.add_argument("--disable-gpu")
    #     chrome_options.add_argument("--window-size=1920,1080")

    # driver = webdriver.Chrome(options=chrome_options)


    if "search" in command.lower():  # this will open the browser and open the search query
        driver.get("https://www.google.com")
        time.sleep(2)
        search = driver.find_element(By.NAME, "q")
        query = command.replace("search", "").strip()
        print(f"Searching for: {query}")
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        time.sleep(5)
    
    # driver.quit()
    # return f"Command '{command}' executed in browser."


    if "scroll down" in command.lower(): # this is for the scroll down 
        scroll_down(driver, 500)
        time.sleep(3)

    if "scroll up" in command.lower(): # this is for the scrool up
        scroll_up(driver, 500)


    if "extract links" in command.lower(): # this will extract the link from the browser
        links = extract_links(driver)
        return links

    if "open new tab" in command.lower():  # this will open the new tab
        url = command.replace("open new tab", "").strip()
        driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(2)


    if "switch to tab" in command.lower(): # this will switch the tab with given index number 
        try:
            index = int(command.split("tab")[1].strip())
            driver.switch_to.window(driver.window_handles[index])
            time.sleep(2)
        except:
            return "Invalid tab index!"
        
    if "close tab" in command.lower(): # this is for the closing the broswer
        try:
            driver.close()

            if len(driver.window_handles) > 0:
                driver.switch_to.window(driver.window_handles[0])
            return "Tab closed successfully."
        except Exception as e:
            return f"Error while closing tab: {str(e)}"

        


    if not debug:
        # driver.quit()
        pass
    else:
        time.sleep(30) 

    return f"Command '{command}' executed in browser."


def scroll_down(driver, pixels,delay=2):
    driver.execute_script(f"window.scrollBy(0, {pixels});")
    time.sleep(delay) 

def extract_links(driver):
    return [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, "a")]

def scroll_up(driver, pixels=500, delay=2):
    driver.execute_script(f"window.scrollBy(0, -{pixels});")
    time.sleep(delay)








