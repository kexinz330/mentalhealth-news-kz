### <ins>Project Overview - PsychKids (University of Chicago) <ins>

Mental health has always been a sensitive topic, and people have been hesitant to discuss it due to the associated stigma. However, in recent years, it has become more normalized to talk about it, even in mainstream media such as newspapers. The outbreak of COVID-19 further highlighted the importance of discussing mental health, as people were isolated and had more time to think about different topics, including their mental health. Quarantine also saw a rise in adverse mental health conditions in the United States, which may have caused more people to seek information and resources about mental health.

Our project aimed to analyze the presence of mental health discussions online, specifically focusing on anxiety and depression in newspaper articles. By examining various attributes, such as the tone of the titles, we were able to identify attitudes towards mental health conditions, providing insights into changing societal attitudes and the impact of policies such as lockdowns. This analysis contributes to broader discussions on mental health advocacy, media attitudes, and public policy.

To begin, our two research questions were:

1. How has the frequency of articles related to anxiety and depression changed from the pre-COVID-19 era through the pandemic and into the present day, specifically in the time frames of lockdown? 
2. How are anxiety and depression framed in newspaper articles?

Our first hypothesis was that there would be a higher number of published articles during the COVID-19 lockdown compared to other time periods. As expected, we observed an increase in the proportion of articles that addressed mental health issues in 2020. This was particularly noticeable for articles related to anxiety. However, as we took a closer look at 2020, we realized that not many articles were directly related to COVID-19, suggesting that the increase in mental health discussion could also be influenced by other factors such as different generations, normal social evolution, etc. 

As for our second hypothesis, we expected that both newspapers would use different approaches and tones since they target different audiences. (e.g. The Guardian is freely accessible, while the NYT requires subscription). Aligning with our expectations, we observed that the NYT uses more emotive language overall (both positive and negative). *(Nevertheless, we need to take into consideration the imbalance of the data as a limitation of our project that could have potentially biased some results (1323 articles from The NYT and 4745 from The Guardian)).*

Overall, after analyzing both newspapers, we concluded that discussions surrounding mental health are becoming more relevant and less stigmatized as the years pass. This is evident by an increase in the neutrality of the narratives.

For future directions, we suggest this study could be replicated in other platforms (such as social media), including other mental health conditions (beyond anxiety and depression) and it could also be enhanced through the exploration of other sentiment analysis techniques and dictionaries. 


### <ins>Navigation of GitHub repository<ins>
Along with this README file, you can find the following folders and documents:

- all_articles_counts: in this directory you'll be able to find two files: "total_articles_by_year_guardian.csv" and "yearly_n_all_nyt". These contain yearly counts for ALL published articles (regardless of topic) on each newspaper from 2004 to 2024 (up until mid-February)
- guardian_articles_raw: this directory contains two csv files ("anxiety_articles_guardian.csv" and "depression_articles_guardian.csv"). These contain The Guardian's articles' raw data
- nyt_articles_raw: this directory contains two json files ("anxiety_articles_NYT.json" and "depression_articles_NYT.json"). These contain The New York Times' articles' raw data
- presentation materials: in this folder you can find two PDF files. One is "psychkids original presentation.pdf", which have the original slides from an in-class presentation of the project. The other one is "psychkids revised presentation.pdf" which are the revised slides after getting feedback.
- READme.md: this file
- psychkids.ipynb: Jupyter notebook containing code used for data collection, data cleaning and data analysis/visualization
- requirements.txt: file listing the required libraries/version numbers needed to reproduce the project

### <ins>Instructions to run the code<ins>

1. Users should clone the whole repository in their local machine.
2. Download two additional folders and one file that are publicly available on Google Drive. The link to access them is: https://drive.google.com/drive/folders/1rzZvmyKf0E0ASt6jOSZFpg4_pyP5EdFq?usp=sharing
4. Make sure to put the two folders ("cleaned_articles" and "NRC-Emotion-Lexicon") and the file "sentiment_data" at the same local repository in your machine, at the same level as the other folders (such as all_articles_counts) (Sometimes local computers will download a zip containing the folder. Be sure to unzip it.)
5. Install all needed packages if they are not already installed (specified in requirements.txt)
6. Open psychkids.ipynb in an integrated development environment (IDE) of choice and run. 

### <ins>Responsibilities of team members<ins>

*Overall project management (correct merge of data, files organization, upload of material, overlook of tasks, etc.)* : Natasha

*Data Collection*
- The New York Times articles: Natasha
- The Guardian articles: Yue

*Data Cleaning*
- The New York Times' data: Jayda
- The Guardian's data: Kexin

*Data Analysis*
- Trends Analysis: Yue
- Frequency of COVID-19 articles on 2020: Jayda
- Words frequencies in titles: Natasha
- N-grams: Kexin
- Sentiment Analysis: Jayda

*Presentation*: All members

*Video Recording*: All members\
*Video Editing*: Yue

*This README file*: Natasha

