import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
import spacy
from collections import defaultdict
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

nlp = spacy.load('en_core_web_sm')

data = pd.read_csv("articles.csv", encoding='latin-1')
print(data.head())

# Create a new column with the length of the article
# Combine all titles into a single string
titles_text = ' '.join(data['Title'])

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)

# Plot the Word Cloud
fig = px.imshow(wordcloud, title='Word Cloud of Titles')
fig.update_layout(showlegend=False)
fig.show()

#analyze the distribution of sentiments in the dataset
# Create a new column with the sentiment of the article
data['Sentiment'] = data['Article'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Plot the distribution of sentiments
fig = px.histogram(data, x='Sentiment', title='Distribution of Sentiments')
fig.show()

#analyze the most common entities in the dataset, Named Entity Recognition (NER)
# Create a dictionary to store the frequency of entities
def extract_named_entities(text):
    doc = nlp(text)
    entities = defaultdict(list)
    for ent in doc.ents:
        entities[ent.label_].append(ent.text)
    return dict(entities)

# Apply the function to the 'Article' column
data['Entities'] = data['Article'].apply(extract_named_entities)

# # Flatten the dictionary of entities
# entities_list = [ent for entities in data['Entities'] for ent in entities.values()]

# Visualize NER
entity_counts = Counter(entity for entities in data['Entities'] for entity in entities)
entity_df = pd.DataFrame.from_dict(entity_counts, orient='index').reset_index()
entity_df.columns = ['Entity', 'Count']

fig = px.bar(entity_df, x='Entity', y='Count', title='Most Common Entities')
fig.show()


#analyze the topics in the dataset using Latent Dirichlet Allocation (LDA)
# Create a CountVectorizer object
vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=1000, stop_words='english')
tf = vectorizer.fit_transform(data['Article'])
lda_model = LatentDirichletAllocation(n_components=5, random_state=42)
lda_topic_matrix = lda_model.fit_transform(tf)

# Visualize topics
topic_names = ["Topic " + str(i) for i in range(lda_model.n_components)]
data['Dominant_Topic'] = [topic_names[i] for i in lda_topic_matrix.argmax(axis=1)]

fig = px.bar(data['Dominant_Topic'].value_counts().reset_index(), x='Dominant_Topic', y='count', title='Topic Distribution')
fig.show()



# Get the most common words for each topic
topic_words = []
for topic in lda_model.components_:
    word_idx = topic.argsort()[::-1][:5]
    topic_words.append([vectorizer.get_feature_names_out()[i] for i in word_idx])

# Create a DataFrame with the topics and the most common words
topic_df = pd.DataFrame(topic_words, columns=['Word 1', 'Word 2', 'Word 3', 'Word 4', 'Word 5'])
topic_df.index.name = 'Topic'

print(topic_df)

# Get the feature names (words) and topic numbers
words = vectorizer.get_feature_names_out()
topics = ["Topic " + str(i) for i in range(lda_model.components_.shape[0])]

# Get the sum of associations for each word across all topics
word_sums = lda_model.components_.sum(axis=0)

# Get the indices of the top 15 words
top_word_indices = word_sums.argsort()[-15:][::-1]

# Select only the top 15 words and their associations
top_words = words[top_word_indices]
top_word_associations = lda_model.components_[:, top_word_indices]

# Visualize the topics
fig = px.imshow(top_word_associations, 
                labels=dict(x="Top Words", y="Topics", color="Association"),
                x=top_words,
                y=topics,
                color_continuous_scale='Viridis', 
                title='LDA Topic Matrix')

# Set the range of the y-axis to include all topics
fig.update_yaxes(autorange="reversed")

fig.show()