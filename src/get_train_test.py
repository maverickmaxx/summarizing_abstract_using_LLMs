import pandas as pd
from sklearn.model_selection import train_test_split

print('reading data')
data = pd.read_csv("../data/raw/arxiv_data_210930-054931.csv")
X_train, X_test, y_train, y_test = train_test_split(data[['terms','abstracts']], data['titles'], test_size=0.2, random_state=923)

print('Writing data to /data/interim/ folder')
X_train.to_csv("../data/interim/X_train.csv", index=False)
X_test.to_csv("../data/interim/X_test.csv", index=False)
y_train.to_csv("../data/interim/y_train.csv", index=False)
y_test.to_csv("../data/interim/y_test.csv", index=False)

print("Done")