from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SelectLanguage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        exp_options = ['English', 'French','German']
        act_options = []

        driver = self.driver
        select_language = Select(driver.find_element(By.ID, 'select-language'))
        self.assertEqual(3, len(select_language.options))


        for option in select_language.options:
            act_options.append(option.text)

        self.assertListEqual(exp_options, act_options)

        select_language.select_by_visible_text('German')
        sleep(8)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity = 2)

