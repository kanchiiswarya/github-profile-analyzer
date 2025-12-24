import requests
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="GitHub Profile Analyzer", layout="centered")

st.title("GitHub Profile Analyzer")
st.write("Analyze GitHub repositories using the GitHub API")

username = st.text_input("Enter GitHub username")

# Fetch data if button clicked
if st.button("Analyze"):
    if username.strip() == "":
        st.error("Please enter a username")
    else:
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)

        if response.status_code != 200:
            st.error("Invalid username or API error")
        else:
            repos = response.json()
            if not repos:
                st.warning("No public repositories found")
            else:
                # Store in session_state
                st.session_state["repos"] = repos
                st.session_state["username"] = username

# Only show analysis if repos exist
if "repos" in st.session_state:
    username = st.session_state["username"]
    repos = st.session_state["repos"]

    data = []
    for repo in repos:
        data.append({
            "Repository": repo["name"],
            "Stars": repo["stargazers_count"],
            "Language": repo["language"],
            "URL": repo["html_url"]
        })

    df = pd.DataFrame(data)

    # --- PROFILE CARD ---
    user_url = f"https://api.github.com/users/{username}"
    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        user = user_response.json()
        st.subheader("Profile")
        col1, col2 = st.columns([1,3])
        with col1:
            st.image(user["avatar_url"], width=120)
        with col2:
            st.markdown(f"**{user.get('name','No name')}**")
            st.write(user.get("bio","No bio available"))
            c1, c2, c3 = st.columns(3)
            c1.metric("Followers", user["followers"])
            c2.metric("Following", user["following"])
            c3.metric("Public Repos", user["public_repos"])

    # --- STAR FILTER ---
    min_stars = st.slider(
        "Minimum Stars",
        min_value=0,
        max_value=int(df["Stars"].max()),
        value=0
    )
    df_filtered = df[df["Stars"] >= min_stars]

    # --- REPO TABLE ---
    st.subheader("Repository Details")
    df_sorted = df_filtered.sort_values(by="Stars", ascending=False)
    df_sorted["Repository"] = df_sorted.apply(
        lambda row: f"[{row['Repository']}]({row['URL']})", axis=1
    )
    st.write(df_sorted[["Repository","Stars","Language"]], unsafe_allow_html=True)

    # --- LANGUAGE PIE CHART ---
    st.subheader("Languages Used (Top 5)")
    lang_count = df_filtered["Language"].dropna().value_counts().head(5)
    fig, ax = plt.subplots()
    ax.pie(lang_count, labels=lang_count.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
