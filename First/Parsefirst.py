import requests
from bs4 import BeautifulSoup

def site_parsing():
    all_urls = []

    url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops/'
    
    try:
        response = requests.get(url)   
        response.raise_for_status()  # Checking for an error when receiving a response
    except requests.exceptions.RequestException as e:
        print("Failed to connect to the site:", url)
        print("Error:", str(e))
        return all_urls
    
    soup = BeautifulSoup(response.text, 'lxml')

    for link in soup.find_all('a', class_='title'):
        href = link.get('href')
        
        if href.startswith('/'):  # If the relative path starts with a slash
            full_url = f"https://webscraper.io{href}"
            all_urls.append(full_url)

    return all_urls