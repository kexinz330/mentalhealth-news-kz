### <ins>Project Overview - PsychKids (University of Chicago) <ins>

Mental health has always been a sensitive topic, and people have been hesitant to discuss it due to the associated stigma. However, in recent years, it has become more normalized to talk about it, even in mainstream media such as newspapers. The outbreak of COVID-19 further highlighted the importance of discussing mental health, as people were isolated and had more time to think about different topics, including their mental health. Quarantine also saw a rise in adverse mental health conditions in the United States, which may have caused more people to seek information and resources about mental health.

Our project aimed to analyze the presence of mental health discussions online, specifically focusing on anxiety and depression in newspaper articles. By examining various attributes, such as the tone of the titles, we were able to identify attitudes towards mental health conditions, providing insights into changing societal attitudes. This analysis contributes to broader discussions on mental health advocacy, media attitudes, and public policy.

To begin, our two research questions were:

1. How has the frequency of articles related to anxiety and depression changed from the pre-COVID-19 era through the pandemic and into the present day, specifically in the time frames of lockdown? 
2. How are anxiety and depression framed in newspaper articles?

Our first hypothesis was that there would be a higher number of published articles during the COVID-19 lockdown compared to other time periods. As expected, we observed an increase in the proportion of articles that addressed mental health issues in 2020. This was particularly noticeable for articles related to anxiety. However, as we took a closer look at 2020, we realized that not many articles were directly related to COVID-19, suggesting that the increase in mental health discussion could also be influenced by other factors such as different generations, normal social evolution, etc. 

As for our second hypothesis, we expected that both newspapers would use different approaches and tones since they target different audiences. (e.g. The Guardian is freely accessible, while the NYT requires subscription). Aligning with our expectations, we observed that the NYT uses more emotive language overall (both positive and negative). *(Nevertheless, we need to take into consideration the imbalance of the data as a limitation of our project that could have potentially biased some results (1323 articles from The NYT and 4745 from The Guardian)).*

Overall, after analyzing both newspapers, we concluded that discussions surrounding mental health are becoming more relevant and less stigmatized as the years pass. This is evident by an increase in the neutrality of the narratives.

For future directions, we suggest this study could be replicated in other platforms (such as social media), including other mental health conditions (beyond anxiety and depression) and it could also be enhanced through the exploration of other sentiment analysis techniques and dictionaries. 

### <ins>Team members<ins>
- Jayda Hart
- Kexin Zhang
- Natasha Carpio Castellanos
- Yue Yin

### <ins>Navigation of GitHub repository<ins>
- all_articles_counts: in this directory you'll be able to find two files: "total_articles_by_year_guardian.csv" and "yearly_n_all_nyt". These contain yearly counts for ALL published articles (regardless of topic) on each newspaper from 2004 to 2024 (up until mid-February)
- guardian_articles_raw: this directory contains two csv files ("anxiety_articles_guardian.csv" and "depression_articles_guardian.csv"). These contain The Guardian's articles' raw data
- nyt_articles_raw: this directory contains two json files ("anxiety_articles_NYT.json" and "depression_articles_NYT.json"). These contain The New York Times' articles' raw data
- presentation materials: in this folder you can find two PDF files. One is "psychkids original presentation.pdf", which has the original slides from an in-class presentation of the project. The other one is "psychkids revised presentation.pdf" which are the revised slides after getting feedback.
- README.md: this file
- psychkids.ipynb: Jupyter notebook containing code used for data collection, data cleaning and data analysis/visualization
- requirements.txt: file listing the dependencies needed to reproduce the project

### <ins>Instructions to run the code<ins>

1. Users should clone the whole repository in their local machine.
2. Download two additional folders and one file that are publicly available on [Google Drive](https://drive.google.com/drive/folders/1rzZvmyKf0E0ASt6jOSZFpg4_pyP5EdFq?usp=sharing). They are:
    -  cleaned_articles: this folder contain three files; "clean_guardian.csv" and "clean_nyt" are each newspaper's clean data by separate, while "combined.csv" contains such data combined.
    -  NRC-Emotion-Lexicon: this folder was originally downloaded from the [NRC Word-Emotion Association Lexicon website](http://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm). It contains one of the sentiment analysis dictionaries that we used for the project, along with the original research papers of its development. All of its content was created by the authors Dr. Saif M. Mohammad and Dr. Peter Turney (Copyright (C) 2011 National Research Council Canada (NRC)). For further details, the folder contains its own README file and the reader can also refer to the NRC's website mentioned above.
   -  sentiment_data: this file contains the final table (both newspapers' data with sentiment analysis scores)
4. Make sure to copy these content at the same local repository in your machine (e.g. the "cleaned_articles" and the "NRC-Emotion-Lexicon" folders must be at the same level as "all_articles_counts", and the file "sentiment_data" must be at the same level as the file "requirements.txt"). Sometimes local computers will download a zip containing the folder. Be sure to unzip it.
5. Install all needed libraries if they are not already installed (specified in [requirements.txt](requirements.txt))
6. Open psychkids.ipynb in an integrated development environment (IDE) of choice and run. 

### <ins>Data sources<ins>
- The Guardian Open Platform API (https://open-platform.theguardian.com/)
- The New York Times Developers Article Search API (https://developer.nytimes.com/docs/articlesearch-product/1/overview)

### <ins>Sentiment analysis resources<ins>
- Finn Årup Nielsen. A new ANEW: Evaluation of a word list for sentiment analysis in microblogs. Proceedings of the ESWC2011 Workshop on 'Making Sense of Microposts': Big things come in small packages 718 in CEUR Workshop Proceedings 93-98. 2011 May. http://arxiv.org/abs/1103.2903.
- Mohammad, S. M., & Turney, P. D. (2013). Crowdsourcing a word–emotion association lexicon. Computational intelligence, 29(3), 436-465.
- Mohammad, S., & Turney, P. (2010, June). Emotions evoked by common words and phrases: Using mechanical turk to create an emotion lexicon. In Proceedings of the NAACL HLT 2010 workshop on computational approaches to analysis and generation of emotion in text (pp. 26-34).

### <ins>Responsibilities<ins>

*Github organization* : Natasha

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


### <ins>Additional material<ins>
- [In-class presentation](presentation%20materials/psychkids%20original%20presentation.pdf)
- [Revised presentation](presentation%20materials/psychkids%20revised%20presentation.pdf)
- Video



