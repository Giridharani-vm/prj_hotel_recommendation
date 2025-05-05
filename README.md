# Swiggy Restaurant Recommendation System using Streamlit

## 🔧 Skills Gained
- Data Preprocessing  
- One-Hot Encoding  
- Clustering (K-Means, Cosine Similarity, etc.)  
- Streamlit Application Development  
- Python Programming  

## 🌐 Domain  
Recommendation Systems and Data Analytics  

## 📌 Problem Statement  
Build a recommendation system based on restaurant data.  
Recommend restaurants based on user input (city, rating, cost, cuisine).  
Use clustering or similarity measures for recommendations.  
Present results via a user-friendly Streamlit interface.  

## ✅ Project Goals  
- Clean and preprocess the dataset.  
- One-Hot Encode categorical variables.  
- Apply clustering or similarity-based recommendation algorithms.  
- Build a Streamlit interface for interactive recommendations.  

## 💼 Business Use Cases  
- Personalized restaurant recommendations.  
- Enhanced customer experience.  
- Insights into customer preferences for marketing.  
- Improved business operations through data analytics.  

## 🗂 Dataset Columns  
- `id`, `name`, `city`, `rating`, `rating_count`, `cost`, `cuisine`  
- `lic_no`, `link`, `address`, `menu`  

### ➕ Data Types  
- Categorical: name, city, cuisine  
- Numerical: rating, rating_count, cost  

## 🚀 Project Workflow

### 1️⃣ Data Cleaning  
- Remove duplicate rows.  
- Handle or drop missing values.  
- Save clean data to `cleaned_data.csv`.  

### 2️⃣ Data Preprocessing  
- Apply One-Hot Encoding to `name`, `city`, `cuisine`.  
- Save encoder as `encoder.pkl`.  
- Save preprocessed data as `encoded_data.csv`.  
- Maintain index alignment with `cleaned_data.csv`.  

### 3️⃣ Recommendation Logic  
- Use K-Means or Cosine Similarity for matching restaurants.  
- Perform similarity matching using encoded data.  
- Map recommended indices back to original dataset.  

### 4️⃣ Streamlit Application  
- User Input Panel: city, rating, cost, cuisine, etc.  
- Backend: process input and fetch recommendations.  
- Output: show relevant restaurants from `cleaned_data.csv`.  

## 📊 Results

### 🧹 Cleaned Data  
- Clean dataset: `cleaned_data.csv`  
- Encoder: `encoder.pkl`  

### 🤖 Recommendation System  
- Algorithm: Clustering or Similarity-based  
- Recommendation mapping from encoded to cleaned data  

### 🌐 Streamlit Interface  
- Intuitive user input  
- Clear display of recommendations  

## 📘 Report Includes  
- Data Cleaning and Preprocessing Steps  
- Recommendation Methodology  
- Key Insights and Takeaways  

## 📏 Evaluation Metrics  
- Relevance and diversity of recommendations  
- Usability of Streamlit interface  
- Index consistency between CSV files  

## 📁 Project Deliverables  
- Python scripts / notebooks  
- Cleaned dataset and encoded dataset  
- Saved encoder (`.pkl`)  
- Streamlit app  
- Final Report  



