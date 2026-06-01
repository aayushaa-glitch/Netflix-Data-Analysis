import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("Dataset Loaded Successfully!")
print("Rows and Columns:", df.shape)

# Clean missing values
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["listed_in"] = df["listed_in"].fillna("Unknown")

# 1. Movies vs TV Shows
type_counts = df["type"].value_counts()

plt.figure(figsize=(7, 5))
type_counts.plot(kind="bar")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/movies_vs_tvshows.png")
plt.show()

# 2. Top 10 Genres
genres = df["listed_in"].str.split(", ").explode()
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10, 6))
top_genres.plot(kind="bar")
plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/top_genres.png")
plt.show()

# 3. Top 10 Countries
countries = df["country"].str.split(", ").explode()
top_countries = countries.value_counts().head(10)

plt.figure(figsize=(10, 6))
top_countries.plot(kind="bar")
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/top_countries.png")
plt.show()

# 4. Release Year Trend
release_trend = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(12, 6))
release_trend.plot(kind="line")
plt.title("Netflix Content Release Trend by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("charts/release_year_trend.png")
plt.show()

# 5. Top 10 Ratings
rating_counts = df["rating"].value_counts().head(10)

plt.figure(figsize=(10, 6))
rating_counts.plot(kind="bar")
plt.title("Top 10 Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/top_ratings.png")
plt.show()

# Print insights
print("\nKEY INSIGHTS")
print("1. Netflix has more Movies than TV Shows.")
print("2. International Movies, Dramas, and Comedies are among the top genres.")
print("3. The United States and India are among the top content-producing countries.")
print("4. Netflix content increased strongly after 2015.")
print("5. TV-MA is one of the most common ratings, showing Netflix has a large mature-audience catalog.")