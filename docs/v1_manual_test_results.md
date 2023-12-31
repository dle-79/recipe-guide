# Example workflow
Theresa wants to try a paleo diet, but doesn’t know what to make. She first adds all the ingredients she has at home to her virtual pantry. She then restricts the recipes she can give to be paleo friendly. She then receives a recipe and starts to use the ingredients. When Theresa makes it, she removes the ingredients used from her virtual pantry.

- Theresa starts by creating a new user by calling /user/create_user
- Theresa starts by calling POST /fridge/add_ingredients to add all the ingredients she has to her virtual fridge.
- then Theresa calls POST /recipe/get_recipe_macros with her paleo diet restrictions.
- She then calls POST /fridge/remove_fridge_ingredients_fridge_remove_repice_ingredients_post in order to remove the recipes from her virtual fridge.

# Testing results
1. Theresa user is created 
curl -X 'POST' \
  'https://recipe-guide.onrender.com/user/create_user' \
  -H 'accept: application/json' \
  -H 'access_token: recipe' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Theresa"
}'

2. Return:
   {
     user_id : 14
   }

4. Adds all her ingredents to her virtual fridge
curl -X 'POST' \
  'https://recipe-guide.onrender.com/fridge/add_ingredients?ingredient_id=25' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": 14,
  "quantity": 3
}'

Return: "Added ingredient"

curl -X 'POST' \
  'https://recipe-guide.onrender.com/fridge/add_ingredients?ingredient_id=11' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": 14,
  "quantity": 3
}'

Return: "Added ingredient"

curl -X 'POST' \
  'https://recipe-guide.onrender.com/fridge/add_ingredients?ingredient_id=12' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_id": 14,
  "quantity": 5
}'

Return: "Added ingredient"

4. Restrict for paleo and get a recipe back
curl -X 'POST' \
  'http://127.0.0.1:8000/recipe/get_recipe?user_id=2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "protein": 0,
  "calories": 0,
  "vegan": true,
  "vegetarian": true,
  "paleo": true,
  "carbs": 0,
  "servings": 0,
  "time_to_make": 0
}'

Response:
[
  {
    "recipe_id": 4,
    "sku": "BAKED_BRUSSEL_SPROUT_CHIPS_0",
    "name": "Baked_Brussels_Sroupt_Chips",
    "steps": "1. Preheat oven to 350°F.\n2. Using a small knife, cut the bottom of a Brussels sprout off so that a few of the outer leaves fall off. Place the separated leaves into a medium bowl. Repeat until all the Brussels sprouts have been cut and leaves have been removed.\n3. Once you peel all the Brussels sprouts, toss the leaves with a small drizzle of olive oil and sea salt and layer them on a baking sheet in a single layer.\n4. Bake the Brussels sprout leaves for 4-6 minutes or until the tips are lightly browned and the leaves are crispy. Watch them carefully so they don’t burn!"
  }
]

5. Check to make sure we have the correct ingredients
curl -X 'POST' \
  'https://recipe-guide.onrender.com/recipe/check_recipe_ingredient?user_id=14&recipe_id=4&servings=1' \
  -H 'accept: application/json' \
  -d ''

Response:
"true"

