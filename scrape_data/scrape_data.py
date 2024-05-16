import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape_brown_dwarfs():
    # Make a page request using the requests module.
    url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get all the tables of the page using find_all() method
    tables = soup.find_all('table', {'class': 'wikitable'})
    table = tables[2]  # The third table

    # Create an empty list.
    scraped_data = []

    # Get all the <tr> tags from the table
    rows = table.find('tbody').find_all('tr')

    # For loop to take out all the <td> tags
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        if len(cols) >= 5:  # Ensure there are enough columns
            # Keep all the <td> rows in the empty list made earlier
            scraped_data.append(cols)

    return scraped_data

if __name__ == "__main__":
    data = scrape_brown_dwarfs()

    # Define the columns (you may need to adjust these based on the actual table structure)
    columns = ["Name", "Constellation", "Right Ascension", "Declination", "Distance", "Spectral Type", "Mass", "Radius", "Discovery Year"]

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Save to CSV
    df.to_csv('dwarf_stars.csv', index=False)

    print("Data saved to dwarf_stars.csv")

