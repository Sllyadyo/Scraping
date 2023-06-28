import requests
from bs4 import BeautifulSoup

def OneUrlScrap(url):
    notebook = {'name': '', 'description': '', 'price': ''}
    
    try:
        response = requests.get(url)   
    except requests.exceptions.RequestException as e:
        print("Failed to connect to the site:", url)
        print("Error:", str(e))
        return notebook

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Name
    name_element = soup.find('h4', class_='')
    if name_element:
        notebook['name'] = name_element.text.strip() 

     # Description  
    description_element = soup.select_one('p.description')
    notebook['description'] = description_element.text.strip() if description_element else "Description not available"

     # Price
    price_element = soup.select_one('h4.price')
    notebook['price'] = price_element.text.strip() if price_element else "The price is not specified"

    return notebook
 
