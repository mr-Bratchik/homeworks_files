from pprint import pprint
def parse_recipes(file_path):
    recipes = {}
    current_recipe = None

    with open(file_path) as file:
        for line in file:
            line = line.strip()

            if not line:
                # Пустая строка(конец текущего рецепта)
                current_recipe = None
                continue

            if '|' not in line and not line.isdigit():
                # Название рецепта
                current_recipe = line
                recipes[current_recipe] = []
            elif line:
                # Ингредиенты
                ingredients = {}
                parts = line.split('|')
                if len(parts) == 3:
                    recipes_parts = []
                    for part in parts:
                        recipes_part = part.strip()
                        recipes_parts.append(recipes_part)
                    ingredients['ingredient_name'] = recipes_parts[0]
                    ingredients['quantity'] = recipes_parts[1]
                    ingredients['measure'] = recipes_parts[2]
                    if current_recipe:
                        recipes[current_recipe].append(ingredients)

    return recipes


def get_shop_list_by_dishes(dishes, person_count):
    file_path = 'recipes.txt'
    cook_book = parse_recipes(file_path)
    product_list = {}
    if dishes and person_count:
        for dish in dishes:
            value = cook_book.get(dish)
            if value:
                for product in value:
                    ingredient_name = product['ingredient_name']
                    quantity = int(product['quantity']) * person_count  # умножаем количество на количество персон
                    measure = product['measure']
                    if not ingredient_name in product_list:
                        product_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
                    else:
                        product_list[ingredient_name]['quantity'] += quantity  # складываю в случае повторения продуктов



            else:
                return f'Блюда {dish} нет в кулинарной книге'
    return pprint(product_list)

if __name__ == '__main__':
    get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
