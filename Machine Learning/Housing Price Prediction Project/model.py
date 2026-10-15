import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import (LinearRegression , Ridge, Lasso, ElasticNet,SGDRegressor,
                                  HuberRegressor,
                                  )

from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline  #data Leakeges
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
#import lightgbm as lgb
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle

#Load dataset

data = pd.read_csv(r'C:\Users\SHIVARAM\OneDrive\Desktop\FSDS\Machine Learning\Capstone Project\USA_Housing.csv')


#preprocessing

X = data.drop(['Price','Address'], axis=1) 
y = data['Price']


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Defin e models

models = {
    'Linear Regression': LinearRegression(),
    'Robust Regression': HuberRegressor(),
    'Ridge Regression': Ridge(),
    'Lasso Regression': Lasso(),
    'ElasticNet': ElasticNet(),
    'Polynomial Regression': Pipeline([
        ('poly', PolynomialFeatures(degree=4)), 
        ('linear', LinearRegression())]),
    'SGD Regressor': SGDRegressor(),
    'ANN': MLPRegressor(hidden_layer_sizes=(100,), max_iter=1000),
    'Random Forest': RandomForestRegressor(),
    'SVR': SVR(),
    # 'LGBM': lgb.LGBMRegressor(),
    'XGBoost': xgb.XGBRegressor(),
    'KNN': KNeighborsRegressor()

 }


results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results.append({
        'Model': name,
        'MSE': mse,
        'MAE': mae,
        'R2 Score': r2
    })

    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(model, f)

# Convert results to DataFrame and save to CSV
results_df = pd.DataFrame(results)
results_df.to_csv('model_evaluation_results.csv', index=False)

print('Model have trained and saved as pickle files. Evaluation results saved to model_evaluation_results.csv')





















