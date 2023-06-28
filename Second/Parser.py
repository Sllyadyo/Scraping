import requests
from bs4 import BeautifulSoup

def parse_data():
    url = 'https://www.tiobe.com/tiobe-index/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Checking the success of the request
    except requests.exceptions.RequestException as e:
        print("Failed to connect to the site:", str(e))
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table')  # Find the table on the page

    if not table:
        print("The table was not found on the page")
        return None

    rows = table.find_all('tr')  # Find all rows of the table
    
    allRating = []  # List for all rows of the table 

    for row in rows[1:]:  # Skip the first line of headers
        cols = row.find_all('td')        

        if len(cols) == 7:  
            rating = {
                'Apr 2023': cols[0].text.strip(),
                'Apr 2022': cols[1].text.strip(),
                'Programming Language': cols[4].text.strip(),
                'Ratings': cols[5].text.strip(),
                'Change': cols[6].text.strip()
            }
            allRating.append(rating)

    return allRating
