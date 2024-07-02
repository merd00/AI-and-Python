import requests
import bs4

url = 'https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=Ordu'

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

