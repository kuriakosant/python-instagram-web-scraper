from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Replace with your Instagram credentials and target profile
username = 'your_instagram_username'
password = 'your_instagram_password'
target_profile = 'target_profile_username'

# Path to your WebDriver (ChromeDriver for Chrome)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

def login_instagram():
    driver.get('https://www.instagram.com/accounts/login/')
    sleep(2)

    # Enter username and password
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.send_keys(username)
    password_input.send_keys(password)

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    sleep(5)

def get_followers():
    # Navigate to the target profile's followers page
    driver.get(f'https://www.instagram.com/{target_profile}/followers/')
    sleep(2)

    # Scroll down to load all followers
    scroll_box = driver.find_element(By.XPATH, "//div[@role='dialog']//ul")
    last_height, height = 0, 1
    while last_height != height:
        last_height = height
        sleep(2)
        height = driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight; return arguments[0].scrollHeight;", scroll_box
        )

    # Get list of followers
    followers = scroll_box.find_elements(By.XPATH, "//li//a")
    follower_names = [follower.text for follower in followers if follower.text]
    return follower_names

def get_following():
    # Navigate to the target profile's following page
    driver.get(f'https://www.instagram.com/{target_profile}/following/')
    sleep(2)

    # Scroll down to load all followings
    scroll_box = driver.find_element(By.XPATH, "//div[@role='dialog']//ul")
    last_height, height = 0, 1
    while last_height != height:
        last_height = height
        sleep(2)
        height = driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight; return arguments[0].scrollHeight;", scroll_box
        )

    # Get list of following
    following = scroll_box.find_elements(By.XPATH, "//li//a")
    following_names = [person.text for person in following if person.text]
    return following_names

def find_non_mutuals(followers, following):
    # Non-mutuals are people the account follows but who don't follow back
    non_mutuals = [user for user in following if user not in followers]
    return non_mutuals

# Main script execution
login_instagram()

followers_list = get_followers()
following_list = get_following()

non_mutuals = find_non_mutuals(followers_list, following_list)
print(f"Non-mutual followers: {non_mutuals}")

driver.quit()
