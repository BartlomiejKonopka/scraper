from selenium import webdriver
from selenium.webdriver.common.by import By


website = 'https://www.investing.com/news/commodities-news'
driver = webdriver.Chrome()
driver.get(website)


news = driver.find_element(By.ID, 'leftColumn')
titles = news.find_elements(By.CLASS_NAME, 'title')

for x in titles:
    title = x.text
    link = x.get_attribute("href")
    driver.switch_to.new_window('tab')
    driver.get(link)
    text_box = driver.find_element(By.XPATH, '//*[@id="leftColumn"]/div[3]')
    contents = text_box.find_elements(By.TAG_NAME, 'p')

    text = []
    for x in contents:
        content = x.text
        text.append(content)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    with open("scrape.json", "a") as outfile:
        outfile.write('title: '+title+" ")
        outfile.write('link: '+link+" ")
        outfile.write('text: '+str(text)+" ")

driver.quit()