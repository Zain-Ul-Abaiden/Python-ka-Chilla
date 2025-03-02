import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

# Header
with header:
    st.title('Titanic Survival Prediction')
    st.text('This is a simple web app to predict the survival of passengers on the Titanic.')

# Load and Display Dataset
with data_sets:
    st.header('Data Sets')
    st.text('This is the dataset used for training the model.')
    df = sns.load_dataset('titanic').dropna()  # Remove NaN values
    st.write(df.head(10))
    
    # Data Visualizations
    st.subheader('Gender Distribution')
    st.bar_chart(df['sex'].value_counts())

    st.subheader('Survival Rate by Class')
    st.bar_chart(df['class'].value_counts())

    st.subheader('Sample of Passenger Ages')
    st.bar_chart(df['age'].sample(10))

# Feature Selection
with features:
    st.header('Features')
    st.text('These are the features used for training the model.')
    st.markdown('1. **Pclass** - Ticket class (1st, 2nd, 3rd)')
    st.markdown('2. **Sex** - Gender of the passenger')
    st.markdown('3. **Age** - Age of the passenger')
    st.markdown('4. **Fare** - Fare paid for ticket')

# Model Training
with model_training:
    st.header('Model Training')
    st.text('This is the model training process.')

    # Sidebar Inputs
    inputs, display = st.columns(2)

    max_depth = inputs.slider("Select tree depth:", min_value=1, max_value=20, value=10, step=1)
    n_estimators = inputs.selectbox("Number of trees in Random Forest:", options=[50, 100, 200, 300, 'No limit'])

    # Convert 'No limit' to default RF settings
    if n_estimators == 'No limit':
        model = RandomForestClassifier(max_depth=max_depth)
    else:
        model = RandomForestClassifier(max_depth=max_depth, n_estimators=int(n_estimators))

    # Feature Selection from User
    selected_feature = inputs.selectbox("Select a feature for prediction:", options=df.columns.tolist())

    if selected_feature:
        X = df[[selected_feature]]  # Independent variable
        y = df['survived']  # Dependent variable (target)

        # Convert categorical features to numerical
        if X[selected_feature].dtype == 'object':
            X = pd.get_dummies(X, drop_first=True)

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model.fit(X_train, y_train)

        # Predictions
        predictions = model.predict(X_test)

        # Display Metrics
        display.subheader('Model Performance:')
        display.write(f"Mean Absolute Error: {mean_absolute_error(y_test, predictions):.2f}")
        display.write(f"Mean Squared Error: {mean_squared_error(y_test, predictions):.2f}")
        display.write(f"R² Score: {r2_score(y_test, predictions):.2f}")
