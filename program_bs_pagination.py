from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movie_letter-A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

pagination = soup.find('ul', class_="pagination")
pages = pagination.find_all('li', class_="page-item")
last_page = pages[-2].text

for page in range(1, int(last_page)+1):
    website = f'{website}?page={page}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    links = []

    for link in box.find_all('a', href=True):
        links.append(link['href'])
    print(links)

    for link in links:
        try:
            print(link)
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()
            title = ''.join(title.split('/'))
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            #with open(f'{title}.txt', 'w') as file:
            #    file.write(transcript)
        except:
            print("-------- Link not working --------")
            print(link)


