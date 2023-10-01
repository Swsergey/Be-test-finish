from selenium import webdriver
from selenium.webdriver.common.by import By

############################################# Добавление коментария ###################################################
# Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Проскролить страницу на 600 пикселей
driver.execute_script("window.scrollBy(0,600);")
# Нажать на название книги Selenium Ruby
selenium_ruby=driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium Ruby")
selenium_ruby.click()
# Нажать на вкладку reviews
tab_reviews=driver.find_element(By.CLASS_NAME, "reviews_tab").click()
# Поставить 5 звёзд
rating=driver.find_element(By.CLASS_NAME, "star-5").click()
driver.execute_script("window.scrollBy(0,500);")
# Заполнить поле Review сообщением Nice Book
Review=driver.find_element(By.ID, "comment")
Review.send_keys("Nice book!")
# Заполнить Имя и емаил
Field_name=driver.find_element(By.ID, "author")
Field_name.send_keys("Sergey")
Field_email=driver.find_element(By.ID, "email")
Field_email.send_keys("test.project@yandex.ru")
# Нажать кнопку Submit
Button_submit=driver.find_element(By.CLASS_NAME, "submit").click()
driver.quit()
print("Test complit")