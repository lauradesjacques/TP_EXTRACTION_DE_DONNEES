import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la page à scraper
url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'

# Faire la requête HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver le tableau des statistiques
table = soup.find('table', {'id': 'per_game_stats'})

# Extraire les en-têtes
headers = []
for th in table.find('thead').find_all('th'):
    headers.append(th.text)


# Extraire les lignes de données
data = []
for row in table.find_all('tr')[1:]: # Ignorer la première ligne (en-tête)
    cols = row.find_all(['th','td'])
    if cols:  # S'assurer que la ligne contient des données
        data.append([col.text for col in cols])


# Créer un DataFrame
df = pd.DataFrame(data=data, columns=headers)

# Exporter le DataFrame en CSV
df.to_csv('./scraped_files/csv/NBA_player_stats_2022.csv', index=False)

