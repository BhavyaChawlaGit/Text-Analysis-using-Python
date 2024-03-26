# Text-Analysis

## Overview

Text Analysis involves extracting meaningful insights from unstructured text data, such as documents, emails, social media posts, and more.  
This project aims to demonstrate various text analysis techniques using Python.

For text analysis, I utilized a dataset containing articles with the following attributes:

- Article
- Title

<img width="753" alt="Screenshot 2024-03-25 at 4 16 48 PM" src="https://github.com/BhavyaChawlaGit/Text-Analysis-using-Python/assets/112718303/7283dd42-f3ee-4b31-b18e-84785a79b371">


You can download the dataset [here](https://statso.io/wp-content/uploads/2023/02/Topic-Modelling.zip).

Furthur the process I followed is as below

- Gather the text data
- Clean and preprocess the text data
- Convert the text into a numerical format that machine learning algorithms can understand
- Analyze the text data to gain insights
- Create relevant features from the text data if necessary
- Select appropriate NLP model for my task


## Results

### Word Cloud of Titles

Created a word cloud visualization to illustrate the most frequent words appearing in the titles of the articles. This provides a quick overview of the topics covered in the dataset.

![newplot](https://github.com/BhavyaChawlaGit/Text-Analysis-using-Python/assets/112718303/023a58ee-9cc6-4fce-9e61-c949e01ff082)


**The word cloud shows that terms such as "Machine Learning" "Python" "Data" "Clustering" and "Algorithm" are very prominent, it is clear that the focus of the dataset is on technical and analytical topics, particularly those related to data science and machine learning.**  
---

### Sentiment Distribution

Analyzed the sentiment expressed in the articles using the TextBlob library. By visualizing the sentiment distribution, it helps in understanding the overall tone or polarity of the content.  

![newplot (1)](https://github.com/BhavyaChawlaGit/Text-Analysis-using-Python/assets/112718303/def3b2b7-fdfd-4f7a-be0f-162fdca1af52)

**The sentiment polarity scores range from -1 to 1, with -1 being very negative, 0 being neutral, and 1 being very positive. The histogram shows that most articles have a neutral sentiment (close to 0), with fewer articles showing negative or positive sentiments. This could indicate that the articles in the dataset are mostly informative or technical in nature, where sentiment is not strongly expressed.**

---

### Top Named Entities

Utilized Named Entity Recognition (NER) technique to extract and visualize the most common named entities (such as organizations, locations, etc.) mentioned in the articles. This aids in identifying the prominent entities discussed in the text data.   

![newplot (2)](https://github.com/BhavyaChawlaGit/Text-Analysis-using-Python/assets/112718303/d9e104bd-6d53-407f-ae11-7b8d8ab5e8be)

**The plot shows that organizations are the most frequently mentioned entities, suggesting that the articles discuss specific institutions, companies, or groups. This is followed by dates and cardinal numbers, which might be used when discussing events, statistics, or providing factual information.**

---

### Topic Distribution

Applied Latent Dirichlet Allocation (LDA) for topic modeling to uncover latent topics within the articles. The bar chart visualization presents the distribution of dominant topics across the dataset, providing insights into prevalent themes or subjects discussed.  

![newplot (3)](https://github.com/BhavyaChawlaGit/Text-Analysis-using-Python/assets/112718303/6b62cf79-f980-4c6d-946f-c48f60871294)

**The histogram indicates that "Topic 1" is the most prevalent, followed by "Topic 3," "Topic 0," "Topic 4," and "Topic 2." The predominance of "Topic 1" suggests that there is a dominant theme or subject area covered in the dataset.**

---

### Most common words for each topic

Generated a matrix visualization to depict the associations between the top words and topics identified through LDA. This matrix helps in understanding the most relevant words associated with each topic, contributing to a deeper understanding of the underlying themes in the text data.  

![newplot (4)](https://github.com/BhavyaChawlaGit/Text-Analysis-using-Python/assets/112718303/140a1d75-5529-4050-8ddc-d1533bb9666b)
<img width="431" alt="Screenshot 2024-03-25 at 4 17 36 PM" src="https://github.com/BhavyaChawlaGit/Text-Analysis-using-Python/assets/112718303/8338e23c-04f1-4f65-95a5-6783ac8a3d1a">

**Words such as "learning," "machine," "data," "python," and "using" appear prominently across multiple topics, reinforcing the notion that machine learning and Python programming are significant themes in the dataset.**

---

## Summary

The text analysis shows us what the articles are mainly about and can guide us on what to look into next. For instance, we might want to dig deeper into the most common topics or think about making more detailed models for those specific areas. This project demonstrates the application of various text analysis techniques using Python. For further details, refer to the code provided in this repository [here](analysis.py)



