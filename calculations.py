import pandas as pd
import matplotlib.pyplot as plt

df_raw = pd.read_csv('analysisdata.csv')
print(df_raw.head(15))

#Cleaning of data
df = pd.read_csv('analysisdata.csv', skiprows=10, header=None)
df = df.dropna()
print(df.head(15))
print(df.info())

#Extraction of vals
df[0] = pd.to_numeric(df[0], errors='coerce')  #to remove errors like str
df[1] = pd.to_numeric(df[1], errors='coerce')  #to remove errors like str

displacement = df[0]
force = df[1]
print(displacement)
print(force)

#Analysis
initial_area = 100  #sq.mm
initial_length = 50 #mm

stress = force.to_numpy()/initial_area
strain = displacement.to_numpy()/initial_length

plt.figure(figsize=(10,6))
plt.plot(strain, stress, label='Stress-Strain curve')
plt.title('Stress-Strain curve from Tensile Test')
plt.legend()
plt.xlabel('Strain ()')
plt.ylabel('Stress (kN/mm^2)')
plt.grid(True)
plt.show()