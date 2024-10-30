
Restaurant Recommendation Software
This repository contains a simple restaurant recommendation software written in Python. The software allows users to search for restaurants based on their preferences for cuisine type and price range.

Project Objectives
Store data in a data structure

Use an algorithm to sort or search for data within a data structure.

Use Git version control.

Use the command line and file navigation.

Write a technical blog post on the project.

Installation
Clone the repository:

sh

Copy
git clone https://github.com/yourusername/restaurant-recommendation.git
Navigate to the project directory:

sh

Copy
cd restaurant-recommendation
Usage
Run the main.py script:

sh

Copy
python main.py
Enter your preferred cuisine type and price range when prompted:


Copy
Enter your preferred cuisine (e.g., Italian, Japanese): 
Enter your preferred price range (e.g., $, $$): 
Code
python

Copy
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
Contributing
Feel free to fork this repository, submit issues and pull requests, or suggest new features!

License
This project is licensed under the MIT License.
