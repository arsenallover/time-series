#!/usr/bin/env python
# coding: utf-8

# In[1]:


def adf_check(time_series):
    """
    Pass in a time series, returns ADF report
    """
    from statsmodels.tsa.stattools import adfuller
    
    result = adfuller(time_series)
    labels = ['ADF Test Statistic','p-value','Number of Lags Used','Number of Observations Used']

    for value,label in zip(result,labels):
        print(label+' : '+str(value) )
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis, reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary \n")

