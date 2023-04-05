import requests
from bs4 import BeautifulSoup
import pandas as pd
pages_crawled = []
def crawler(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    finalrev = []
    df = pd.DataFrame()
    for link in links:
        if 'href' in link.attrs:
            if link['href'].startswith('?page') and ':' not in link['href']:
                if link['href'] not in pages_crawled:
                    new_link = f"https://www.consumeraffairs.com/sporting_goods/nike.html{link['href']}"
                    print(new_link)
                    pages_crawled.append(link['href'])
                    try:
                        reviews = []
                        table = soup.find_all('div', attrs = {'class':'rvw-bd'})
                        for x in table:
                            reviews.append(str(x.findAll('p')))
                        rev4 = []
                        table4 = soup.findAll('div', attrs={'class': 'rvw-bd'})
                        for x in table4:
                            tb2 = x.findAll('div', {'class': 'js-collapsed'})
                            for x in tb2:
                                rev4.append(x.find('p').text)
                        rev = reviews + rev4
                        df1 = pd.DataFrame(rev)
                        df = df.append(df1)
                        df.to_csv('out.csv', mode='a', index=False, header=False)
                        
                        crawler(new_link)
                    except:
                        continue
                    #finalrev.append(rev)
    #print(type(df[1]))
    #print(len(df.columns))
    #df.to_csv('out.csv', index=False)
    return df
result = crawler('https://www.consumeraffairs.com/sporting_goods/nike.html')
print(type(result))
print(len(result.columns))
print(len(result))
