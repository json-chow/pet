import pandas as pd
import random

random.seed(123)

df = pd.read_csv("hypo.csv")
n = len(df)

# 100 training examples, 10% data held out for validation
n_train = 100
n_dev = int(n * 0.1)
n_train_unlabeled = n - n_dev

train_unlabeled_ind = random.sample(range(len(df)), k=n_train_unlabeled)
train_ind = random.sample(train_unlabeled_ind, k=n_train)
val_df = df.loc[set(df.index) - set(train_unlabeled_ind)]
train_df = df.loc[train_ind]
unlabeled_df = df.loc[set(train_unlabeled_ind) - set(train_ind)]
unlabeled_df["hyperbole"] = -1

train_df.to_csv("train.csv", index=False, header=False)
val_df.to_csv("dev.csv", index=False, header=False)
unlabeled_df.to_csv("unlabeled.csv", index=False, header=False)