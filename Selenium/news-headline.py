from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = 'https://www.thesun.co.uk/sport/football/'
path = '/usr/bin/chromedriver'

# Make headless
options = Options()
options.add_argument('---headless')


service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

titles = []
subtitles = []
links = []

containers = driver.find_elements(by="xpath", value="//div[@class='teaser__copy-container']")

for container in containers:
    title = container.find_element(by="xpath", value="./a/span").text
    subtitle = container.find_element(by="xpath", value="./a/h3").text
    link = container.find_element(by="xpath", value="./a").get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

news_dict = {
    'title': titles,
    'subtitle': subtitles,
    'link': links
}

news_df = pd.DataFrame(news_dict)
news_df.to_csv('headlines-headless.csv')

driver.quit()
