import os
import pathlib
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def file_uri(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return pathlib.Path(os.path.join(base_dir, filename)).as_uri()


driver = webdriver.Edge()


class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("counter.html"))
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "increase"))
        )
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")
        increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "1")

    def test_decrease(self):
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element(By.ID, "decrease")
        decrease.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increase(self):
        driver.get(file_uri("counter.html"))
        increase = driver.find_element(By.ID, "increase")
        for i in range(31):
            increase.click()
        self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "31")


if __name__ == "__main__":
    unittest.main()
