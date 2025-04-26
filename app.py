import pandas as pd

df = pd.read_csv('dados/planetas.csv')

print("=== Explorador Astronômico: Top 5 planetas em massa ===")
print(df.nlargest(5, 'massa'))

print("\n=== Média da distância ao Sol (em AU) ===")
print(df['dist_sol'].mean())
