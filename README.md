# Smart_recipe_generator

Overview
The "Smart Recipe Generator" is a command-line tool that allows users to search for recipes based on ingredients or keywords. The program reads a dataset of recipes and provides relevant results, which can be saved as JSON files for later use.

# Features
- Load a dataset of recipes from a CSV file
- Search for recipes using:
  - Ingredients (comma-separated input)
  - Keywords in the title or instructions
- Save search results in JSON format
- Simple command-line interface for user interaction

# Prerequisites
- Python 3.x
- Required Python libraries:
  - "pandas"
  - "json"

# Installation
1. Ensure you have Python 3 installed.
2. Install the required dependencies using pip:
    " pip install pandas "
3. Place the recipe dataset (13k-recipes.csv) in the appropriate directory.
4. Modify the file path in smart_recipe_system.py accordingly:
   file_path = "set_your_file_path_here"  # Change this to the correct path

# Usage
1. Run the script:
    python smart_recipe_system.py
  
2. Choose an option:
   - 1: Search by ingredients (enter ingredients separated by commas)
   - 2: Search by keyword (enter a keyword to find recipes related to it)
   - 3: Exit the program

3. If recipes are found, they will be displayed in the terminal and saved as JSON files in the specified directory:
   - ingredient_search_results.json
   - keyword_search_results.json

# Customization
- Change Output Directory: Modify the 'output_path' in the 'save_to_json' function to specify where the JSON files should be saved.
   output_path = " your_file_path "  # Change this if needed
 
- Update Dataset Path: Ensure 'file_path' is correctly set to the location of '13k-recipes.csv'.

# Limitations
- The dataset file must contain columns 'Title', 'Ingredients', 'Instructions', and 'Cleaned_Ingredients'.
- The search functionality is case-insensitive but may not handle complex ingredient combinations perfectly.

# Future Enhancements
- Add a web-based UI for better user experience
- Implement filtering options (e.g., dietary restrictions, cuisine types)
- Improve ingredient matching using NLP techniques

# License
This project is open-source and available for modification and distribution.

# Author
Created by  [ Akshay N.M , Bhuvan.D , Jeevanmay M.S , Tharun.M ]

