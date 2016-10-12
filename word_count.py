import read
import numpy as np
import matplotlib.pyplot as plt


## initialize DataFrame as transcript
transcript = read.load_data()

## extract clinton responses from transcript
clinton = transcript[transcript["Speaker"] == "Clinton"]
clinton = clinton["Text"]
clinton_wc = 0
clinton_response_lengths = []

## extract trump responses from transcript
trump = transcript[transcript["Speaker"] == "Trump"]
trump = trump["Text"]
trump_wc = 0
trump_response_lengths = []

## loop through each to get word count, average response length
for response in clinton:
    clinton_response_lengths.append(len(response.split()))
    clinton_wc += len(response.split())
    
for response in trump:
    trump_response_lengths.append(len(response.split()))
    trump_wc += len(response.split())

## check output
print("Clinton word count:", clinton_wc)
print("Trump word count:", trump_wc)

x = [clinton.index, trump.index]
plt.bar(x[0], clinton_response_lengths, width=.5, color="b")
plt.bar(x[1], trump_response_lengths, width=.5, color="r")
plt.show()

print("Clinton average response length:", np.mean(clinton_response_lengths))
print("Trump average response length:", np.mean(trump_response_lengths))

plt.bar(range(2), [np.mean(clinton_response_lengths), np.mean(trump_response_lengths)])