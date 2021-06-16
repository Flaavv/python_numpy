import pandas as pd
import io

df = pd.read_csv('house_pricing.csv')

# df.shape shows us number of rows and columns
print(df, type(df), df.shape)
print(df.info())

# Display ten first lines
print(df.head(10))

salePrice = df['SalePrice']
# affiche moyenne de prix
print('Moyenne prix de vente :', salePrice.mean())

#Donne plein d'infos statistiques
keyValue = df.describe()
print(keyValue)