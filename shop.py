import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
wait=WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

############################################## Отображение страницы товара #############################################
# Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Перейти в вкладку My Account
button_my_account=driver.find_element(By.LINK_TEXT, "My Account").click()
# Авторизоваться
username=driver.find_element(By.ID, "username")
username.send_keys("test.project@yandex.ru")
password=driver.find_element(By.ID, "password")
password.send_keys("test.project%!")
button_login=driver.find_element(By.NAME, "login").click()
# Перейти в вкладку Shop
button_shop=driver.find_element(By.LINK_TEXT, "Shop").click()
# Открыть книгу HTML 5 Form и тест заголовка
open_book=driver.find_element_by_xpath("//*[@id='content']/ul/li[3]/a[1]/img").click()
Book_title_test=driver.find_element_by_xpath("//div [@class='summary entry-summary']//h1")
text=Book_title_test.text
assert text == "HTML5 Forms"
print("The book matches")
driver.quit()
############################################### Количество тавара в категории ##########################################
# Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Перейти в вкладку My Account
button_my_account=driver.find_element(By.LINK_TEXT, "My Account").click()
# Авторизоваться
username=driver.find_element(By.ID, "username")
username.send_keys("test.project@yandex.ru")
password=driver.find_element(By.ID, "password")
password.send_keys("test.project%!")
button_login=driver.find_element(By.NAME, "login").click()
# Перейти в вкладку Shop
button_shop=driver.find_element(By.LINK_TEXT, "Shop").click()
# Открыть категорию HTML
button_html=driver.find_element_by_link_text("HTML").click()
# Тест на отображения 3х товаров на страницу
book_1=driver.find_element_by_css_selector("[data-product_id='181']").click()
time.sleep(1)
book_2=driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(1)
book_3=driver.find_element_by_css_selector("[data-product_id='163']").click()
time.sleep(1)
book_cor=driver.find_element_by_xpath("// span [@class='cartcontents']")
test=book_cor.text
if test and "3 items":
    print("In section 3 of the book")
else:
    print("Product quantity is incorrect")
driver.quit()
################################################## Сортировка товара ###################################################
# Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Перейти в вкладку My Account
button_my_account=driver.find_element(By.LINK_TEXT, "My Account").click()
# Авторизоваться
username=driver.find_element(By.ID, "username")
username.send_keys("test.project@yandex.ru")
password=driver.find_element(By.ID, "password")
password.send_keys("test.project%!")
button_login=driver.find_element(By.NAME, "login").click()
# Перейти в вкладку Shop
button_shop=driver.find_element(By.LINK_TEXT, "Shop").click()
# Тест что в селекторе выбран вариант по умолчанию через Value
selector=driver.find_element_by_name("orderby")
selector_default=selector.get_attribute("value")
if selector_default == "menu_order":
    print("Selector Default = Default sorting")
else:
    print("Selector Another selector selected")
# Отсортировать товары по цене от большей к меньшей используя класс select
selector=driver.find_element_by_tag_name("select")
select=Select(selector)
select.select_by_index(5)
# Тест что выбран селектора по цене от большей к меньшей методом Value
selector=selector=driver.find_element_by_name("orderby")
selector_high_to_low=selector.get_attribute("value")
if selector_high_to_low == "price-desc":
    print("Selector high to low")
else:
    print("Error selector")
driver.quit()
############################################## Отображения скидки товара ###############################################
# Открытие страницы
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Переход во вкладку "My Account"
button_my_account=driver.find_element(By.LINK_TEXT, "My Account").click()
# # Авторизация
username=driver.find_element(By.ID, "username")
username.send_keys("test.project@yandex.ru")
password=driver.find_element(By.ID, "password")
password.send_keys("test.project%!")
button_login=driver.find_element(By.NAME, "login").click()
# # Переход в вкладку "Shop"
button_shop=driver.find_element(By.LINK_TEXT, "Shop").click()
# Открытие книги "Android Quick Guide"
open_book=driver.find_element(By.XPATH, "//div [@class='list-post']/ul/li/a/img [@title='Android Quick Start Guide']").click()
# Тест строки старая цена метод assert
old_price=driver.find_element(By.XPATH, "//div/p/del/span")
old_price_value=old_price.text
assert old_price_value == "₹600.00"
print("Old price = ₹600.00")
# Тест строки новой цены метод assert
new_price=driver.find_element(By.XPATH, "//div/p/ins/span")
new_price_value=new_price.text
assert new_price_value == "₹450.00"
print("new_price = ₹450.00")
# Открыть окно предпросмотра явным ожиданием.
cover=wait(driver, 40).until(EC.element_to_be_clickable((By.CLASS_NAME, "images"))).click()
# Закрыть явным ожиданием окно предпросмотра
cover_close=wait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
driver.quit()
############################################### Проверка цены в корзине ################################################
# Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Перейти в раздел "Shop"
button_shop=driver.find_element(By.LINK_TEXT, "Shop").click()
# Добавить книгу в корзину
add_book=driver.find_element(By.XPATH, "//div [@id='content']/ul/li [4]/a [2]").click()
# Тест отображения товара в корзине и стоимость методом assert
time.sleep(2)
product=driver.find_element(By.CLASS_NAME, "cartcontents")
product_test=product.text
assert product_test and "1 item"
price=driver.find_element(By.CLASS_NAME, "amount")
price_test=price.text
assert price_test == "₹180.00"
# Перейти в корзину
open_basket=driver.find_element(By.CLASS_NAME, "cartcontents").click()
# Явным ожиданием проверить отображение стоимости в Subtotal
subtotal=wait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, "//div [@class='cart_totals '] // span [@class='woocommerce-Price-amount amount']"), "₹180.00"))
# Явным ожиданием проверить отображение стоимости в Total
total=wait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH, "//div/table/tbody/tr[3]/td/strong/span"), "₹183.60"))
driver.quit()
####################################################### Работа в корзине ###############################################
# Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Перейти в раздел "Shop"
button_shop=driver.find_element(By.LINK_TEXT, "Shop").click()
# Добавить в корзину 2е книги
time.sleep(1) #  VREMENO
driver.execute_script("window.scrollBy(0,300);")
add_book_one=driver.find_element(By.XPATH, "//*[@id='content']/ul/li[4]/a[2]").click()
time.sleep(1)
add_book_two=driver.find_element(By.XPATH, "//*[@id='content']/ul/li[5]/a[2]").click()
# Перейти в корзину
basket=driver.find_element(By.CLASS_NAME, "cartcontents").click()
# Удалить первую книгу
time.sleep(2)
del_book=driver.find_element(By.CSS_SELECTOR, ".cart_item [data-product_id='182']").click()
# Нажать на Undo отмена удаления
time.sleep(1)
undo=driver.find_element(By.CSS_SELECTOR, ".woocommerce-message [href]").click()
# Увеличить кол-во товара книги "JS Data" до 3х штук предварительно очистив поле
time.sleep(2)
jd_data_book=driver.find_element(By.XPATH, "//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
jd_data_book.clear()
jd_data_book.send_keys("3")
# Нажать кнопку Update Basket
update=driver.find_element(By.NAME, "update_cart").click()
# Тест, что элемент Value = 3
time.sleep(1)
element=driver.find_element(By.XPATH, "//*[@id='page-34']/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
element_value=element.get_attribute("Value")
assert element_value == "3"
# Нажать на кнопку Apply coupon
time.sleep(2)
apply_btn=driver.find_element(By.NAME, "apply_coupon").click()
# Добавить тест сообщения Pleas enter a coupon code
time.sleep(2)
message=driver.find_element(By.CLASS_NAME, "woocommerce-error").text
if message and "Please enter a coupon code.":
    print("Message present")
else:
    print("message missing")
driver.quit()

#################################################### Покупка товара ###################################################
#Открыть страницу
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
# Перейти в раздел "Shop" и проскролить 300 пикселей вниз
button_shop=driver.find_element(By.LINK_TEXT, "Shop").click()
driver.execute_script("window.scrollBy(0,300);")
# Добавить в корзину книгу
add_book_one=driver.find_element(By.XPATH, "//*[@id='content']/ul/li[4]/a[2]").click()
# Перейти в корзину
time.sleep(1)
basket=driver.find_element(By.CLASS_NAME, "cartcontents").click()
#Нажать на Proceed to checkout с явным ожиданием
btn=wait(driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward"))).click()
# Заполнить все обязательные поля
first_name=wait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Sergey")
last_name=driver.find_element(By.ID, "billing_last_name")
last_name.send_keys("Vvvvvvvv")
email_address=driver.find_element_by_id("billing_email")
email_address.send_keys("test.project@yandex.ru")
phone=driver.find_element(By.NAME, "billing_phone")
phone.send_keys("+79651234567")
country=driver.find_element(By.ID, "s2id_billing_country").click()
country_field=driver.find_element_by_id("s2id_autogen1_search")
country_field.send_keys("Russia")
country_complit=driver.find_element(By.ID, "select2-result-label-394").click()
address=driver.find_element(By.ID, "billing_address_1").send_keys("my house")
city=driver.find_element(By.ID, "billing_city").send_keys("big tower")
state=driver.find_element(By.ID, "billing_state").send_keys("5")
postcode=driver.find_element(By.ID, "billing_postcode").send_keys("66666666")
# Выбрать способ оплаты Check Payments
driver.execute_script("window.scrollBy(0,600);")
time.sleep(2)
check_payments=driver.find_element(By.ID, "payment_method_cheque").click()
# Нажать на Place Order
place_order=driver.find_element_by_id("place_order").click()
# Не явным ожиданием проверить надпись Thank you. Your order has been received.
order=wait(driver, 40).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# Явным ожиданием проверить что в Payment Method отображается текст Check Payments
payment=wait(driver, 40).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id='page-35']/div/div[1]/table/tfoot/tr[3]/td"), "Check Payments"))
driver.quit()