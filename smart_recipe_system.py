import pandas as pd
import json

def load_dataset(file_path):
    """Load the recipe dataset."""
    df = pd.read_csv(file_path)
    return df

def search_by_ingredients(df, ingredients):
    """Find recipes that include the given ingredients."""
    ingredients = set(ingredients.lower().split(","))
    results = df[df["Cleaned_Ingredients"].apply(lambda x: any(ing in x.lower() for ing in ingredients))]
    return results[["Title", "Ingredients", "Instructions"]]

def search_by_keyword(df, keyword):
    """Find recipes by keyword in the title or instructions."""
    keyword = keyword.lower()
    results = df[df["Title"].str.lower().str.contains(keyword) | df["Instructions"].str.lower().str.contains(keyword)]
    return results[["Title", "Ingredients", "Instructions"]]

def save_to_json(results, filename):
    """Save the search results to a JSON file."""
    if not results.empty:
        output_path = r"C:\Users\nmaks\Downloads"  # Change this if needed
        full_path = f"{output_path}\\{filename}"
        results.to_json(full_path, orient="records", indent=4)
        print(f"Results saved to {full_path}")
    else:
        print("No recipes found to save.")

def main():
    file_path = r"C:\Users\nmaks\Downloads\13k-recipes.csv"  # Adjust the path if needed
    df = load_dataset(file_path)

    while True:
        print("\nSmart Recipe Generator")
        print("1. Search by ingredients")
        print("2. Search by keyword")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            ingredients = input("Enter ingredients (comma-separated): ")
            results = search_by_ingredients(df, ingredients)
            print(results if not results.empty else "No recipes found.")
            save_to_json(results, "ingredient_search_results.json")
        
        elif choice == "2":
            keyword = input("Enter a keyword: ")
            results = search_by_keyword(df, keyword)
            print(results if not results.empty else "No recipes found.")
            save_to_json(results, "keyword_search_results.json")
        
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
