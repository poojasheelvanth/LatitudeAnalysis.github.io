import pandas as pd
import csv

df = pd.read_csv("Resources\cities.csv")
df.to_html('DataCopy.html')