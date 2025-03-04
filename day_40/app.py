from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import ExplainerDashboard
from explainerdashboard.datasets import titanic_survive, feature_descriptions
from explainerdashboard.explainers import ClassifierExplainer

# Load Titanic dataset
X_train, y_train, X_test, y_test = titanic_survive()

# Train RandomForest Model with fixed parameters for stability
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42).fit(X_train, y_train)

# Create Explainer
explainer = ClassifierExplainer(
    model, X_test, y_test,
    cats=['Sex', 'Deck', 'Embarked'],
    descriptions=feature_descriptions,
    labels=['Not survived', 'Survived']
)

# Run Dashboard with explicit layout settings to prevent titlefont issues
ExplainerDashboard(
    explainer, 
    dashboard_kwargs={'layout': {'title': {'text': 'Explainer Dashboard', 'font': {'size': 20}}}},
    verbose=True  # Enable debugging
).run()
