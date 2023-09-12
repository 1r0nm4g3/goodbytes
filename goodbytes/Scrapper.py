import requests
import csv
from bs4 import BeautifulSoup as bs

from goodbytes.Recipe import Recipe

class Scrapper:
    def __init__(self, sitemap_url, output_filename='scrapper_results.csv') -> None:
        self.sitemap_url = sitemap_url
        self.output_filename = output_filename
        self.sitemap_urls = self.get_sitemap()
        self.recipe_urls = self.get_recipe_urls(self.sitemap_urls[0])
        self.create_csv_file()

    def get_sitemap(self):
        sitemap = requests.get(self.sitemap_url)
        sitemap_soup = bs(sitemap.text, features='xml')
        sitemap_urls = [url.text for url in sitemap_soup.find_all('loc')]
        return sitemap_urls

    def get_recipe_urls(self, sitemap_url):
        sitemap = requests.get(sitemap_url)
        sitemap_soup = bs(sitemap.text, features='xml')
        recipe_urls = [url.text for url in sitemap_soup.find_all('loc') if '/recipe/' in url.text]
        return recipe_urls

    def create_csv_file(self):
        with open(self.output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            row = ['Recipe Name', 'Rating', 'Reviews', 'Ingredients', 'Directions', 'URL', 'Calories', 'Fat', 'Carbs', 'Protein']

            writer.writerow(row)

    def add_recipe_to_csv(self, recipe_url):
        try:
            recipe = Recipe(recipe_url)
            with open(self.output_filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)

                row = [recipe.recipe_name, recipe.rating, recipe.reviews, recipe.ingredients, recipe.directions, recipe.url, recipe.calories, recipe.fat, recipe.carbs, recipe.protein]

                writer.writerow(row)
        except KeyboardInterrupt:
            exit()
        except:
            pass

    def parse(self, i=None):
        if i:
            for j in range(0, i):
                self.add_recipe_to_csv(self.recipe_urls[j])
        else:
            for recipe_url in self.recipe_urls:
                self.add_recipe_to_csv(recipe_url)

if __name__ == '__main__':
    sitemap_url = 'https://www.allrecipes.com/sitemap.xml'
    scrapper = Scrapper(sitemap_url)
    scrapper.parse()