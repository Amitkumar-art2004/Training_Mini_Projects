
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Check connection
if response.status_code == 200:
    print("Website connected successfully")
else:
    print("Failed to connect")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Empty list for storing data
book_data = []

for book in books:

    # Title
    title = book.h3.a["title"]

    # Price
    price = book.find(
        "p", 
        class_="price_color"
    ).text

    # Rating
    rating = book.p["class"][1]

    # Store in dictionary
    data = {
        "Title": title,
        "Price": price,
        "Rating": rating
    }

    book_data.append(data)


# Convert list to DataFrame
df = pd.DataFrame(book_data)

# Save to CSV
df.to_csv(
    "books_data.csv",
    index=False
)
print("Data saved successfully!")

print(df.head())
