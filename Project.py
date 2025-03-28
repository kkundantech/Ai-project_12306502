import requests
import time

# Conversion Rate (1 USD = 83 INR)
USD_TO_INR = 86 

# ANSI escape codes for color formatting
GREEN = "\033[92m"
BLUE = "\033[94m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

PRODUCT_CATEGORIES = {
    "men's clothing": ["Shirt", "Trousers", "Jacket", "Jeans"],
    "women's clothing": ["Dress", "Skirt", "Saree", "Jeans"]
}

PRODUCT_OPTIONS = {
    "Shirt": ["Polo", "Full Sleeves", "Half Sleeves", "Casual"],
    "Trousers": ["Chinos", "Cargo", "Formal", "Joggers"],
    "Dress": ["Evening", "Casual", "Maxi"],
    "Jeans": ["Skinny", "Straight", "Bootcut"]
}

SIZES = ["XS", "S", "M", "L", "XL", "XXL"]

def fetch_sustainable_products(category):
    """Fetch sustainable clothing products from the API based on category."""
    category = category.lower().replace(" ", "%20")  # URL encoding
    url = f"https://fakestoreapi.com/products/category/{category}"

    print(f"{BLUE}🔍 Searching for products in '{category.replace('%20', ' ')}' category...{RESET}")
    time.sleep(1)  # Simulating loading time

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not data:
            return {"error": f"No products found in '{category.replace('%20', ' ')}' category."}
        return data

    except requests.exceptions.RequestException as e:
        return {"error": f"⚠️ Failed to fetch products: {str(e)}"}

def convert_price_to_inr(price_usd):
    """Convert USD price to INR."""
    return round(price_usd * USD_TO_INR, 2)

def get_user_preferences():
    """Get user preferences for a better shopping experience."""
    while True:
        print("\n👕 Please choose a category:")
        for i, category in enumerate(PRODUCT_CATEGORIES.keys(), start=1):
            print(f"{YELLOW}{i}. {category.title()}{RESET}")
        choice = input("👉 Enter your choice: ").strip()

        if choice in ["1", "2"]:
            category = list(PRODUCT_CATEGORIES.keys())[int(choice) - 1]
            break
        else:
            print(f"{RED}❌ Invalid choice! Please enter 1 or 2.{RESET}")
    
    while True:
        print("\n🛍️ What product are you looking for?")
        for i, product in enumerate(PRODUCT_CATEGORIES[category], start=1):
            print(f"{YELLOW}{i}. {product}{RESET}")
        choice = input("👉 Enter your choice: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(PRODUCT_CATEGORIES[category]):
            product = PRODUCT_CATEGORIES[category][int(choice) - 1]
            break
        else:
            print(f"{RED}❌ Invalid choice! Please enter a valid option.{RESET}")
    
    if product in PRODUCT_OPTIONS:
        while True:
            print("\n👕 What type of", product, "do you prefer?")
            for i, option in enumerate(PRODUCT_OPTIONS[product], start=1):
                print(f"{YELLOW}{i}. {option}{RESET}")
            choice = input("👉 Enter your choice: ").strip()

            if choice.isdigit() and 1 <= int(choice) <= len(PRODUCT_OPTIONS[product]):
                product_type = PRODUCT_OPTIONS[product][int(choice) - 1]
                break
            else:
                print(f"{RED}❌ Invalid choice! Please enter a valid option.{RESET}")
    else:
        product_type = "Any"
    
    while True:
        print("\n📏 What size do you prefer?")
        for i, size in enumerate(SIZES, start=1):
            print(f"{YELLOW}{i}. {size}{RESET}")
        choice = input("👉 Enter your choice: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(SIZES):
            size = SIZES[int(choice) - 1]
            break
        else:
            print(f"{RED}❌ Invalid choice! Please enter a valid option.{RESET}")
    
    while True:
        min_price = input("💰 Enter minimum price (in ₹): ").strip()
        max_price = input("💰 Enter maximum price (in ₹): ").strip()
        if min_price.isdigit() and max_price.isdigit() and int(min_price) <= int(max_price):
            min_price, max_price = int(min_price), int(max_price)
            break
        else:
            print(f"{RED}❌ Invalid price range! Please enter valid numbers.{RESET}")
    
    return category, product, product_type, size, min_price, max_price

def display_recommendations(recommendations, min_price, max_price):
    """Display the recommended products in a structured format."""
    print(f"\n{GREEN}============================================")
    print("      🌿 Sustainable Clothing Picks 🛍️     ")
    print("============================================\n")

    filtered = [p for p in recommendations if min_price <= convert_price_to_inr(p['price']) <= max_price]
    
    if filtered:
        for product in filtered:
            price_inr = convert_price_to_inr(product['price'])
            print(f"🔹 {YELLOW}{product['title']}{RESET}")
            print(f"   💰 Price: ₹{price_inr}")
            print(f"   🏷️ Description: {product.get('description', 'No description available.')[:100]}...")
            print("--------------------------------------------")
            time.sleep(0.5)
    else:
        print(f"{RED}❌ No products found within your price range.{RESET}")

def main():
    """Main function to interact with the user."""
    print(f"\n{GREEN}============================================")
    print("  🎯 Welcome to the AI Ethical Fashion Assistant!")
    print("  Helping you shop sustainably 🌱")
    print("============================================{RESET}\n")

    category, product, product_type, size, min_price, max_price = get_user_preferences()

    products = fetch_sustainable_products(category)
    
    if "error" in products:
        print(f"{RED}❌ {products['error']}{RESET}")
    else:
        display_recommendations(products, min_price, max_price)

    print(f"{GREEN}👋 Thank you for using the Ethical Fashion Assistant!{RESET}")

if _name_ == "_main_":
    main()