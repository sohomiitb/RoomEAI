# RoomAI: Roommate Recommendation System

RoomAI is a Python-based application that generates a large synthetic dataset of roommate profiles and provides a recommendation system to find the best roommate matches based on user preferences. The project uses pandas, scikit-learn, and Streamlit for data generation, similarity computation, and interactive web UI.

## Features

- **Synthetic Data Generation**: Creates 20,000+ realistic roommate profiles with attributes like gender, nationality, language, occupation, hobbies, and more using [Faker](https://faker.readthedocs.io/).
- **Profile Encryption**: Each profile is assigned a unique encrypted ID for privacy.
- **Roommate Matching**: Uses one-hot encoding and cosine similarity to recommend the top N most compatible roommates.
- **Interactive Web App**: Built with Streamlit for easy user interaction and visualization of results.

## Project Structure

```
roomAI_app.py                  # (Optional) Main app script if using .py
RoomAI.ipynb                   # Jupyter notebook with all code and Streamlit app
synthetic_roommate_profiles.csv # Generated dataset of roommate profiles
```

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/roomai.git
cd roomai
```

### 2. Install Dependencies

```sh
pip install pandas numpy scikit-learn faker streamlit
```

### 3. Generate the Dataset

You can generate the dataset by running the code in [RoomAI.ipynb](RoomAI.ipynb) or executing the relevant Python script if available.

### 4. Run the Streamlit App

```sh
streamlit run RoomAI.ipynb
```
or, if you have a `.py` file:
```sh
streamlit run roomAI_app.py
```

### 5. Use the App

- Enter your roommate preferences in the sidebar.
- Click "Find My Top Matches" to see your best roommate matches from the dataset.

## How It Works

- **Data Generation**: Uses Faker and randomization to create diverse roommate profiles.
- **Similarity Calculation**: Selects key features, encodes them, and computes cosine similarity between users.
- **Recommendation**: Returns the top N most similar profiles based on your input.

## Example

![RoomAI Streamlit Screenshot](screenshot.png)

## License

MIT License

## Acknowledgements

- [Faker](https://faker.readthedocs.io/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)

---

*Created by [Your Name]*
