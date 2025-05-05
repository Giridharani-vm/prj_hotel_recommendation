import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load models and preprocessor
preprocessor = joblib.load(r'C:\DATA SCIENCE\PROJECT FOLDERS\prj_restaurant_recommendation\preprocessor.pkl')
svd = joblib.load(r'C:\DATA SCIENCE\PROJECT FOLDERS\prj_restaurant_recommendation\svd_model.pkl')
kmeans = joblib.load(r'C:\DATA SCIENCE\PROJECT FOLDERS\prj_restaurant_recommendation\kmeans_model.pkl')
imputer = joblib.load(r'C:\DATA SCIENCE\PROJECT FOLDERS\prj_restaurant_recommendation\imputer.pkl')

# Load clustered data
data = pd.read_csv(r"C:\DATA SCIENCE\PROJECT FOLDERS\prj_restaurant_recommendation\clustered.csv")

st.balloons()

# App title
st.title("🍽️ Swiggy Restaurant Recommendation System")
st.markdown("Get top restaurant suggestions based on your preferences!")

# User Inputs
restaurant_names = sorted(data['NAME'].dropna().unique())
NAME = st.selectbox(" Restaurant NAME (Optional)", options=[""] + restaurant_names)
COST = st.slider("Desired COST (approximate)", min_value=100, max_value=2000, step=50, value=500)
CITY = st.selectbox("Select CITY", options=[""] + sorted(data['CITY'].dropna().unique()))
CUISINE = st.selectbox("Preferred CUISINE", options=[""] + sorted(data['CUISINE'].dropna().unique()))
RATING = st.slider("Desired Minimum RATING", min_value=1.0, max_value=5.0, step=0.1, value=3.5)

# Optional Rating Count
use_rating_count = st.checkbox("Include Rating Count?")
Rating_Count = st.number_input("Rating Count (Optional)", min_value=0, max_value=10000, step=10, value=0, disabled=not use_rating_count)

# Save default values for comparison
default_cost = 500
default_rating = 3.5

# Recommend button
if st.button("🔍 Get Recommendations"):
    try:
        filters = []

        if CITY:
            filters.append(data['CITY'] == CITY)

        if CUISINE:
            filters.append(data['CUISINE'] == CUISINE)

        if RATING != default_rating:
            filters.append(data['RATING'] >= RATING)

        if COST != default_cost:
            filters.append((data['COST'] >= COST - 300) & (data['COST'] <= COST + 300))

        if use_rating_count:
            filters.append(data['Rating_Count'] >= Rating_Count)

        if not filters:
            st.warning("Please select at least one preference (like Cuisine, City, Cost, etc.) to get recommendations.")
        else:
            filtered_data = data.copy()
            for f in filters:
                filtered_data = filtered_data[f]

            # Sort by rating and rating count
            recommendations = filtered_data.sort_values(by=['RATING', 'Rating_Count'], ascending=[False, False]).head(10)

            if recommendations.empty:
                st.info("No restaurants found matching your preferences.")
            else:
                display_df = recommendations[['NAME', 'CITY', 'CUISINE', 'COST', 'RATING', 'Rating_Count']].copy()
                display_df.columns = ['Restaurant Name', 'City', 'Cuisine', 'Cost (₹)', 'Rating', 'Rating Count']
                st.success("Top Restaurant Recommendations for You:")
                st.dataframe(display_df.reset_index(drop=True), use_container_width=True)

    except Exception as e:
        st.error("Something went wrong! Please check your data and models.")
        st.exception(e)




