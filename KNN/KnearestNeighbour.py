import random
import numpy as np
import warnings
from collections import Counter
import pandas as pd


def get_euclidean(features, predict):
    euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
    return euclidean_distance


def knn(dataSet, predict, groups):
    if len(dataSet) > groups:
        warnings.warn("Your dataSet is les than the number of groups to be created")
    elif len(dataSet) == groups:
        warnings.warn("Your dataSet is equal to the number of groups required hence each feature will be on its own "
                      "group")

    distances = []

    for grp in dataSet:
        for features in dataSet[grp]:
            euclidean_distance = get_euclidean(features, predict)
            distances.append([euclidean_distance, grp])

    votes = [j[1] for j in sorted(distances)[:groups]]
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result


if __name__ == '__main__':
    df = pd.read_csv("../Data/heart.data.txt", header=None, delimiter=" ")
    df.replace('?', -9999, inplace=True)
    full_data = df.astype(float).values.tolist()
    random.shuffle(full_data)

    test_s = int(input("Input the test data as a %: "))
    test_size = test_s / 100
    test_set = {2: [], 1: []}
    train_set = {2: [], 1: []}
    train_data = full_data[:-int(test_size * len(full_data))]
    test_data = full_data[-int(test_size * len(full_data)):]

    for i in train_data:
        train_set[i[-1]].append(i[:-1])

    for i in test_data:
        test_set[i[-1]].append(i[:-1])

    correct = 0
    total = 0
    for group in test_set:
        for data in test_set[group]:
            # print(data)
            vote = knn(train_set, data, 5)
            if group == vote:
                correct += 1
            total += 1
    accuracy = (correct / total * 100)
    print("Accuracy {}%".format(accuracy))
