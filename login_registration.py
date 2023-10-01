from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()

################################################## Регистрация аккаунта ################################################
# Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Перейти в вкладку My Account
button_my_account=driver.find_element(By.LINK_TEXT, "My Account").click()
# Заполнить логин и пароль (пороль должен иметь сложность Medium или Strong)
reg_email=driver.find_element(By.ID, "reg_email")
reg_email.send_keys("test.project@yandex.ru")
reg_pass=driver.find_element(By.ID, "reg_password")
reg_pass.send_keys("test.project%!")
# Нажать кнопку Register
button_register=driver.find_element(By.NAME, "register").click()
driver.quit()
print("Registration complit")
################################################# Логин в систему ######################################################
# Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Перейти в вкладку My Account
button_my_account=driver.find_element(By.LINK_TEXT, "My Account").click()
# Заполнить логин и пароль
username=driver.find_element(By.ID, "username")
username.send_keys("test.project@yandex.ru")
password=driver.find_element(By.ID, "password")
password.send_keys("test.project%!")
# Нажать кнопку Login
button_login=driver.find_element(By.NAME, "login").click()
# Тест что на странице есть элемент Logout
logout=driver.find_element(By.LINK_TEXT, "Logout")
logout_test=logout.text
if logout_test and "Logout":
    print("On the page the Logut element is located")
else:
    print("Item not found")
driver.quit()