from bs4 import BeautifulSoup
import requests

def get_info():
    # Station Reuss - Mellingen - 2018
    html_text = requests.get("https://www.hydrodaten.admin.ch/de/2018.html").text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', class_= 'table table-bordered table-narrow')
    time = table.find('small', class_='text-muted').text
    abfluss = table.find('td', class_='text-center').text
    
    return time, abfluss