from random import randint
import string
import random
import sqlalchemy
from src import database as db
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from src.api import auth


#insert ingredients into recipe
for i in range(1, 2031+1):
    num_ingredients = randint(5, 20)
    ingredients = []
    while len(ingredients) < num_ingredients:
        ingredient_id = randint(1, 1662)
        if ingredient_id not in ingredients:
            ingredients.append(ingredient_id)
    
    for h in range(len(ingredients)):
        quantity = randint(1, 10)

        with db.engine.begin() as connection:
            connection.execute(sqlalchemy.text("""
            INSERT INTO recipe_ingredients(recipe_id, ingredient_id, quantity, purchase)
            VALUES (:user_id, :ingredient, :amount_needed, False)
            """),
            [{"user_id": i,
            "ingredient": ingredients[h],
            "amount_needed": quantity}])


#add users

for i in range(1, 13001):
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for j in range(10))
    print(username)

    with db.engine.begin() as connection:
            connection.execute(sqlalchemy.text("""
            INSERT INTO users(name)
            VALUES (:name)
            """),
            [{"name": username}])

#add reviews to table

one_star = ["Horrible", "Awful", "Dreadful", "Abominable", "Atrocious", "Repugnant", "Ghastly", "Appalling", "Frightful", "Deplorable", "Disastrous", "Lamentable", "Miserable", "Hateful", "Wretched", "Execrable", "Detestable", "Loathsome", "Unpleasant", "Offensive", "Repulsive", "Unspeakable", "Odious", "Despicable", "Disgusting", "Abysmal", "Terrible", "Infernal", "Ghastly", "Dire", "Egregious", "Gruesome", "Intolerable", "Sickening", "Monstrous", "Vile", "Disconcerting", "Aberrant", "Nauseating", "Revolting", "Nasty", "Fearsome", "Dismal", "Shocking", "Repellant", "Unbearable", "Oppressive", "Execrable", "Forlorn", "Abhorrent"]
two_star = ["Poor", "Substandard", "Inferior", "Deficient", "Mediocre", "Lousy", "Unsatisfactory", "Faulty", "Flawed", "Unacceptable", "Unsuitable", "Second-rate", "Amateurish", "Inadequate", "Dismal", "Miserable", "Abysmal", "Dreadful", "Terrible", "Awful", "Horrible", "Unfavorable", "Adverse", "Negative", "Detrimental", "Deleterious", "Harmful", "Damaging", "Unpleasant", "Displeasing", "Disappointing", "Unpleasant", "Inferior", "Defective", "Shoddy", "Crummy", "Rotten", "Wretched", "Sloppy", "Faulty", "Subpar", "Underwhelming", "Unsatisfying", "Regrettable", "Catastrophic", "Haphazard", "Insufficient", "Insatisfactory", "Unworthy"]
three_star = ["Satisfactory", "Acceptable", "Adequate", "Fine", "Passable", "Tolerable", "Decent", "Sufficient", "Average", "Fair", "Reasonable", "O.K.", "Good enough", "Mediocre", "So-so", "All right", "Fairly good", "Moderate", "Not bad", "Halfway decent", "Middle-of-the-road", "Plain", "Run-of-the-mill", "Common", "Ordinary", "Usual", "Routine", "Standard", "Middling", "Intermediate", "Moderately good", "Serviceable", "Inoffensive", "Mild", "Neutral", "Lukewarm", "Meh", "Not great", "Ho-hum", "Passing", "Indifferent", "Unremarkable", "Inadequate", "Bearable", "Fine and dandy", "Just okay", "Fair enough", "Not too shabby"]
four_star = ["Excellent", "Superb", "Outstanding", "Exceptional", "Marvelous", "Wonderful", "Terrific", "Fantastic", "Splendid", "Great", "Fine", "First-rate", "Top-notch", "Superior", "Prime", "High-quality", "Quality", "Exemplary", "Top-quality", "Impressive", "Commendable", "Worthy", "Noteworthy", "Good-quality", "Praiseworthy", "Admirable", "Capable", "Skilled", "Competent", "Proficient", "Talented", "Skillful", "Adept", "Dexterous", "A1", "Ace", "Brilliant", "Super", "Fine", "Admirable", "Satisfactory", "Solid", "Decent", "Good enough", "Passable", "Sufficient", "Up to par", "Acceptable", "Reputable", "Desirable"]
five_star = ["Incredible", "Astounding", "Stunning", "Breathtaking", "Astonishing", "Mind-blowing", "Remarkable", "Extraordinary", "Unbelievable", "Phenomenal", "Fantastic", "Spectacular", "Marvellous", "Wondrous", "Jaw-dropping", "Outstanding", "Sublime", "Incomparable", "Unparalleled", "Exceptional", "Transcendent", "Magnificent", "Miraculous", "Prodigious", "Wondrous", "Dazzling", "Splendid", "Inspirational", "Awesome", "Grand", "Superb", "Supreme", "Peerless", "Breathtaking", "Sensational", "Unreal", "Ineffable", "Divine", "Awe-inspiring", "Overwhelming", "Awe-striking", "Stupendous", "Epic", "Glorious", "Majestic", "Ethereal", "Inexpressible", "Overpowering", "Incredible"]

for i in range(1, 2031+2):
    num_reviews = randint(5, 300)
    user_ids = []
    while len(user_ids) < num_reviews:
        user_id = randint(1, 13000)
        if user_id not in user_ids:
            user_ids.append(user_id)
    for h in range(num_reviews):
        rating = randint(1, 5)
        review_description_num = randint(0, 49)
        review = ""
        if rating == 1:
            review = one_star[review_description_num]
        elif rating == 2:
            review = two_star[review_description_num]
        elif rating == 3:
            review = three_star[review_description_num]
        elif rating == 4:
            review = four_star[review_description_num]
        else:
            review = five_star[review_description_num]

        with db.engine.begin() as connection:
            connection.execute(sqlalchemy.text("""
            INSERT INTO review(recipe_id, rating, review_description, user_id)
            VALUES (:recipe_id, :rating, :review_description, :user_id)
            """),
            [{"user_id": user_ids[h],
            "rating": rating,
            "review_description": review,
            "recipe_id": i}])

#fridge
for i in range(1, 13001):
    num_fridge = randint(10, 50)
    fridge_items = []
    while len(fridge_items) < num_fridge:
        ingredient = randint(1, 13000)
        if ingredient not in fridge_items:
            user_ids.append(ingredient)
    for h in range(len(fridge_items)):
        quant = randint(0, 20)
    with db.engine.begin() as connection:
            connection.execute(sqlalchemy.text("""
            INSERT INTO fridge(ingrdient_id, user_id, quantity)
            VALUES (:ingredient_id, :user_id, :quantity)
            """),
            [{"user_id": i,
            "ingredient_id": fridge_items[h],
            "quantity": quant}])

#shopping_list
for i in range(1, 13001):
    num_shop= randint(10, 30)
    shop_items = []
    while len(shop_items) < num_shop:
        ingredient = randint(1, 13000)
        if ingredient not in shop_items:
            user_ids.append(ingredient)
    for h in range(len(shop_items)):
        quant = randint(0, 10)
    with db.engine.begin() as connection:
            connection.execute(sqlalchemy.text("""
            INSERT INTO shopping_list(ingrdient_id, user_id, quantity)
            VALUES (:ingredient_id, :user_id, :quantity)
            """),
            [{"user_id": i,
            "ingredient_id": shop_items[h],
            "quantity": quant}])
    


        
        




    