# Shop: отображение страницы товара
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
# 2. Залогиньтесь
my_account = driver.find_element_by_id("menu-item-50").click()
email = driver.find_element_by_id("username")
email.send_keys("rihasi6404@tonaeto.com")
password = driver.find_element_by_id("password")
password.send_keys("rihasi6404@tonaeto.com")
login_btn = driver.find_element_by_css_selector("[name='login']")
login_btn.click()
# 3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# 4. Откройте книгу "HTML 5 Forms"
open_book = driver.find_element_by_css_selector("[alt='Mastering HTML5 Forms']").click()
# 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
book_name = driver.find_element_by_css_selector("[itemprop='name']")
book_name_text = book_name.text
assert book_name_text == "HTML5 Forms"
driver.quit()



# Shop: количество товаров в категории
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
# 2. Залогиньтесь
my_account = driver.find_element_by_id("menu-item-50").click()
email = driver.find_element_by_id("username")
email.send_keys("rihasi6404@tonaeto.com")
password = driver.find_element_by_id("password")
password.send_keys("rihasi6404@tonaeto.com")
login_btn = driver.find_element_by_css_selector("[name='login']")
login_btn.click()
# 3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# 4. Откройте категорию "HTML"
html = driver.find_element_by_css_selector(".cat-item-19 > a").click()
# 5. Добавьте тест, что отображается три товара
products = driver.find_elements_by_css_selector("[data-quantity='1']")
assert len(products) == 3
driver.quit()



# Shop: сортировка товаров
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
# 2. Залогиньтесь
my_account = driver.find_element_by_id("menu-item-50").click()
email = driver.find_element_by_id("username")
email.send_keys("rihasi6404@tonaeto.com")
password = driver.find_element_by_id("password")
password.send_keys("rihasi6404@tonaeto.com")
login_btn = driver.find_element_by_css_selector("[name='login']")
login_btn.click()
# 3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию. Используйте проверку по value
filter = driver.find_element_by_css_selector("[value='menu_order']")
filter_selected = filter.get_attribute("selected")
assert filter_selected is not None
# 5. Отсортируйте товары по цене от большей к меньшей, в селекторах используйте класс Select
from selenium.webdriver.support.select import Select
# default_sorting = driver.find_element_by_css_selector("select[name='orderby']")
# select = Select(default_sorting)
# select.select_by_visible_text("Default sorting")
high_low = driver.find_element_by_css_selector("select.orderby")
select = Select(high_low)
select.select_by_visible_text("Sort by price: high to low")
# 6. Снова объявите переменную с локатором основного селектора сортировки, т.к. после сортировки страница обновится
default_sorting = driver.find_element_by_css_selector("select[name='orderby']")
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей. Используйте проверку по value
filter = driver.find_element_by_css_selector("[value='price-desc']")
filter_selected = filter.get_attribute("selected")
assert filter_selected is not None
driver.quit()



# Shop: отображение, скидка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# 2. Залогиньтесь
my_account = driver.find_element_by_id("menu-item-50").click()
email = driver.find_element_by_id("username")
email.send_keys("rihasi6404@tonaeto.com")
password = driver.find_element_by_id("password")
password.send_keys("rihasi6404@tonaeto.com")
login_btn = driver.find_element_by_css_selector("[name='login']")
login_btn.click()
# 3. Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# 4. Откройте книгу "Android Quick Start Guide"
book = driver.find_element_by_css_selector("[alt='Android Quick Start Guide']").click()
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
# 7. Добавьте явное ожидание и нажмите на обложку книги
# Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
cover.click()
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа
cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
cover_close.click()
driver.quit()



# Shop: проверка цены в корзине
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("http://practice.automationtesting.in/")
# 2. Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
book = driver.find_element_by_css_selector("[data-product_id='182']").click()
# # 4. Добавьте тест, что возле коризны (вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00". Используйте для проверки assert
# cart_content = driver.find_element_by_class_name("cartcontents")
# cart_content_text = cart_content.text
# assert cart_content_text == "1 item"
# cart_amount = driver.find_element_by_css_selector("#wpmenucartli .amount")
# cart_amount_text = cart_amount.text
# assert cart_amount == "₹180.00"
# 5. Перейдите в корзину
basket = driver.find_element_by_css_selector("[title='View Basket']").click()
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# subtotal = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-title='Subtotal'] > .amount")))
# subtotal_text = subtotal.text
# assert subtotal_text is not None
subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] > .amount"), "₹180.00"))
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
total = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "strong > .amount")))
total_text = total.text
assert total_text is not None
driver.quit()



# Shop: работа в корзине
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
import time
# Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("http://practice.automationtesting.in/")
# 2. Нажмите на вкладку "Shop"
shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
book_1 = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(2)
book_2 = driver.find_element_by_css_selector("[data-product_id='180']").click()
# 4. Перейдите в корзину
basket = driver.find_element_by_css_selector(".wpmenucart-contents").click()
time.sleep(2)
# 5. Удалите первую книгу. Перед удалением добавьте sleep
book_1_del = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(2)
# 6. Нажмите на Undo (отмена удаления)
# book_1_undo = driver.find_element_by_css_selector(".woocommerce-message > a").click()
book_1_undo = driver.find_element_by_link_text("Undo?").click()
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
qty = driver.find_element_by_css_selector(".cart_item:nth-child(1) input").clear()
qty_add = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
qty_add.send_keys("3")
time.sleep(2)
# 8. Нажмите на кнопку "UPDATE BASKET"
update_cart = driver.find_element_by_css_selector("[name='update_cart']").click()
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
qty_value = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
qty_value_check = qty_value.get_attribute("value")
assert qty_value_check == "3"
time.sleep(2)
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
apply_coupon = driver.find_element_by_css_selector("[name='apply_coupon']").click()
time.sleep(2)
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# # если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии
message = driver.find_element_by_css_selector(".woocommerce-error li")
message_text = message.text
assert message_text == "Please enter a coupon code."
driver.quit()



# Shop: покупка товара
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
import time
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get("http://practice.automationtesting.in/")
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
shop = driver.find_element_by_css_selector("#menu-item-40 > a").click()
driver.execute_script("window.scrollBy(0, 300);")
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
add_book = driver.find_element_by_css_selector("[data-product_id='182']").click()
# 4. Перейдите в корзину
basket_ec = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".added_to_cart")))
basket = driver.find_element_by_css_selector(".added_to_cart").click()
# 5. Нажмите "PROCEED TO CHECKOUT". Перед нажатием, добавьте явное ожидание
checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn = driver.find_element_by_class_name("checkout-button")
checkout_btn.click()
# 6. Заполните все обязательные поля. Перед заполнением first name, добавьте явное ожидание
# Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
first_name_ec = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Ivan")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Petrov")
email = driver.find_element_by_id("billing_email")
email.send_keys("mail@mail.com")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("168686816")
country = driver.find_element_by_id("select2-chosen-1").click()
country_add = driver.find_element_by_id("s2id_autogen1_search")
country_add.send_keys("United States (US)")
address = driver.find_element_by_id("billing_address_1")
address.send_keys("5th Avenue, 20-50")
city = driver.find_element_by_id("billing_city")
city.send_keys("New York")
state_add = driver.find_element_by_id("billing_state")
state_add.send_keys("NY")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("11250")
# # 7. Выберите способ оплаты "Check Payments". Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
payment_method = driver.find_element_by_id("payment_method_cheque")
# payment_method.click() # НЕ РАБОТАЕТ
driver.execute_script("arguments[0].click();", payment_method)
# 8. Нажмите PLACE ORDER
place_order = driver.find_element_by_id("place_order")
# place_order.click() # НЕ РАБОТАЕТ
driver.execute_script("arguments[0].click();", place_order)
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
thank_you = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
check_payments = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))
driver.quit()
