from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ApplewebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537 .3'}

def currency(ammount, fv, sv):
    print('Converting...')

    res = requests.get(f'https://www.google.com/search?q={ammount}+{fv}+to+{sv}', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    #print(soup.prettify())
    second_value = soup.find('span', class_="DFlfde SwHCTb").getText('data-value').strip()
    fv = soup.find('span', class_="vLqKYe").getText('data-name').strip()
    sv = soup.find('span', class_="MWvIVe nGP2Tb").getText('data-name').strip()
    print(ammount, fv, 'equals', second_value, sv)


ammount = input('Ammount: ')
fv = input('First value: ')
sv = input('Second value: ')
currency(ammount, fv, sv)