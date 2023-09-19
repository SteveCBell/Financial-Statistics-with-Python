import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as npr
import math
#
#   Reads in currency data files, downloaded from the Bundesbank (ECB data though), from the folder 'ECB Currency Data'
#   Assigns each to a Pandas DataFrame. Swiss data has different format from the others so needed different processing.
#   Data import using dictionary will be demonstrated later in the course.
#   Data is then charted using matplotlib in a (2,3) array
#
DKrona=pd.read_csv('ECB Currency Data\DanishKrona.csv',skiprows=9,index_col=0,parse_dates=True,na_values='.')
Sterling=pd.read_csv('ECB Currency Data\Sterling.csv', skiprows=9,index_col=0,parse_dates=True,na_values='.')
Swiss=pd.read_csv('ECB Currency Data\SwissDollar.csv',skiprows=9,index_col=0,parse_dates=True,na_values='.',dayfirst=True)
Zloty=pd.read_csv('ECB Currency Data\PolishZloty.csv',skiprows=9,index_col=0,parse_dates=True,na_values='.')
TLira=pd.read_csv('ECB Currency Data\TurkishLira.csv',skiprows=9,index_col=0,parse_dates=True,na_values='.')
Scheckel=pd.read_csv('ECB Currency Data\IsraeliScheckel.csv',skiprows=9,index_col=0,parse_dates=True,na_values='.')
#
Currencies=[DKrona,Sterling,Swiss,Zloty,TLira,Scheckel]
Cnames=['Euro/DKrona','Euro/Sterling','Euro/Swiss','Euro/Zloty','Euro/TLira','Euro/Scheckel']
#
for currency in Currencies:
    currency.index.name='Date'                                 # Renames the index as 'Date'
    currency.drop(currency.columns[[1]],axis=1,inplace=True)   # removes a redundant column in the data
    currency.dropna(how='all',inplace=True)                    # removes NaN values
#
#   Note the use of 'inplace=True' above so that a copy of the DataFrame is not made.
#
for i,currency in enumerate(Currencies):
    currency.columns=[Cnames[i]]
#
Swiss['Euro/Swiss']=Swiss['Euro/Swiss'].apply(pd.to_numeric,errors='coerce')
#
plt.Figure(figsize=(7,5))
plt.suptitle('European Area Exchange Rates',fontweight='bold',fontsize=18)   # Creates an overall title for the array of charts.
#
for j in range(1,7):
    plt.subplot(2,3,j)
    plt.plot(Currencies[j-1])
    plt.xticks(rotation=45)
    plt.title(Cnames[j-1])
#
plt.tight_layout()      # ensures that chart titles are not overlaid on tick labels from above.
plt.show()


