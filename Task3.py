import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data= pd.read_csv("C:\\Users\\Mathivathanan\\Downloads\\householdtask3.csv")
data.head(10)

plt.scatter(data['year'],data['own'])
plt.title("Scatter Plot")
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.plot(data['year'])
plt.plot(data['own'])
plt.title("Line Plot")
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.bar(data['year'], data['own'])
plt.title("Bar Plot")
plt.xlabel('year')
plt.ylabel('own')
plt.show()

plt.hist(data['income'])
plt.title("Histogram")
plt.show()



