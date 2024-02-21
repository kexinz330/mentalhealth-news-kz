import pandas as pd
from datetime import datetime
import re

anxiety_df = pd.read_csv('anxiety_articles.csv', low_memory=False)
depression_df = pd.read_csv('depression_articles.csv', low_memory=False)

anxiety_df['Anxiety or Depression'] = 0  # 0 for anxiety articles
depression_df['Anxiety or Depression'] = 1  # 1 for depression articles

combined_df = pd.concat([anxiety_df, depression_df], axis = 0, ignore_index=True)

combined_df.rename(columns={'Headline': 'Title'}, inplace=True)

combined_df['Sources'] = '1' # 1 for The Guardian

# Convert 'Publication Date' to datetime and remove rows with invalid or missing dates
combined_df['Publication Date'] = pd.to_datetime(combined_df['Publication Date'], errors='coerce')
combined_df = combined_df.dropna(subset=['Publication Date'])

# Remove timezone information from 'Publication Date'
combined_df['Publication Date'] = combined_df['Publication Date'].dt.tz_localize(None)

# Extract 'Month', 'Date', and 'Year'
combined_df['Month'] = combined_df['Publication Date'].dt.month
combined_df['Date'] = combined_df['Publication Date'].dt.day
combined_df['Year'] = combined_df['Publication Date'].dt.year

# Define the criteria for 'Time frame'
pre_date = datetime.strptime('2020-03-11', '%Y-%m-%d')
post_date = datetime.strptime('2023-05-11', '%Y-%m-%d')

# Function to determine the 'Time frame'
def determine_time_frame(row):
    if row['Publication Date'] < pre_date:
        return 0  # Pre
    elif row['Publication Date'] <= post_date:
        return 1  # During
    else:
        return 2  # Post

# Apply the function to set the 'Time frame'
combined_df['Time frame'] = combined_df.apply(determine_time_frame, axis=1)

# Remove the original 'Publication Date' column
combined_df.drop(columns=['Publication Date'], inplace=True)

def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
    else:
        text = ""
    return text

combined_df['Title'] = combined_df['Title'].apply(clean_text)
combined_df['Body Text'] = combined_df['Body Text'].apply(clean_text)

combined_df.dropna(subset=['Title', 'Body Text'], inplace=True)

combined_df = combined_df[['Sources', 'Month', 'Date', 'Year',
                           'Anxiety or Depression', 'Title',
                           'Body Text', 'Time frame']]

combined_df.to_csv('combined_articles.csv', index=False)


