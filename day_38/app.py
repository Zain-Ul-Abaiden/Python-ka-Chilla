# import libraries
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


#  Webapp Title
st.write("""
# Explore different ML models and datasets.
Let's see which model performs best on the selected dataset.
""")

# siderbar
dataset_name = st.sidebar.selectbox('Select Dataset', ('Iris', 'Breast Cancer', 'Wine'))
classifier_name = st.sidebar.selectbox('Select Classifier', ('KNN', 'SVM', 'Random Forest'))
# define function to load dataset
def get_dataset(dataset_name):
    data = None
    if dataset_name == 'Iris':
        data = datasets.load_iris()
    elif dataset_name == 'Breast Cancer':
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_wine()
    X = data.data
    y = data.target
    return X, y

X, y = get_dataset(dataset_name)

# shape of dataset
st.write('Dataset Shape:', X.shape)
st.write('Number of classes:', len(np.unique(y)))

# Add Different classifiers parameters with user input
def add_parameter_ui(classifier_name):
    params = dict() # create empty dictionary
    if classifier_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C # it's a degree of correct classification
    elif classifier_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)
        params['K'] = K # it's a number of nearest neighbors
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        params['max_depth'] = max_depth # it's a depth of tree in Random Forest
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)
        params['n_estimators'] = n_estimators # it's a number of trees in Random Forest
    return params

params = add_parameter_ui(classifier_name)

# call classifier base on classifier name
def get_classifier(classifier_name, params):
    clf = None
    if classifier_name == 'SVM':
        clf = SVC(C=params['C'])
    elif classifier_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = RandomForestClassifier(n_estimators=params['n_estimators'], max_depth=params['max_depth'], random_state=1234)
    return clf

if st.checkbox('Show Code'):
    with st.echo():
        # call classifier base on classifier name
        def get_classifier(classifier_name, params):
            clf = None
            if classifier_name == 'SVM':
                clf = SVC(C=params['C'])
            elif classifier_name == 'KNN':
                clf = KNeighborsClassifier(n_neighbors=params['K'])
            else:
                clf = RandomForestClassifier(n_estimators=params['n_estimators'], max_depth=params['max_depth'], random_state=1234)
            return clf

        clf = get_classifier(classifier_name, params)

        # split dataset into train and test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

        # fit classifier
        clf.fit(X_train, y_train)

        # make predictions
        y_pred = clf.predict(X_test)

        # calculate accuracy
        acc = accuracy_score(y_test, y_pred)

clf = get_classifier(classifier_name, params)

# split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# fit classifier
clf.fit(X_train, y_train)

# make predictions
y_pred = clf.predict(X_test)

# calculate accuracy
acc = accuracy_score(y_test, y_pred)
st.write(f'Classifier = {classifier_name}')
st.write(f'Accuracy = {acc}')

# plot PCA
pca = PCA(2)
X_projected = pca.fit_transform(X)
x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

plt.colorbar()

st.pyplot(fig)
