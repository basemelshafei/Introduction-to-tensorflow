# -*- coding: utf-8 -*-
"""l09c03_nlp_prepare_larger_text_corpus.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l09c03_nlp_prepare_larger_text_corpus.ipynb

##### Copyright 2020 The TensorFlow Authors.
"""

#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""# Tokenize and sequence a bigger corpus of text

<table class="tfo-notebook-buttons" align="left">
  <td>
    <a target="_blank" href="https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l09c03_nlp_prepare_larger_text_corpus.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Run in Google Colab</a>
  </td>
  <td>
    <a target="_blank" href="https://github.com/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l09c03_nlp_prepare_larger_text_corpus.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />View source on GitHub</a>
  </td>
</table>

So far, you have written some test sentences and generated a word index and then created sequences for the sentences. 

Now you will tokenize and sequence a larger body of text, specifically reviews from Amazon and Yelp. 

## About the dataset

You will use a dataset containing Amazon and Yelp reviews of products and restaurants. This dataset was originally extracted from [Kaggle](https://www.kaggle.com/marklvl/sentiment-labelled-sentences-data-set).

The dataset includes reviews, and each review is labelled as 0 (bad) or 1 (good). However, in this exercise, you will only work with the reviews, not the labels, to practice tokenizing and sequencing the text. 

### Example good reviews:

*   This is hands down the best phone I've ever had.
*   Four stars for the food & the guy in the blue shirt for his great vibe & still letting us in to eat !

### Example bad reviews:  

*   A lady at the table next to us found a live green caterpillar In her salad
*   If you plan to use this in a car forget about it.

### See more reviews
Feel free to [download the dataset](https://drive.google.com/uc?id=13ySLC_ue6Umt9RJYSeM2t-V0kCv-4C-P) from a drive folder belonging to Udacity and open it on your local machine to see more reviews.
"""

# Import Tokenizer and pad_sequences
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Import numpy and pandas
import numpy as np
import pandas as pd

"""# Get the corpus of text

The combined dataset of reviews has been saved in a Google drive belonging to Udacity. You can download it from there.
"""

path = tf.keras.utils.get_file('reviews.csv', 
                               'https://drive.google.com/uc?id=13ySLC_ue6Umt9RJYSeM2t-V0kCv-4C-P')
print (path)

"""# Get the dataset

Each row in the csv file is a separate review.

The csv file has 2 columns:

*   **text** (the review)
*   **sentiment** (0 or 1 indicating a bad or good review)
"""

# Read the csv file
dataset = pd.read_csv(path)

# Review the first few entries in the dataset
dataset.head()

"""# Get the reviews from the csv file"""

# Get the reviews from the text column
reviews = dataset['text'].tolist()

"""# Tokenize the text
Create the tokenizer, specify the OOV token, tokenize the text, then inspect the word index.
"""

tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(reviews)

word_index = tokenizer.word_index
print(len(word_index))
print(word_index)

"""# Generate sequences for the reviews
Generate a sequence for each review. Set the max length to match the longest review. Add the padding zeros at the end of the review for reviews that are not as long as the longest one.
"""

sequences = tokenizer.texts_to_sequences(reviews)
padded_sequences = pad_sequences(sequences, padding='post')

# What is the shape of the vector containing the padded sequences?
# The shape shows the number of sequences and the length of each one.
print(padded_sequences.shape)

# What is the first review?
print (reviews[0])

# Show the sequence for the first review
print(padded_sequences[0])

# Try printing the review and padded sequence for other elements.