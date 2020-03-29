import pandas as pd

df = pd.read_csv("population.csv", nrows= 2000)

# result = pd.DataFrame(df,columns=['yearofbirth'])


print(df)