import requests
import pandas as pd
import matplotlib.pyplot as plt

print("=== GitHub Profile Analyzer ===")

username = input("Enter GitHub username: ")

url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)

if response.status_code != 200:
    print("Invalid username or API error")
    exit()

repos = response.json()

if not repos:
    print("No public repositories found")
    exit()

data = []
for repo in repos:
    data.append({
    "Repository": repo["name"],
    "Stars": repo["stargazers_count"],
    "Language": repo["language"],
    "URL": repo["html_url"]
})

df = pd.DataFrame(data)

print("\nTotal Repositories:", len(df))
print("Total Stars:", df["stars"].sum())

top_repo = df.sort_values(by="stars", ascending=False).iloc[0]
print("Most Starred Repo:", top_repo["name"], "-", top_repo["stars"], "stars")

lang_count = df["language"].value_counts()

plt.figure()
lang_count.plot(kind="bar")
plt.title("Languages Used")
plt.xlabel("Language")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("languages.png")

print("\nLanguage chart saved as languages.png")
