import pandas as pd
import matplotlib.pyplot as plt

col_names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data (1).csv' ,
                   names=col_names)
print(data.describe().to_csv('./results/describe.csv'))