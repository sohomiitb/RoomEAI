import streamlit as st
import pandas as pd
import hashlib
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics.pairwise import cosine_similarity

# --- Helper functions ---
def generate_encrypted_id(name, email=None, phone=None):
    email = email or "abc@xyz.com"
    phone = phone or "123456789"
    combined = f"{name}_{email}_{phone}"
    return hashlib.sha256(combined.encode()).hexdigest()

def get_top_matches(user_profile, df, top_n=5):
    # Add user's input to the dataset temporarily for comparison
    df_extended = df.copy()
    user_profile["Encrypted_ID"] = "user_input"
    df_extended = pd.concat([df_extended, pd.DataFrame([user_profile])], ignore_index=True)

    # Encode features
    features = df_extended[[
        "Gender", "Do you smoke", "Do you have pet", "Nationality",
        "Primary Language", "Dietary Preference", "Occupation", "Work Schedule"
    ]]
    encoder = OneHotEncoder()
    encoded_features = encoder.fit_transform(features).toarray()

    similarity_matrix = cosine_similarity(encoded_features)
    similarity_df = pd.DataFrame(similarity_matrix, index=df_extended["Encrypted_ID"], columns=df_extended["Encrypted_ID"])

    # Extract top matches for the user input
    top_matches_series = similarity_df.loc["user_input"].sort_values(ascending=False)[1:top_n+1]
    top_match_ids = top_matches_series.index.tolist()
    top_match_scores = top_matches_series.values.round(2)

    top_matches_df = df[df["Encrypted_ID"].isin(top_match_ids)][[
        "Encrypted_ID", "Name", "Email", "Phone Number", "Gender", "Nationality", "Do you smoke", "Do you have pet","Location",
         "Dietary Preference", "Occupation", "Work Schedule","Primary Language"
    ]]
    top_matches_df = top_matches_df.set_index("Encrypted_ID").loc[top_match_ids].reset_index()
    #top_matches_df.insert(0, "Similarity Score", top_match_scores)
    top_matches_df=top_matches_df.drop(columns=["Encrypted_ID"], errors='ignore')
    return top_matches_df

# --- Streamlit UI ---
st.title("🏠 Roommate Recommendation System")

st.sidebar.header("🔍 Enter Your Preferences")
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"])
smoke = st.sidebar.selectbox("Do you smoke?", ["Yes", "No"])
pet = st.sidebar.selectbox("Do you have a pet?", ["Yes", "No"])
nationality = st.sidebar.text_input("Nationality")
language = st.sidebar.text_input("Primary Language")
diet = st.sidebar.selectbox("Dietary Preference", ["Vegetarian", "Vegan", "No restriction", "Others"])
occupation = st.sidebar.text_input("Occupation")
schedule = st.sidebar.selectbox("Work Schedule", ["Day", "Afternoon", "Overnight"])

if st.sidebar.button("Find My Top Matches"):
    try:
        df = pd.read_csv("synthetic_roommate_profiles.csv")

        # Prepare user profile
        user_profile = {
            "Gender": gender,
            "Do you smoke": smoke,
            "Do you have pet": pet,
            "Nationality": nationality,
            "Primary Language": language,
            "Dietary Preference": diet,
            "Occupation": occupation,
            "Work Schedule": schedule
        }

        matches = get_top_matches(user_profile, df)
        if not matches.empty:
            st.success("✅ Top Roommate Matches Found:")
            st.dataframe(matches)
    except Exception as e:
        st.error(f"Error: {str(e)}")