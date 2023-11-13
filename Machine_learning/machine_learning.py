import pandas as pd
from ydata_profiling import ProfileReport

# dataset report
data = pd.read_csv("C:/Users/chngk/OneDrive/Desktop/Machine_learning/heart_disease_health_indicators_BRFSS2015.csv", sep=",", encoding='utf-8')
profile = ProfileReport(data)

# Print the profiling report
print(profile)

# preprocessing
data["HeartDiseaseorAttack"] = data["HeartDiseaseorAttack"].astype(int)
data["HighBP"] = data["HighBP"].astype(int)
data["HighChol"] = data["HighChol"].astype(int)
data["CholCheck"] = data["CholCheck"].astype(int)
data["BMI"] = data["BMI"].astype(int)
data["Smoker"] = data["Smoker"].astype(int)
data["Stroke"] = data["Stroke"].astype(int)
data["Diabetes"] = data["Diabetes"].astype(int)
data["PhysActivity"] = data["PhysActivity"].astype(int)
data["Fruits"] = data["Fruits"].astype(int) 
data["Veggies"] = data["Veggies"].astype(int)
data["HvyAlcoholConsump"] = data["HvyAlcoholConsump"].astype(int)
data["AnyHealthcare"] = data["AnyHealthcare"].astype(int)
data["NoDocbcCost"] = data["NoDocbcCost"].astype(int)
data["GenHlth"] = data["GenHlth"].astype(int)
data["MentHlth"] = data["MentHlth"].astype(int)
data["PhysHlth"] = data["PhysHlth"].astype(int)
data["DiffWalk"] = data["DiffWalk"].astype(int)
data["Sex"] = data["Sex"].astype(int)
data["Age"] = data["Age"].astype(int)
data["Education"] = data["Education"].astype(int)
data["Income"] = data["Income"].astype(int)

data.info()

# check null value
print(data.isnull().sum())

# checking unique values in different variables
unique_values = {}
for col in data.columns:
    unique_values[col] = data[col].value_counts().shape[0]

print(pd.DataFrame(unique_values, index=['unique value count']).transpose())

# check duplicated data
print(data.duplicated().sum())

# drop duplicated data
data.drop_duplicates(inplace=True)
