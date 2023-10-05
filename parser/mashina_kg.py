import requests
from parsel import Selector


url = 'https://www.mashina.kg/new/search'
main_url = 'https://www.mashina.kg'

def get_html():
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

def parse_html(html):
    selector = Selector(text=html)
    return selector

if __name__ == '__main__':
    html = get_html()
    selector = parse_html(html)
    cars = selector.css('.listing.search-page.x-3 .listing-item.main')
    name = cars.css('a span[title]::text').getall()
    price = cars.css('.font-big.custom-margins::text, .font-small.custom-margins::text').getall()
    link = cars.css('a::attr(href)').getall()
new_cars = (name[0], price[0], main_url+link[0], name[1], price[1], main_url+link[1],
            name[2], price[2], main_url+link[2], name[3], price[3], main_url+link[3],
            name[4], price[4], main_url+link[4], name[5], price[5], main_url+link[5],
            name[6], price[6], main_url+link[6], name[7], price[7], main_url+link[7],
            name[8], price[8], main_url+link[8], name[9], price[9], main_url+link[9],
            name[10], price[10], main_url+link[10])
for c in new_cars:
    print(c)
