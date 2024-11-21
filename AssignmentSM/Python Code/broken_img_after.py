# -*- coding: utf-8 -*-

"""
https://the-internet.herokuapp.com/broken_images
"""

import unittest
import requests
from selenium import webdriver  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore


class TestBrokenImages(unittest.TestCase):
    """A test case for verifying broken images on a webpage
       This test navigates to a webpage containing images,
       checks each iamge URL,
       and verifies if any images are broken by analyzing
       their HTTP response codes.
    """

    def setUp(self):
        """Set up the Selenium WebDriver and navigate to the test URL."""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.base_url = "https://the-internet.herokuapp.com/broken_images"

    def test_broken_images(self):
        """Test for broken images on the page by validating
           HTTP response code.
        """
        driver = self.driver
        driver.get(self.base_url)
        image_list = driver.find_elements(By.TAG_NAME, "img")
        broken_images = 0
        for image in image_list:
            src = image.get_attribute('src')
            if src:
                response = requests.get(src, stream=True, timeout=10)
                if response.status_code != 200:
                    broken_images += 1
            else:
                broken_images += 1
        self.assertEqual(broken_images, 2)

    def tearDown(self) -> None:
        """Quit the WebDriver and clean up resources."""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
