from bs4 import BeautifulSoup
import requests

def get_info():
    # Station Reuss - Mellingen - 2018
    html_text = requests.get("https://www.hydrodaten.admin.ch/de/2018.html").text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', class_= 'table table-bordered table-narrow')
    time = table.find('small', class_='text-muted').text
    flow_rate = table.find('td', class_='text-center').text
    water_level = table.find('td', class_='text-center').findNext('td', class_='text-center').text
    temperature = table.find('td', class_='text-center').findNext('td', class_='text-center').findNext('td', class_='text-center').text

  
    
    return time, flow_rate, water_level, temperature