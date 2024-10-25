# 🛠️ TP : EXTRACTION DE DONNEES

Les données représentent une véritable richesse, à condition de savoir où et comment les dénicher.
L'objectif de ce brief est d'explorer la pratique du scraping, une technique permettant d'extraire automatiquement des données publiques habituellement accessibles à la consultation humaine.

---

## 📋 Contexte du projet

Votre entreprise souhaite obtenir des informations sur la concurrence afin d'optimiser sa stratégie globale, et plus spécifiquement sa stratégie sur les prix. Ne disposant actuellement d'aucune donnée à ce sujet, vous avez entrepris de monter sur cette compétence afin de proposer à votre manager de faire du scraping.

---

## 📚 Ressources Utiles

- <a href="https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296776-extrayez-et-transformez-des-donnees-avec-lextraction-web" target="_blank">Course</a>
- <a href="https://proxiesapi.com/articles/the-complete-beautifulsoup-cheatsheet-with-examples" target="_blank">BeautifulSoup</a>
- <a href="https://proxiesapi.com/articles/web-scraping-in-python-the-complete-guide" target="_blank">Web Scraping with python</a>
- <a href="https://www.selenium.dev/documentation/overview/" target="_blank">Selenium Overview</a>

---

## ⚙️ Consignes

### 🎯 **Réaliser une veille sur le scraping**

1. **Cas d’utilisation**
2. **Outils**
3. **Processus du Scraping**
4. **Difference BeautifulSoup et Selenium**

---

### 🗂️ **Partie 1 : Prise en main Scraping avec BeautifulSoup**

Outils : **Python**, **BeautifulSoup**, **Request**.

Pour la prise en main de **BeautifulSoup** je vous propose un ensemble de cas pratiques simples (voir fichier pdf).

Pour chacun de ces cas, vous devez rechercher l'organisation **HTML** du site, et notamment les **noms et type de balise** permettant de repérer les informations utiles. Ecrire un script python qui récupère des informations par scraping

​
Allé plus loin en explorant des sites plus complexes...

Remarque : Vous pouvez scrapper "n'importe" quel site Internet que vous pouvez consulter, mais la difficulté de cette opération dépend du site. D'autres exemples de sites :
- http://books.toscrape.com/
- https://realpython.github.io/fake-jobs/
- https://www.gov.uk


---

### 🗂️ **Partie 2 : Scraping Dynamique avec Selenium**

Outils : **Python**, **Selenium**.

Utiliser **Selenium** pour extraire des données sur un site dynamique.

Exemple site : https://www.adamchoi.co.uk/overs/detailed. Ce site fournit des statistiques détaillées sur les matchs de football.

---

### 🗂️ **Partie 3 : Extraction de Données via une API**

Explorer l'**API publique** d'un service (par exemple, l’API d’OpenWeather pour récupérer des informations météo ou l'API GitHub pour obtenir des informations sur des repositories).

---

### 🗂️ **Partie 4 : Comparaison des Méthodes et Conclusion**

1. **Quand utilisé ces outils ?**
2.**Limites ?**
3.**Ethiques du scraping**
4.**Gestion des données personnelles et confidentialité.**

---

## 📦 Livrables

- Script bien documenté
