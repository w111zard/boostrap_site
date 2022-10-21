import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url= "file:///home/wizard/Documents/boostrap_site/index.html"

class FirefoxTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="/home/wizard/Documents/boostrap_site/test/geckodriver")

    def test_next_lesson(self):
        driver = self.driver
        driver.get("file:///home/wizard/Documents/boostrap_site/lessons/lesson_1_1.html")
        button = driver.find_element(By.CLASS_NAME, "btn-success")
        button.click()
        title = driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("Комментарии", title.text)

    def test_button_text(self):
        driver = self.driver
        driver.get("file:///home/wizard/Documents/boostrap_site/lessons/lesson_1_1.html")
        button = driver.find_element(By.CLASS_NAME, "btn-success")
        self.assertIn("Следующий урок", button.text)

    def test_main_title(self):
        driver = self.driver
        driver.get(url);
        self.assertIn("Бесплатный учебник JS!", driver.title)

    def test_list_title(self):
        driver = self.driver
        driver.get(url)
        button = driver.find_element(By.CLASS_NAME, "btn-primary")
        button.click()
        self.assertIn("Список уроков", driver.title)

    def test_next_lesson2(self):
        driver = self.driver
        driver.get("file:///home/wizard/Documents/boostrap_site/lessons/lesson_1_3.html")
        button = driver.find_element(By.CLASS_NAME, "btn-success")
        button.click()
        title = driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("Арифметические операции", title.text)

    def test_navbar_brand(self):
        driver = self.driver
        driver.get(url)
        
        button = driver.find_element(By.CLASS_NAME, "btn-primary")
        button.click()
         
        button = driver.find_element(By.CLASS_NAME, "navbar-brand")
        button.click()

        self.assertIn("Бесплатный учебник JS!", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
