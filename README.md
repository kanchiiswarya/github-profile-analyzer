Live App: https://app-profile-analyzer-xjpkhqdvuaxwfgxiafczeg.streamlit.app/
# GitHub Profile Analyzer

A Streamlit web application that analyzes a GitHub user's public repositories using the GitHub API.
The app displays repository statistics, filtering options, and language visualizations.

---

## Features

- Fetch public repositories of any GitHub user
- Display total repositories and total stars
- Show the most starred repository
- Filter repositories by minimum stars using a slider
- Display repositories in a table
- Visualize top programming languages using a pie chart
- Interactive UI built with Streamlit

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Requests
- Matplotlib
- GitHub REST API

---

## Setup Instructions

Clone the repository:

git clone https://github.com/kanchiiswarya/github-profile-analyzer.git  
cd github-profile-analyzer

Create a virtual environment (optional but recommended):

python -m venv venv

Activate the virtual environment (Windows):

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

---

## Run the Application

streamlit run app.py

The app will open automatically in your browser.

---

## Usage

1. Enter a GitHub username
2. Click Analyze
3. View repository statistics and charts
4. Use the slider to filter repositories by stars

---

## Notes

- The venv folder is excluded from GitHub using .gitignore
- Uses GitHub public API (no authentication required)
- Best tested with users having multiple repositories (example: torvalds)

---

## Author

GitHub: https://github.com/kanchiiswarya
