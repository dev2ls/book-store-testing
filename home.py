# Home: добавление комментария
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# 1. Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
# 2. Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
selenium_ruby = driver.find_element_by_css_selector("[title='Selenium Ruby']").click()
# 4. Нажмите на вкладку "REVIEWS"
reviews = driver.find_element_by_css_selector("[href='#tab-reviews']").click()
# 5. Поставьте 5 звёзд
rating = driver.find_element_by_class_name("star-5").click()
# 6. Заполните поле "Review" сообщением: "Nice book!"
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
# 7. Заполните поле "Name"
author = driver.find_element_by_id("author")
author.send_keys("Name")
# 8. Заполните "Email"
email = driver.find_element_by_id("email")
email.send_keys("email@email.com")
# 9. Нажмите на кнопку "SUBMIT"
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
driver.quit()
