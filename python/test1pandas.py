import pandas as pd
import seaborn as sns
import statistics as sts

dados = pd.read_csv("dados/Churn.csv", sep=";")
print(dados.head())

print(dados.shape)

dados.columns = ["Id", "Score", "Estado", "Genero", "Idade", "Patrimonio", "Saldo", "Produtos", "TemCartCredito", "Ativo", "Salario", "Saiu"]

print(dados.head())



