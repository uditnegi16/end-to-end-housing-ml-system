# End-to-End Housing ML System

A production-style Machine Learning system built using the California Housing Dataset. This project goes beyond notebook experimentation by implementing an end-to-end ML workflow including data preprocessing, feature engineering, model training, model serving, monitoring, logging, and API deployment.

---

## Business Problem

A real estate investment company wants to identify promising housing districts in California.

The company requires a system capable of:

- Predicting median house values
- Supporting investment decisions
- Serving predictions through APIs
- Tracking model behavior in production

---

## Machine Learning Objective

Predict:

```text
median_house_value
```

Problem Type:

```text
Supervised Learning
Regression
```

Evaluation Metric:

```text
RMSE (Root Mean Squared Error)
```

---

## Dataset

California Housing Dataset

### Features

- longitude
- latitude
- housing_median_age
- total_rooms
- total_bedrooms
- population
- households
- median_income
- ocean_proximity

### Target

```text
median_house_value
```

---

## Project Architecture

```text
User Input
    │
    ▼
FastAPI Endpoint
    │
    ▼
Pydantic Validation
    │
    ▼
Preprocessing Pipeline
    │
    ▼
Random Forest Regressor
    │
    ▼
Predicted House Price
    │
    ▼
Investment Decision Engine
    │
    ▼
JSON Response
    │
    ▼
Prediction Logging
```

---

## Machine Learning Workflow

### 1. Business Understanding

Defined:

- Stakeholder
- Business Objective
- Machine Learning Objective
- Success Metric

Chosen Metric:

```text
RMSE
```

### 2. Data Exploration

Performed:

- Dataset inspection
- Schema analysis
- Missing value analysis
- Feature distribution analysis
- Categorical feature analysis

### 3. Train/Test Strategy

Implemented:

```python
StratifiedShuffleSplit
```

to preserve income distribution across train and test datasets.

### 4. Exploratory Data Analysis

Performed:

- Correlation analysis
- Geographic visualization
- Scatter plot analysis
- Feature relationship analysis
- Housing value trend exploration

### 5. Feature Engineering

Created:

```text
rooms_per_household
bedrooms_per_room
population_per_household
```

### 6. Data Preparation

Implemented:

- SimpleImputer
- OneHotEncoder
- StandardScaler
- ColumnTransformer

### 7. Pipeline Construction

Built:

- Numerical preprocessing pipeline
- Full preprocessing pipeline

### 8. Model Training

#### Linear Regression

RMSE:

```text
68,232
```

#### Decision Tree

Training RMSE:

```text
0
```

Cross Validation RMSE:

```text
68,730
```

Result:

```text
Overfitting Detected
```

#### Random Forest

Cross Validation RMSE:

```text
48,901
```

Selected as final model.

---

## Model Training

### Linear Regression

RMSE: 68,232

### Decision Tree

Training RMSE: 0

Cross Validation RMSE: 68,730

### Random Forest

Cross Validation RMSE: 48,901

Selected as Final Model

---

## Hyperparameter Tuning

Used:

```python
GridSearchCV
```

Best Parameters:

```text
n_estimators = 30
max_features = 8
```

---

## Final Evaluation

Test RMSE:

```text
49,933
```

Final Model:

```text
RandomForestRegressor
```

---

## Production Components

### Model Artifacts

```text
models/
├── full_pipeline.joblib
├── price_model.joblib
└── metadata.json
```

### Monitoring

```text
logs/
└── predictions.log
```

### Metrics

```text
reports/
└── model_metrics.json
```

---

## API Service

### Predict House Price

```http
POST /predict
```

### Model Metadata

```http
GET /model-info
```

---

## Example Request

```json
{
  "longitude": -122.23,
  "latitude": 37.88,
  "housing_median_age": 41,
  "total_rooms": 880,
  "total_bedrooms": 129,
  "population": 322,
  "households": 126,
  "median_income": 8.3252,
  "ocean_proximity": "NEAR BAY"
}
```

---

## Example Response

```json
{
  "predicted_price": 445720.2,
  "decision": "DO_NOT_INVEST",
  "risk_level": "HIGH",
  "latency_ms": 12.8
}
```

---

## Monitoring

Implemented:

- Prediction Logging
- Latency Tracking
- Model Metadata Tracking
- Versioned Model Artifacts

---

## Repository Structure

```text
end-to-end-housing-ml-system/

├── app/
├── src/
├── models/
├── reports/
├── logs/
├── data/
├── notebooks/
├── README.md
└── requirements.txt
```

---

## Technologies Used

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy

### API Development

- FastAPI
- Pydantic
- Uvicorn

### Model Persistence

- Joblib

### Monitoring

- JSON Logging
- Latency Tracking

---

## Key Learning Outcomes

- End-to-end ML workflow design
- Feature engineering
- Model evaluation
- Hyperparameter tuning
- Pipeline serialization
- Model serving with FastAPI
- Prediction monitoring
- Production-style project architecture

---

## Future Improvements

- Docker containerization
- CI/CD pipelines
- Automated retraining
- Data drift detection
- Model performance monitoring
- Cloud deployment
- MLflow experiment tracking