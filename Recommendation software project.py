restaurants = [
    {"name": "Sushi Place", "cuisine": "Japanese", "rating": 4.5, "price": "$$"},
    {"name": "Pizza Palace", "cuisine": "Italian", "rating": 4.0, "price": "$"},
    {"name": "Burger Joint", "cuisine": "American", "rating": 4.2, "price": "$"},
    {"name": "Taco Town", "cuisine": "Mexican", "rating": 4.8, "price": "$$"},
    {"name": "Pasta House", "cuisine": "Italian", "rating": 4.1, "price": "$$"},
    # Add more restaurant data as needed
]

def search_restaurants(restaurants, cuisine=None, price=None):
    results = []
    for restaurant in restaurants:
        if cuisine and restaurant["cuisine"] != cuisine:
            continue
        if price and restaurant["price"] != price:
            continue
        results.append(restaurant)
    return results

# Example usage:
cuisine_preference = input("Enter your preferred cuisine (e.g., Italian, Japanese): ")
price_preference = input("Enter your preferred price range (e.g., $, $$): ")
recommended_restaurants = search_restaurants(restaurants, cuisine_preference, price_preference)

print("\nRecommended Restaurants:")
for r in recommended_restaurants:
    print(f"Name: {r['name']}, Cuisine: {r['cuisine']}, Rating: {r['rating']}, Price: {r['price']}")
