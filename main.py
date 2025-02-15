from bs4 import BeautifulSoup

honda_all_msrps =[]
honda_all_names = []
toyota_all_years = []
toyota_all_msrps = []
toyota_all_names = []

with open('honda.html', 'r') as honda_html:
    honda_content = honda_html.read()

    honda_soup = BeautifulSoup(honda_content, 'lxml')
    honda_cards = honda_soup.find_all('article', class_='rzf-gry rzf-gry-card-tile card vehicle')

    for honda_card in honda_cards:
        honda_msrp = honda_card.find('div', class_='rzf-gry-card-vehicle-info').span.text
        honda_name = honda_card.find('div', class_ = 'vehicle-heading').text

        if len(honda_msrp) > 0:
            honda_all_msrps.append(honda_msrp)

        if len(honda_name) > 0:
            honda_all_names.append(honda_name)




with open('toyota.html', 'r') as toyota_html:
    toyota_content = toyota_html.read()

    toyota_soup = BeautifulSoup(toyota_content, 'lxml')
    toyota_cards = toyota_soup.find_all('div', class_='vehicle-card')

    for toyota_card in toyota_cards:
        toyota_msrp = toyota_card.find('div', class_='header body-01').text
        toyota_name = toyota_card.find('div', class_='title heading-04').text
        toyota_year = toyota_card.find('div', class_='model-year label-01').text

        toyota_all_msrps.append(toyota_msrp)
        toyota_all_names.append(toyota_name)
        toyota_all_years.append(toyota_year)
