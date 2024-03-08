spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food["name"] for food in spicy_foods]
names = get_names(spicy_foods)
print(names)
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
cuisine = "Thai"
spicy_food = get_spicy_food_by_cuisine(spicy_foods, cuisine)
if spicy_food:
    print(spicy_food)
else:
    print(f"No spicy food found for cuisine: {cuisine}")

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


print_spiciest_foods(spicy_foods)
def average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)
    if num_foods == 0:
        return 0
    return total_heat_level // num_foods

average_heat = average_heat_level(spicy_foods)
print(average_heat)


def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods

new_food = {
    "name": "Spicy Ramen",
    "cuisine": "Japanese",
    "heat_level": 8,
}
updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(updated_spicy_foods)

    
