import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import yfinance as yf
from arch import arch_model
#
#   Use yfinance module to download data for two stocks and build GARCH(1,1) models for the
#   returns using the ARCH module. Plot out the results for volatility, standardised residuals
#   and the prices.
#
#   ITM is a high risk, loss making 'hydrogen economy' stock.
#   RELX is a highly profitable global corporation specialising in academic publishing.
#
stktick=['itm.l','rel.l']
#
st="2007-01-01"
stock1=yf.download(stktick[0],start=st)
print(stock1['Close'].head(20))
xr=np.log(stock1['Close']/stock1['Close'].shift(1))
am=arch_model(100.0*xr.iloc[1:])
res=am.fit(update_freq=5)
print(res.summary)
fig=res.plot(annualize='D')
plt.suptitle('ITM Power',fontweight='bold',fontsize=18)
plt.show()
#
stock2=yf.download(stktick[1],start=st)
print(stock2['Close'].tail())
wr=np.log(stock2['Close']/stock2['Close'].shift(1))
am=arch_model(100.0*wr.iloc[1:])
res=am.fit(update_freq=5)
print(res.summary)
fig=res.plot(annualize='D')
plt.suptitle('RELX',fontweight='bold',fontsize=18)
plt.show()
#
iclose=0
if iclose==0:  
    fig=plt.figure()
    plt.suptitle('A tale of two UK stocks',fontweight='bold',fontsize=18)
    ax=fig.add_subplot(2,1,1)
    ax.plot(stock1.index,stock1['Close'])
    plt.title('ITM Power')
    ax2=fig.add_subplot(2,1,2)
    ax2.plot(stock2.index,stock2['Close'])
    plt.title('RELX')
    plt.tight_layout()
    plt.show()
