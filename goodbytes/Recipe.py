import requests
from bs4 import BeautifulSoup as bs
import re

def strip_line_breaks(text):
    text = text.replace('\n', '')
    text = text.replace('\r', '')
    return text

class Ingredient:
    def __init__(self, quantity, unit, name) -> None:
        self.quantity = quantity
        self.unit = unit
        self.name = name
    
    def __repr__(self) -> str:
        return f'{self.quantity} {self.unit} {self.name}'

def create_ingredient(soup):
    quantity = soup.find('span', {'data-ingredient-quantity': 'true'}).text if soup.find('span', {'data-ingredient-quantity': 'true'}) else None
    unit = soup.find('span', {'data-ingredient-unit': 'true'}).text if soup.find('span', {'data-ingredient-unit': 'true'}) else None
    name = soup.find('span', {'data-ingredient-name': 'true'}).text if soup.find('span', {'data-ingredient-name': 'true'}) else None

    return Ingredient(quantity, unit, name)

class Recipe:
    def __init__(self, url) -> None:
        self.url = url
        self.soup = self._get_soup(url)

    def __repr__(self) -> str:
        return f'Recipe: {self.recipe_name}\nRating: {self.rating} ({self.reviews})\nIngredients: {self.ingredients}\nDirections: {self.directions}'

    def _get_soup(self, url=None):
        response = requests.get(url) if url else requests.get(self.url)
        self.soup = bs(response.text, 'html.parser')
        self._get_recipe()
        return self.soup

    def _get_recipe_name(self):
        self.recipe_name = self.soup.find('h1', {'id': 'article-heading_1-0'}).text
        self.recipe_name = strip_line_breaks(self.recipe_name)
        return self.recipe_name
    
    def _get_rating(self):
        rating = self.soup.find('div', {'id': 'mntl-recipe-review-bar__rating_1-0'})
        self.rating = strip_line_breaks(rating.text)
        return self.rating
    
    def _get_reviews(self):
        reviews = self.soup.find('div', {'id': 'mntl-recipe-review-bar__rating-count_1-0'})
        reviews = re.sub('[^0-9]', '', reviews.text)
        self.reviews = reviews
        return reviews
    
    def _get_ingredients(self):
        ingredients = self.soup.find_all('li', {'class': 'mntl-structured-ingredients__list-item'})
        self.ingredients = [create_ingredient(ingredient) for ingredient in ingredients]
        return self.ingredients
    
    def _get_directions(self):
        steps = self.soup.find('div', {'id': 'recipe__steps-content_1-0'})
        self.directions = strip_line_breaks(steps.text)
        return self.directions
    
    def _get_recipe(self):
        self._get_rating()
        self._get_reviews()
        self._get_recipe_name()
        self._get_ingredients()
        self._get_directions()

if __name__ == '__main__':
    url = 'https://www.allrecipes.com/crockpot-italian-chicken-recipe-7501402'
    test_recipe = Recipe(url)
    print(test_recipe)