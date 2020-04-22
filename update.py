import requests
import bs4
import pandas as pd
import requests

url_1 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_2 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
url_3 = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

def update_world():
    r = requests.get(url_1)
    with open('confirmed.csv', 'wb') as f:
        f.write(r.content)

    r = requests.get(url_2)
    with open('recovered.csv', 'wb') as f:
        f.write(r.content)

    r = requests.get(url_3)
    with open('death.csv', 'wb') as f:
        f.write(r.content)

def update_vietnam():
    url = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Vietnam'
    def get_page_contents(url):
        page = requests.get(url, headers={"Accept-Language": "en-US"})
        return bs4.BeautifulSoup(page.text, "html.parser")

    ct = get_page_contents(url)
    ct2 = ct.findAll( class_="wikitable")
    ct3=ct2[2].findAll("td")
    ct4=[content.text for content in ct3]
    ct4= [element.rstrip("\n")for element in ct4]

    main_data=[]
    def chunker(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))
    for group in chunker(ct4, 4):
        main_data.append(group)

    df = pd.DataFrame(main_data, columns =['province', 'cases','recovered','death']) 
    df.to_csv('corona_vietnam.csv')


update_world()
update_vietnam()
