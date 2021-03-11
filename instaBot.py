from time import sleep
from selenium import webdriver
from secret import pw
from selenium.webdriver.common.keys import Keys
class Bot():

    links = []

    def __init__(self):
        self.login('your_username')
        self.like_comment('your_hastag')

    def login(self, username):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        username_input = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        username_input.send_keys('your_username')
        password_input = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        password_input.send_keys('your_password')
        login_btn =self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
        login_btn.click()
        sleep(5)
        not_now_btn1 = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        not_now_btn1.click()
        sleep(60)
        notnow2 = self.driver.find_element_by_xpath('html/body/div[4]/div/div/div/div[3]/button[2]')
        notnow2.click()

    def like_comment(self, hashtag):
        search_box = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_box.send_keys('#'+hashtag)
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
        sleep(5)

        links = self.driver.find_elements_by_tag_name('a')
        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)
        for link in self.links:
            self.driver.get(link)

            #like
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(5)
            #comment
            self.driver.find_element_by_class_name('Ypffh').click()
            sleep(5)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys('lit')
            sleep(5)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]').click()
            sleep(3)

    def logout(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div').click()

        driver.close()
def main():
    my_bot = Bot()

if __name__ == '__main__' :
     main()
