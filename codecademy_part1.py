import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URL de la page à scraper
url = 'https://content.codecademy.com/courses/beautifulsoup/cacao/index.html'

# Faire la requête HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Localiser le tableau et extraire les données
table = soup.find('table', {'id': 'cacaoTable'})
rows = table.find_all('tr')

# Extraction des colonnes « Cocoa Percent » et « Rating »
cocoa_percents = []
ratings = []

# Parcourir chaque ligne du tableau et récupérer les valeurs des colonnes
for row in rows[1:]:  # Ignorer la première ligne d'en-tête
    cols = row.find_all('td')
    if len(cols) > 4:  # S'assurer que la ligne a le nombre de colonnes attendu
        cocoa_percent = cols[4].get_text(strip=True).replace('%', '')  # Retirer le symbole %
        rating = cols[2].get_text(strip=True)

        # Convertir les valeurs en float pour faciliter l'analyse
        cocoa_percents.append(float(cocoa_percent))
        ratings.append(float(rating))


# Création du DataFrame
data = {
    "Cocoa Percent": cocoa_percents,
    "Rating": ratings
}
df = pd.DataFrame(data)

# Exportation en CSV
df.to_csv("./scraped_files/csv/chocolate_ratings.csv", index=False)

# Exportation en JSON avec différents paramètres `orient`
df.to_json("./scraped_files/json/chocolate_ratings_index.json", orient="index")
df.to_json("./scraped_files/json/chocolate_ratings_records.json", orient="records")
df.to_json("./scraped_files/json/chocolate_ratings_values.json", orient="values")
