import pandas as pd

ecom = pd.read_csv('./Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Ecommerce Purchases')

# print(ecom.describe())
# print(ecom.head())
print(ecom.columns)
print(ecom.shape[0], ecom.shape[1])
print(ecom['Purchase Price'].mean())
print('Max: ', ecom['Purchase Price'].max())
print('Min: ', ecom['Purchase Price'].min())

numEnglish = len(ecom[ecom['Language'] == 'en'])
print(numEnglish)

numLawyer = len(ecom[ecom['Job'] == 'Lawyer'])
print('Num lawyers: ', numLawyer)

AMPur = ecom[ecom['AM or PM'] == 'AM']
print('AM Purchases: ', len(AMPur))

PMPur = ecom[ecom['AM or PM'] == 'PM']
print('PM Purchases: ', len(PMPur))

print('Value counts: ', ecom['AM or PM'].value_counts())

jobTitles = ecom['Job'].value_counts().head(5)
print(jobTitles)

lot90WT = ecom[ecom['Lot'] == '90 WT']
print(lot90WT['Purchase Price'])

ccFind = ecom[ecom['Credit Card'] == 4926535242672853]
print(ccFind['Email'])

amProv = ecom[ecom['CC Provider'] == 'American Express']
bigPur = amProv[amProv['Purchase Price'] > 95]
print(len(bigPur))

ccExp = ecom['CC Exp Date']

def extract2025(ccExp):
    exp2025 = []
    for exp in ccExp:
        year = exp.split('/')
        if (year[1] == '25'):
            exp2025.append(year[1])
    return exp2025


exp2025 = extract2025(ccExp)
print(len(exp2025))

def addProviderCol(df):
    df['Provider'] = 'na'
    for index in range(0, len(df)):
        df.iat[index, 14] = df.iat[index, 9].split('@')[1]

    return df

ecomWithProvider = addProviderCol(ecom)
print(ecomWithProvider['Provider'].value_counts().head(5))

