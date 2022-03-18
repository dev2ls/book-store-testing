# Registration_login: регистрация аккаунта
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
# 2. Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50").click()
# 3. В разделе "Register", введите email для регистрации
email = driver.find_element_by_id("reg_email")
email.send_keys("rihasi6404@tonaeto.com")
# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
password = driver.find_element_by_id("reg_password")
password.send_keys("rihasi6404@tonaeto.com")
# 5. Нажмите на кнопку "Register"
register_btn = driver.find_element_by_css_selector("[name='register']")
register_btn.click()
driver.quit()



# Registration_login: логин в систему
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
# 2. Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50").click()
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
email = driver.find_element_by_id("username")
email.send_keys("rihasi6404@tonaeto.com")
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
password = driver.find_element_by_id("password")
password.send_keys("rihasi6404@tonaeto.com")
# 5. Нажмите на кнопку "Login"
login_btn = driver.find_element_by_css_selector("[name='login']")
login_btn.click()
# 6. Добавьте проверку, что на странице есть элемент "Logout"
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation [href='http://practice.automationtesting.in/my-account/customer-logout/']")
logout_text = logout.text
assert logout_text == "Logout"
driver.quit()