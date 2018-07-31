
# Will we need to trim off the quote marks again?
# NOTE: Dash runs in threads. So callbacks should not modify global variables, or they could get threads out of sync.
import pandas as pd
from textblob import TextBlob

df = pd.read_csv('Hamlet.csv')
# print(df.head())

hamlet = ''
char_count = [0, 0] # To get right number...
total = 0

# Ok weird idea: we add a column to the dataframe that keeps track of how many characters have appeared so far. So first line gets 0. Then next line gets 13. Then 57. Etc.
for line in df['Lines'][2:]:
    # print(line)
    hamlet += line + ' '
    # if 'death' in line:
    #     print(line)
    char_count.append(total)
    total += len(line) + 1 # add one because of the space

df['char_count'] = pd.Series(char_count, index=df.index)


print(df.head(30))



hamlet_blob = TextBlob(hamlet)

sentences = hamlet_blob.sentences # Hmmm, but we'd like to attach the speaker to each one...

hamlet_dict = {}


# words = hamlet_blob.words

# print(sentences[:5], words[:50])

# print(hamlet_blob.translate(to='es'))
# print(hamlet_blob.tags)
# print(hamlet_blob.sentiment)


# for line in df['Lines'][2:]:
#     analysis = TextBlob(hamlet)


for s in sentences[:20]:
    # if (abs(s.sentiment.polarity) > 0.5):
        # print(s.start, s.end, hamlet_blob[s.start])
    if (df['char_count'==s.start]['Speakers']):
        print(df['char_count'==s.start]['Speakers'])

    # print(s.start, hamlet_blob[s.start])









# to be or not to be
