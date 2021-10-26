from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


options = Options()
options.headless = False
browser = webdriver.Firefox(options=options)
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

def Login(username, password):
    
    try:

        username_input = browser.find_element_by_css_selector('input[name = "username"]')
        password_input = browser.find_element_by_css_selector('input[name = "password"]')

        # username_input.send_keys(<username>)
        # password_input.send_keys(<password>)

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(2)
        browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    except:
        Login(username, password)


    
    

def Get_Followings(username):
    ## GET FOLLINGS
    try:
        # browser.find_element_by_xpath("//a[contains(@href, 'captain_boomerung')]").click()
        browser.find_element_by_xpath("//a[contains(@href, '/{}')]".format(username)).click()
        sleep(2)
        browser.find_element_by_xpath("//a[contains(@href, '/following')]").click()

        ## Followers
        scroll_box  = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[3]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = browser.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        sleep(2)
        following = scroll_box.find_elements_by_tag_name('a')
        following = [follower.get_attribute('href') for follower in following]
        for follower in following:
            Get_Profile(follower)

    except Exception as e:
        print(e)


def Get_Profile(url):
    browser.get(url)
    sleep(5)
    try:
        browser.find_element_by_xpath('//button//span/*[name()="svg"]').click()
        sleep(1)
        browser.find_element_by_xpath("//a[contains(.,'See All')]").click()
        sleep(1)
        follow_btn_elements = browser.find_elements_by_xpath("//div[contains(@aria-label,'Similar Accounts')]//button[contains(.,'Follow')]")
        # browser.find_element_by_xpath("//button[contains(.,'Follow')]").click()
        sleep(1)
        try:
            for btn in follow_btn_elements:
                sleep(2)
                btn.click()
        except:
            pass

    except:
        print("This profile does not have suggession")


Login("username", "password")
sleep(5)
Get_Followings("username")
sleep(5)
browser.close()



# from instapy import InstaPy
# session = InstaPy(username='username', password = 'password')
# session.login()
# session.set_do_like(True, percentage=50)







