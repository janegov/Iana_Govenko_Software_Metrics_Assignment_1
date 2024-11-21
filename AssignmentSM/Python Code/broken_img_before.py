# -*- coding: utf-8 -*-

"""
https://the-internet.herokuapp.com/broken_images
"""

import unittest
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBrokenImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "https://the-internet.herokuapp.com/broken_images"

    def test_broken_images(self):
        driver = self.driver
        driver.get(self.base_url)
        image_list = driver.find_elements(By.TAG_NAME, "img")
        broken_images = 0
        for image in image_list:
            src = image.get_attribute('src')
            if src:
                response = requests.get(src, stream=True)
                if response.status_code != 200:
                    broken_images += 1
            else:
                broken_images += 1
        self.assertEqual(broken_images, 2)

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
