import unittest
from bs4 import BeautifulSoup as bs

from goodbytes.Recipe import Recipe, Ingredient

class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.allrecipes.com/crockpot-italian-chicken-recipe-7501402'
        self.recipe = Recipe(self.url)

    def test_recipe(self):
        self.assertEqual(self.recipe.recipe_name, 'Crockpot Italian Chicken')
        self.assertEqual(self.recipe.rating, '4.3')
        self.assertEqual(self.recipe.reviews, '31')
        self.assertEqual(len(self.recipe.ingredients), 3)
        self.assertEqual(self.recipe.ingredients[0].quantity, '1')
        self.assertEqual(self.recipe.ingredients[1].unit, 'cup')
        self.assertEqual(self.recipe.ingredients[2].name, 'boneless skinless chicken breasts')
        self.assertEqual(self.recipe.directions, 'Stir Italian dressing and Parmesan cheese together in a bowl.Place chicken in a slow cooker, and pour dressing mixture over chicken. Cover and cook on Low until chicken is tender, no longer pink in the center, and the juices run clear, about 8 hours.   Editor\'s Note:  Nutrition data for this recipe includes the full amount of Italian dressing. The actual amount of dressing consumed will vary.')
        self.assertEqual(self.recipe.calories, '506')
        self.assertEqual(self.recipe.fat, '31')
        self.assertEqual(self.recipe.carbs, '15')
        self.assertEqual(self.recipe.protein, '39')

if __name__ == '__main__':
    unittest.main()