# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import linear_model
import seaborn as sns
from scipy.stats import skew 
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (12,8)

df = pd.read_excel (r'/Users/filippobalbo/Desktop/Tesi//Companies List/Companies.xlsx', 'Company')
A2A = df.iloc[0:13,1:8]
AMP = df.iloc[13:26,1:8]
ATL = df.iloc[26:39,1:8]
AZM = df.iloc[39:52,1:-1]
CPR = df.iloc[52:65,1:-1]
CNHI = df.iloc[65:78,1:-1]
DIA = df.iloc[78:91,1:-1]
ENEL = df.iloc[91:104,1:-1]
ENI = df.iloc[104:117,1:-1]
RACE = df.iloc[117:130,1:-1]
HER = df.iloc[130:143,1:-1]
IP = df.iloc[143:156,1:-1]
INW = df.iloc[156:169,1:-1]
IG = df.iloc[169:182,1:-1]
LDO = df.iloc[182:195,1:-1]
MONC = df.iloc[195:208,1:-1]
NEXI = df.iloc[208:221,1:-1]
PIRC = df.iloc[221:234,1:-1]
PST = df.iloc[234:247,1:-1]
PRY  = df.iloc[247:260,1:-1]
REC  = df.iloc[260:273,1:-1]
SPM  = df.iloc[273:286,1:-1]
SRG  = df.iloc[286:299,1:-1]
STLA  = df.iloc[299:312,1:-1]
STM  = df.iloc[312:325,1:-1]
TIT  = df.iloc[325:338,1:-1]
TEN  = df.iloc[338:351,1:-1]
TRN  = df.iloc[351:,1:-1]

companies = {A2A,AMP,ATL,AZM,CPR,CNHI,DIA,ENEL,ENI,RACE,HER,IP,INW,IG,LDO,MONC,NEXI,PIRC,PST,PRY,REC,SPM,SRG,STLA,STM,TIT,TEN,TRN}

    
#------ (1) - A2A -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from sklearn import preprocessing
# d = preprocessing.normalize(A2A)
# scaled_df = pd.DataFrame(d)

# a2a_T = scaled_df.T
# a2a_T.columns = ['Credit_Rating','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']
# a2a_T = a2a_T.iloc[::-1]

# # Risk Regression:
# A2A_X_Risk = a2a_T[['ROA','ESG_Score','Tot_Asset','Tot_Revenue','Debt_E_Ratio']]
# A2A_y_Risk = a2a_T[['Credit_Rating']]
# A2A_X0 = sm.add_constant(A2A_X_Risk)
# A2A_est = sm.OLS(A2A_y_Risk, A2A_X0)
# A2A_est1 = A2A_est.fit()
# print(A2A_est1.summary())

# # Performance Regression
# A2A_X_Perf = a2a_T[['ESG_Score','Debt_E_Ratio','Tot_Revenue','Credit_Rating']]
# A2A_y_Perf = a2a_T[['ROA']]
# A2A_X1 = sm.add_constant(A2A_X_Perf)
# A2A_Perf  = sm.OLS(A2A_y_Perf, A2A_X1)
# A2A_Perf2 = A2A_Perf.fit()
# print(A2A_Perf2.summary())

# # Risk Channel Regression:
# A2A_X_Channel_Risk = a2a_T[['ROA','E_Score','S_Score','G_Score','Debt_E_Ratio']]
# A2A_y_Channel_Risk = a2a_T[['Credit_Rating']]
# A2A_Channel_X0 = sm.add_constant(A2A_X_Channel_Risk)
# A2A_Channel_Risk  = sm.OLS(A2A_y_Channel_Risk, A2A_Channel_X0)
# A2A_Channel_Risk2 = A2A_Channel_Risk.fit()
# print(A2A_Channel_Risk2.summary())

# # Performance Channel Regression
# A2A_X_Channel_Perf = a2a_T[['Tot_Revenue','E_Score','S_Score','G_Score','Debt_E_Ratio']]
# A2A_y_Channel_Perf = a2a_T[['ROA']]
# A2A_Channel_X1 = sm.add_constant(A2A_X_Channel_Perf)
# A2A_Channel_Perf  = sm.OLS(A2A_y_Channel_Perf, A2A_Channel_X1)
# A2A_Channel_Perf2 = A2A_Channel_Perf.fit()
# print(A2A_Channel_Perf2.summary())


    
# #------ (2) - AMP -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# from sklearn import preprocessing
# d = preprocessing.normalize(AMP)
# scaled_df = pd.DataFrame(d)

# AMP_T = scaled_df.T
# AMP_T.columns = ['Credit_Rating','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']
# AMP_T = AMP_T.iloc[::-1]

# # Risk Regression:
# AMP_X_Risk = AMP_T[['ROA','ESG_Score','Tot_Asset','Tot_Revenue','Debt_E_Ratio']]
# AMP_y_Risk = AMP_T[['Credit_Rating']]
# AMP_X0 = sm.add_constant(AMP_X_Risk)
# AMP_est = sm.OLS(AMP_y_Risk, AMP_X0)
# AMP_est1 = AMP_est.fit()
# print(AMP_est1.summary())

# # Performance Regression
# AMP_X_Perf = AMP_T[['ESG_Score','Debt_E_Ratio','Tot_Revenue','Credit_Rating']]
# AMP_y_Perf = AMP_T[['ROA']]
# AMP_X1 = sm.add_constant(AMP_X_Perf)
# AMP_Perf  = sm.OLS(AMP_y_Perf, AMP_X1)
# AMP_Perf2 = AMP_Perf.fit()
# print(AMP_Perf2.summary())

# # Risk Channel Regression:
# AMP_X_Channel_Risk = AMP_T[['ROA','E_Score','S_Score','G_Score','Debt_E_Ratio']]
# AMP_y_Channel_Risk = AMP_T[['Credit_Rating']]
# AMP_Channel_X0 = sm.add_constant(AMP_X_Channel_Risk)
# AMP_Channel_Risk  = sm.OLS(AMP_y_Channel_Risk, AMP_Channel_X0)
# AMP_Channel_Risk2 = AMP_Channel_Risk.fit()
# print(AMP_Channel_Risk2.summary())

# # Performance Channel Regression
# AMP_X_Channel_Perf = AMP_T[['Tot_Revenue','E_Score','S_Score','G_Score','Debt_E_Ratio']]
# AMP_y_Channel_Perf = AMP_T[['ROA']]
# AMP_Channel_X1 = sm.add_constant(AMP_X_Channel_Perf)
# AMP_Channel_Perf  = sm.OLS(AMP_y_Channel_Perf, AMP_Channel_X1)
# AMP_Channel_Perf2 = AMP_Channel_Perf.fit()
# print(AMP_Channel_Perf2.summary())


    
# #------ (3) - ATL -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(ATL)
scaled_df = pd.DataFrame(d)

ATL_T = scaled_df.T
ATL_T.columns = ['Credit_Rating','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']


# Risk Regression:
ATL_X_Risk = ATL_T[['ROA','ESG_Score','Tot_Asset','Tot_Revenue','Debt_E_Ratio']]
ATL_y_Risk = ATL_T[['Credit_Rating']]
ATL_X0 = sm.add_constant(ATL_X_Risk)
ATL_est = sm.OLS(ATL_y_Risk, ATL_X0)
ATL_est1 = ATL_est.fit()
print(ATL_est1.summary())

# Performance Regression
ATL_X_Perf = ATL_T[['ESG_Score','Debt_E_Ratio','Tot_Revenue','Credit_Rating']]
ATL_y_Perf = ATL_T[['ROA']]
ATL_X1 = sm.add_constant(ATL_X_Perf)
ATL_Perf  = sm.OLS(ATL_y_Perf, ATL_X1)
ATL_Perf2 = ATL_Perf.fit()
print(ATL_Perf2.summary())

# Risk Channel Regression:
ATL_X_Channel_Risk = ATL_T[['ROA','E_Score','S_Score','G_Score','Debt_E_Ratio']]
ATL_y_Channel_Risk = ATL_T[['Credit_Rating']]
ATL_Channel_X0 = sm.add_constant(ATL_X_Channel_Risk)
ATL_Channel_Risk  = sm.OLS(ATL_y_Channel_Risk, ATL_Channel_X0)
ATL_Channel_Risk2 = ATL_Channel_Risk.fit()
print(ATL_Channel_Risk2.summary())

# Performance Channel Regression
ATL_X_Channel_Perf = ATL_T[['Tot_Revenue','E_Score','S_Score','G_Score','Debt_E_Ratio']]
ATL_y_Channel_Perf = ATL_T[['ROA']]
ATL_Channel_X1 = sm.add_constant(ATL_X_Channel_Perf)
ATL_Channel_Perf  = sm.OLS(ATL_y_Channel_Perf, ATL_Channel_X1)
ATL_Channel_Perf2 = ATL_Channel_Perf.fit()
print(ATL_Channel_Perf2.summary())

    
# #------ (4) - AZM -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(AZM)
scaled_df = pd.DataFrame(d)

AZM_T = scaled_df.T
AZM_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
AZM_X_Risk = AZM_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
AZM_y_Risk = AZM_T[['Credit_Raiting']]
AZM_reg_Risk = linear_model.LinearRegression()
AZM_reg_Risk.fit(AZM_X_Risk,AZM_y_Risk)
AZM_b_Risk = AZM_reg_Risk.coef_
AZM_b0_Risk=AZM_reg_Risk.intercept_

# Performance Regression
AZM_X_Perf = AZM_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
AZM_y_Perf = AZM_T[['ROA']]
AZM_reg_Perf = linear_model.LinearRegression()
AZM_reg_Perf.fit(AZM_X_Perf,AZM_y_Perf)
AZM_b_Perf = AZM_reg_Perf.coef_
AZM_b0_Perf= AZM_reg_Perf.intercept_

# Risk Channel Regression:
AZM_X_Channel_Risk = AZM_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
AZM_y_Channel_Risk = AZM_T[['Credit_Raiting']]
AZM_reg_Channel_Risk = linear_model.LinearRegression()
AZM_reg_Channel_Risk.fit(AZM_X_Channel_Risk,AZM_y_Channel_Risk)
AZM_b_Channel_Risk = AZM_reg_Channel_Risk.coef_
AZM_b0_Channel_Risk= AZM_reg_Channel_Risk.intercept_

# Performance Channel Regression
AZM_X_Channel_Perf = AZM_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
AZM_y_Channel_Perf = AZM_T[['ROA']]
AZM_reg_Channel_Perf = linear_model.LinearRegression()
AZM_reg_Channel_Perf.fit(AZM_X_Channel_Perf,AZM_y_Channel_Perf)
AZM_b_Channel_Perf = AZM_reg_Channel_Perf.coef_
AZM_b0_Channel_Perf= AZM_reg_Channel_Perf.intercept_

    
# #------ (5) - CNHI -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(CNHI)
scaled_df = pd.DataFrame(d)

CNHI_T = scaled_df.T
CNHI_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
CNHI_X_Risk = CNHI_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
CNHI_y_Risk = CNHI_T[['Credit_Raiting']]
CNHI_reg_Risk = linear_model.LinearRegression()
CNHI_reg_Risk.fit(CNHI_X_Risk,CNHI_y_Risk)
CNHI_b_Risk = CNHI_reg_Risk.coef_
CNHI_b0_Risk= CNHI_reg_Risk.intercept_

# Performance Regression
CNHI_X_Perf = CNHI_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
CNHI_y_Perf = CNHI_T[['ROA']]
CNHI_reg_Perf = linear_model.LinearRegression()
CNHI_reg_Perf.fit(CNHI_X_Perf,CNHI_y_Perf)
CNHI_b_Perf = CNHI_reg_Perf.coef_
CNHI_b0_Perf= CNHI_reg_Perf.intercept_

# Risk Channel Regression:
CNHI_X_Channel_Risk = CNHI_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
CNHI_y_Channel_Risk = CNHI_T[['Credit_Raiting']]
CNHI_reg_Channel_Risk = linear_model.LinearRegression()
CNHI_reg_Channel_Risk.fit(CNHI_X_Channel_Risk,CNHI_y_Channel_Risk)
CNHI_b_Channel_Risk = CNHI_reg_Channel_Risk.coef_
CNHI_b0_Channel_Risk= CNHI_reg_Channel_Risk.intercept_

# Performance Channel Regression
CNHI_X_Channel_Perf = CNHI_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
CNHI_y_Channel_Perf = CNHI_T[['ROA']]
CNHI_reg_Channel_Perf = linear_model.LinearRegression()
CNHI_reg_Channel_Perf.fit(CNHI_X_Channel_Perf,CNHI_y_Channel_Perf)
CNHI_b_Channel_Perf = CNHI_reg_Channel_Perf.coef_
CNHI_b0_Channel_Perf= CNHI_reg_Channel_Perf.intercept_

    
# #------ (6) - CPR -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(CPR)
scaled_df = pd.DataFrame(d)

CPR_T = scaled_df.T
CPR_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
CPR_X_Risk = CPR_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
CPR_y_Risk = CPR_T[['Credit_Raiting']]
CPR_reg_Risk = linear_model.LinearRegression()
CPR_reg_Risk.fit(CPR_X_Risk,CPR_y_Risk)
CPR_b_Risk = CPR_reg_Risk.coef_
CPR_b0_Risk= CPR_reg_Risk.intercept_

# Performance Regression
CPR_X_Perf = CPR_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
CPR_y_Perf = CPR_T[['ROA']]
CPR_reg_Perf = linear_model.LinearRegression()
CPR_reg_Perf.fit(CPR_X_Perf,CPR_y_Perf)
CPR_b_Perf = CPR_reg_Perf.coef_
CPR_b0_Perf= CPR_reg_Perf.intercept_

# Risk Channel Regression:
CPR_X_Channel_Risk = CPR_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
CPR_y_Channel_Risk = CPR_T[['Credit_Raiting']]
CPR_reg_Channel_Risk = linear_model.LinearRegression()
CPR_reg_Channel_Risk.fit(CPR_X_Channel_Risk,CPR_y_Channel_Risk)
CPR_b_Channel_Risk = CPR_reg_Channel_Risk.coef_
CPR_b0_Channel_Risk= CPR_reg_Channel_Risk.intercept_

# Performance Channel Regression
CPR_X_Channel_Perf = CPR_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
CPR_y_Channel_Perf = CPR_T[['ROA']]
CPR_reg_Channel_Perf = linear_model.LinearRegression()
CPR_reg_Channel_Perf.fit(CPR_X_Channel_Perf,CPR_y_Channel_Perf)
CPR_b_Channel_Perf = CPR_reg_Channel_Perf.coef_
CPR_b0_Channel_Perf= CPR_reg_Channel_Perf.intercept_
    
# #------ (7) - DIA -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(DIA)
scaled_df = pd.DataFrame(d)

DIA_T = scaled_df.T
DIA_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
DIA_X_Risk = DIA_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
DIA_y_Risk = DIA_T[['Credit_Raiting']]
DIA_reg_Risk = linear_model.LinearRegression()
DIA_reg_Risk.fit(DIA_X_Risk,DIA_y_Risk)
DIA_b_Risk = DIA_reg_Risk.coef_
DIA_b0_Risk= DIA_reg_Risk.intercept_

# Performance Regression
DIA_X_Perf = DIA_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
DIA_y_Perf = DIA_T[['ROA']]
DIA_reg_Perf = linear_model.LinearRegression()
DIA_reg_Perf.fit(DIA_X_Perf,DIA_y_Perf)
DIA_b_Perf = DIA_reg_Perf.coef_
DIA_b0_Perf= DIA_reg_Perf.intercept_

# Risk Channel Regression:
DIA_X_Channel_Risk = DIA_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
DIA_y_Channel_Risk = DIA_T[['Credit_Raiting']]
DIA_reg_Channel_Risk = linear_model.LinearRegression()
DIA_reg_Channel_Risk.fit(DIA_X_Channel_Risk,DIA_y_Channel_Risk)
DIA_b_Channel_Risk = DIA_reg_Channel_Risk.coef_
DIA_b0_Channel_Risk= DIA_reg_Channel_Risk.intercept_

# Performance Channel Regression
DIA_X_Channel_Perf = DIA_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
DIA_y_Channel_Perf = DIA_T[['ROA']]
DIA_reg_Channel_Perf = linear_model.LinearRegression()
DIA_reg_Channel_Perf.fit(DIA_X_Channel_Perf,DIA_y_Channel_Perf)
DIA_b_Channel_Perf = DIA_reg_Channel_Perf.coef_
DIA_b0_Channel_Perf= DIA_reg_Channel_Perf.intercept_

    
# #------ (8) - ENEL -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(ENEL)
scaled_df = pd.DataFrame(d)

ENEL_T = scaled_df.T
ENEL_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
ENEL_X_Risk = ENEL_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
ENEL_y_Risk = ENEL_T[['Credit_Raiting']]
ENEL_reg_Risk = linear_model.LinearRegression()
ENEL_reg_Risk.fit(ENEL_X_Risk,ENEL_y_Risk)
ENEL_b_Risk = ENEL_reg_Risk.coef_
ENEL_b0_Risk= ENEL_reg_Risk.intercept_

# Performance Regression
ENEL_X_Perf = ENEL_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
ENEL_y_Perf = ENEL_T[['ROA']]
ENEL_reg_Perf = linear_model.LinearRegression()
ENEL_reg_Perf.fit(ENEL_X_Perf,ENEL_y_Perf)
ENEL_b_Perf = ENEL_reg_Perf.coef_
ENEL_b0_Perf= ENEL_reg_Perf.intercept_

# Risk Channel Regression:
ENEL_X_Channel_Risk = ENEL_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
ENEL_y_Channel_Risk = ENEL_T[['Credit_Raiting']]
ENEL_reg_Channel_Risk = linear_model.LinearRegression()
ENEL_reg_Channel_Risk.fit(ENEL_X_Channel_Risk,ENEL_y_Channel_Risk)
ENEL_b_Channel_Risk = ENEL_reg_Channel_Risk.coef_
ENEL_b0_Channel_Risk= ENEL_reg_Channel_Risk.intercept_

# Performance Channel Regression
ENEL_X_Channel_Perf = ENEL_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
ENEL_y_Channel_Perf = ENEL_T[['ROA']]
ENEL_reg_Channel_Perf = linear_model.LinearRegression()
ENEL_reg_Channel_Perf.fit(ENEL_X_Channel_Perf,ENEL_y_Channel_Perf)
ENEL_b_Channel_Perf = ENEL_reg_Channel_Perf.coef_
ENEL_b0_Channel_Perf= ENEL_reg_Channel_Perf.intercept_

    
# #------ (9) - ENI -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(ENI)
scaled_df = pd.DataFrame(d)

ENI_T = scaled_df.T
ENI_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
ENI_X_Risk = ENI_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
ENI_y_Risk = ENI_T[['Credit_Raiting']]
ENI_reg_Risk = linear_model.LinearRegression()
ENI_reg_Risk.fit(ENI_X_Risk,ENI_y_Risk)
ENI_b_Risk = ENI_reg_Risk.coef_
ENI_b0_Risk= ENI_reg_Risk.intercept_

# Performance Regression
ENI_X_Perf = ENI_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
ENI_y_Perf = ENI_T[['ROA']]
ENI_reg_Perf = linear_model.LinearRegression()
ENI_reg_Perf.fit(ENI_X_Perf,ENI_y_Perf)
ENI_b_Perf = ENI_reg_Perf.coef_
ENI_b0_Perf= ENI_reg_Perf.intercept_

# Risk Channel Regression:
ENI_X_Channel_Risk = ENI_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
ENI_y_Channel_Risk = ENI_T[['Credit_Raiting']]
ENI_reg_Channel_Risk = linear_model.LinearRegression()
ENI_reg_Channel_Risk.fit(ENI_X_Channel_Risk,ENI_y_Channel_Risk)
ENI_b_Channel_Risk = ENI_reg_Channel_Risk.coef_
ENI_b0_Channel_Risk= ENI_reg_Channel_Risk.intercept_

# Performance Channel Regression
ENI_X_Channel_Perf = ENI_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
ENI_y_Channel_Perf = ENI_T[['ROA']]
ENI_reg_Channel_Perf = linear_model.LinearRegression()
ENI_reg_Channel_Perf.fit(ENI_X_Channel_Perf,ENI_y_Channel_Perf)
ENI_b_Channel_Perf = ENI_reg_Channel_Perf.coef_
ENI_b0_Channel_Perf= ENI_reg_Channel_Perf.intercept_

    
# #------ (10) - HER -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(HER)
scaled_df = pd.DataFrame(d)

HER_T = scaled_df.T
HER_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
HER_X_Risk = HER_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
HER_y_Risk = HER_T[['Credit_Raiting']]
HER_reg_Risk = linear_model.LinearRegression()
HER_reg_Risk.fit(HER_X_Risk,HER_y_Risk)
HER_b_Risk = HER_reg_Risk.coef_
HER_b0_Risk= HER_reg_Risk.intercept_

# Performance Regression
HER_X_Perf = HER_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
HER_y_Perf = HER_T[['ROA']]
HER_reg_Perf = linear_model.LinearRegression()
HER_reg_Perf.fit(HER_X_Perf,HER_y_Perf)
HER_b_Perf = HER_reg_Perf.coef_
HER_b0_Perf= HER_reg_Perf.intercept_

# Risk Channel Regression:
HER_X_Channel_Risk = HER_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
HER_y_Channel_Risk = HER_T[['Credit_Raiting']]
HER_reg_Channel_Risk = linear_model.LinearRegression()
HER_reg_Channel_Risk.fit(HER_X_Channel_Risk,HER_y_Channel_Risk)
HER_b_Channel_Risk = HER_reg_Channel_Risk.coef_
HER_b0_Channel_Risk= HER_reg_Channel_Risk.intercept_

# Performance Channel Regression
HER_X_Channel_Perf = HER_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
HER_y_Channel_Perf = HER_T[['ROA']]
HER_reg_Channel_Perf = linear_model.LinearRegression()
HER_reg_Channel_Perf.fit(HER_X_Channel_Perf,HER_y_Channel_Perf)
HER_b_Channel_Perf = HER_reg_Channel_Perf.coef_
HER_b0_Channel_Perf= HER_reg_Channel_Perf.intercept_

    
# #------ (11) - IG -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(IG)
scaled_df = pd.DataFrame(d)

IG_T = scaled_df.T
IG_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
IG_X_Risk = IG_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
IG_y_Risk = IG_T[['Credit_Raiting']]
IG_reg_Risk = linear_model.LinearRegression()
IG_reg_Risk.fit(IG_X_Risk,IG_y_Risk)
IG_b_Risk = IG_reg_Risk.coef_
IG_b0_Risk= IG_reg_Risk.intercept_

# Performance Regression
IG_X_Perf = IG_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
IG_y_Perf = IG_T[['ROA']]
IG_reg_Perf = linear_model.LinearRegression()
IG_reg_Perf.fit(IG_X_Perf,IG_y_Perf)
IG_b_Perf = IG_reg_Perf.coef_
IG_b0_Perf= IG_reg_Perf.intercept_

# Risk Channel Regression:
IG_X_Channel_Risk = IG_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
IG_y_Channel_Risk = IG_T[['Credit_Raiting']]
IG_reg_Channel_Risk = linear_model.LinearRegression()
IG_reg_Channel_Risk.fit(IG_X_Channel_Risk,IG_y_Channel_Risk)
IG_b_Channel_Risk = IG_reg_Channel_Risk.coef_
IG_b0_Channel_Risk= IG_reg_Channel_Risk.intercept_

# Performance Channel Regression
IG_X_Channel_Perf = IG_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
IG_y_Channel_Perf = IG_T[['ROA']]
IG_reg_Channel_Perf = linear_model.LinearRegression()
IG_reg_Channel_Perf.fit(IG_X_Channel_Perf,IG_y_Channel_Perf)
IG_b_Channel_Perf = IG_reg_Channel_Perf.coef_
IG_b0_Channel_Perf= IG_reg_Channel_Perf.intercept_

    
# #------ (12) - INW -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(INW)
scaled_df = pd.DataFrame(d)

INW_T = scaled_df.T
INW_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
INW_X_Risk = INW_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
INW_y_Risk = INW_T[['Credit_Raiting']]
INW_reg_Risk = linear_model.LinearRegression()
INW_reg_Risk.fit(INW_X_Risk,INW_y_Risk)
INW_b_Risk = INW_reg_Risk.coef_
INW_b0_Risk= INW_reg_Risk.intercept_

# Performance Regression
INW_X_Perf = INW_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
INW_y_Perf = INW_T[['ROA']]
INW_reg_Perf = linear_model.LinearRegression()
INW_reg_Perf.fit(INW_X_Perf,INW_y_Perf)
INW_b_Perf = INW_reg_Perf.coef_
INW_b0_Perf= INW_reg_Perf.intercept_

# Risk Channel Regression:
INW_X_Channel_Risk = INW_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
INW_y_Channel_Risk = INW_T[['Credit_Raiting']]
INW_reg_Channel_Risk = linear_model.LinearRegression()
INW_reg_Channel_Risk.fit(INW_X_Channel_Risk,INW_y_Channel_Risk)
INW_b_Channel_Risk = INW_reg_Channel_Risk.coef_
INW_b0_Channel_Risk= INW_reg_Channel_Risk.intercept_

# Performance Channel Regression
INW_X_Channel_Perf = INW_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
INW_y_Channel_Perf = INW_T[['ROA']]
INW_reg_Channel_Perf = linear_model.LinearRegression()
INW_reg_Channel_Perf.fit(INW_X_Channel_Perf,INW_y_Channel_Perf)
INW_b_Channel_Perf = INW_reg_Channel_Perf.coef_
INW_b0_Channel_Perf= INW_reg_Channel_Perf.intercept_

    
# #------ (13) - IP -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(IP)
scaled_df = pd.DataFrame(d)

IP_T = scaled_df.T
IP_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
IP_X_Risk = IP_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
IP_y_Risk = IP_T[['Credit_Raiting']]
IP_reg_Risk = linear_model.LinearRegression()
IP_reg_Risk.fit(IP_X_Risk,IP_y_Risk)
IP_b_Risk = IP_reg_Risk.coef_
IP_b0_Risk= IP_reg_Risk.intercept_

# Performance Regression
IP_X_Perf = IP_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
IP_y_Perf = IP_T[['ROA']]
IP_reg_Perf = linear_model.LinearRegression()
IP_reg_Perf.fit(IP_X_Perf,IP_y_Perf)
IP_b_Perf = IP_reg_Perf.coef_
IP_b0_Perf= IP_reg_Perf.intercept_

# Risk Channel Regression:
IP_X_Channel_Risk = IP_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
IP_y_Channel_Risk = IP_T[['Credit_Raiting']]
IP_reg_Channel_Risk = linear_model.LinearRegression()
IP_reg_Channel_Risk.fit(IP_X_Channel_Risk,IP_y_Channel_Risk)
IP_b_Channel_Risk = IP_reg_Channel_Risk.coef_
IP_b0_Channel_Risk= IP_reg_Channel_Risk.intercept_

# Performance Channel Regression
IP_X_Channel_Perf = IP_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
IP_y_Channel_Perf = IP_T[['ROA']]
IP_reg_Channel_Perf = linear_model.LinearRegression()
IP_reg_Channel_Perf.fit(IP_X_Channel_Perf,IP_y_Channel_Perf)
IP_b_Channel_Perf = IP_reg_Channel_Perf.coef_
IP_b0_Channel_Perf= IP_reg_Channel_Perf.intercept_

    
# #------ (14) - LDO -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(LDO)
scaled_df = pd.DataFrame(d)

LDO_T = scaled_df.T
LDO_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
LDO_X_Risk = LDO_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
LDO_y_Risk = LDO_T[['Credit_Raiting']]
LDO_reg_Risk = linear_model.LinearRegression()
LDO_reg_Risk.fit(LDO_X_Risk,LDO_y_Risk)
LDO_b_Risk = LDO_reg_Risk.coef_
LDO_b0_Risk= LDO_reg_Risk.intercept_

# Performance Regression
LDO_X_Perf = LDO_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
LDO_y_Perf = LDO_T[['ROA']]
LDO_reg_Perf = linear_model.LinearRegression()
LDO_reg_Perf.fit(LDO_X_Perf,LDO_y_Perf)
LDO_b_Perf = LDO_reg_Perf.coef_
LDO_b0_Perf= LDO_reg_Perf.intercept_

# Risk Channel Regression:
LDO_X_Channel_Risk = LDO_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
LDO_y_Channel_Risk = LDO_T[['Credit_Raiting']]
LDO_reg_Channel_Risk = linear_model.LinearRegression()
LDO_reg_Channel_Risk.fit(LDO_X_Channel_Risk,LDO_y_Channel_Risk)
LDO_b_Channel_Risk = LDO_reg_Channel_Risk.coef_
LDO_b0_Channel_Risk= LDO_reg_Channel_Risk.intercept_

# Performance Channel Regression
LDO_X_Channel_Perf = LDO_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
LDO_y_Channel_Perf = LDO_T[['ROA']]
LDO_reg_Channel_Perf = linear_model.LinearRegression()
LDO_reg_Channel_Perf.fit(LDO_X_Channel_Perf,LDO_y_Channel_Perf)
LDO_b_Channel_Perf = LDO_reg_Channel_Perf.coef_
LDO_b0_Channel_Perf= LDO_reg_Channel_Perf.intercept_

    
# #------ (15) - MONC -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(MONC)
scaled_df = pd.DataFrame(d)

MONC_T = scaled_df.T
MONC_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
MONC_X_Risk = MONC_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
MONC_y_Risk = MONC_T[['Credit_Raiting']]
MONC_reg_Risk = linear_model.LinearRegression()
MONC_reg_Risk.fit(MONC_X_Risk,MONC_y_Risk)
MONC_b_Risk = MONC_reg_Risk.coef_
MONC_b0_Risk= MONC_reg_Risk.intercept_

# Performance Regression
MONC_X_Perf = MONC_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
MONC_y_Perf = MONC_T[['ROA']]
MONC_reg_Perf = linear_model.LinearRegression()
MONC_reg_Perf.fit(MONC_X_Perf,MONC_y_Perf)
MONC_b_Perf = MONC_reg_Perf.coef_
MONC_b0_Perf= MONC_reg_Perf.intercept_

# Risk Channel Regression:
MONC_X_Channel_Risk = MONC_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
MONC_y_Channel_Risk = MONC_T[['Credit_Raiting']]
MONC_reg_Channel_Risk = linear_model.LinearRegression()
MONC_reg_Channel_Risk.fit(MONC_X_Channel_Risk,MONC_y_Channel_Risk)
MONC_b_Channel_Risk = MONC_reg_Channel_Risk.coef_
MONC_b0_Channel_Risk= MONC_reg_Channel_Risk.intercept_

# Performance Channel Regression
MONC_X_Channel_Perf = MONC_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
MONC_y_Channel_Perf = MONC_T[['ROA']]
MONC_reg_Channel_Perf = linear_model.LinearRegression()
MONC_reg_Channel_Perf.fit(MONC_X_Channel_Perf,MONC_y_Channel_Perf)
MONC_b_Channel_Perf = MONC_reg_Channel_Perf.coef_
MONC_b0_Channel_Perf= MONC_reg_Channel_Perf.intercept_

    
# #------ (16) - NEXI -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(NEXI)
scaled_df = pd.DataFrame(d)

NEXI_T = scaled_df.T
NEXI_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
NEXI_X_Risk = NEXI_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
NEXI_y_Risk = NEXI_T[['Credit_Raiting']]
NEXI_reg_Risk = linear_model.LinearRegression()
NEXI_reg_Risk.fit(NEXI_X_Risk,NEXI_y_Risk)
NEXI_b_Risk = NEXI_reg_Risk.coef_
NEXI_b0_Risk= NEXI_reg_Risk.intercept_

# Performance Regression
NEXI_X_Perf = NEXI_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
NEXI_y_Perf = NEXI_T[['ROA']]
NEXI_reg_Perf = linear_model.LinearRegression()
NEXI_reg_Perf.fit(NEXI_X_Perf,NEXI_y_Perf)
NEXI_b_Perf = NEXI_reg_Perf.coef_
NEXI_b0_Perf= NEXI_reg_Perf.intercept_

# Risk Channel Regression:
NEXI_X_Channel_Risk = NEXI_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
NEXI_y_Channel_Risk = NEXI_T[['Credit_Raiting']]
NEXI_reg_Channel_Risk = linear_model.LinearRegression()
NEXI_reg_Channel_Risk.fit(NEXI_X_Channel_Risk,NEXI_y_Channel_Risk)
NEXI_b_Channel_Risk = NEXI_reg_Channel_Risk.coef_
NEXI_b0_Channel_Risk= NEXI_reg_Channel_Risk.intercept_

# Performance Channel Regression
NEXI_X_Channel_Perf = NEXI_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
NEXI_y_Channel_Perf = NEXI_T[['ROA']]
NEXI_reg_Channel_Perf = linear_model.LinearRegression()
NEXI_reg_Channel_Perf.fit(NEXI_X_Channel_Perf,NEXI_y_Channel_Perf)
NEXI_b_Channel_Perf = NEXI_reg_Channel_Perf.coef_
NEXI_b0_Channel_Perf= NEXI_reg_Channel_Perf.intercept_

    
# #------ (17) - PIRC -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(PIRC)
scaled_df = pd.DataFrame(d)

PIRC_T = scaled_df.T
PIRC_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
PIRC_X_Risk = PIRC_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PIRC_y_Risk = PIRC_T[['Credit_Raiting']]
PIRC_reg_Risk = linear_model.LinearRegression()
PIRC_reg_Risk.fit(PIRC_X_Risk,PIRC_y_Risk)
PIRC_b_Risk = PIRC_reg_Risk.coef_
PIRC_b0_Risk= PIRC_reg_Risk.intercept_

# Performance Regression
PIRC_X_Perf = PIRC_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PIRC_y_Perf = PIRC_T[['ROA']]
PIRC_reg_Perf = linear_model.LinearRegression()
PIRC_reg_Perf.fit(PIRC_X_Perf,PIRC_y_Perf)
PIRC_b_Perf = PIRC_reg_Perf.coef_
PIRC_b0_Perf= PIRC_reg_Perf.intercept_

# Risk Channel Regression:
PIRC_X_Channel_Risk = PIRC_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PIRC_y_Channel_Risk = PIRC_T[['Credit_Raiting']]
PIRC_reg_Channel_Risk = linear_model.LinearRegression()
PIRC_reg_Channel_Risk.fit(PIRC_X_Channel_Risk,PIRC_y_Channel_Risk)
PIRC_b_Channel_Risk = PIRC_reg_Channel_Risk.coef_
PIRC_b0_Channel_Risk= PIRC_reg_Channel_Risk.intercept_

# Performance Channel Regression
PIRC_X_Channel_Perf = PIRC_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PIRC_y_Channel_Perf = PIRC_T[['ROA']]
PIRC_reg_Channel_Perf = linear_model.LinearRegression()
PIRC_reg_Channel_Perf.fit(PIRC_X_Channel_Perf,PIRC_y_Channel_Perf)
PIRC_b_Channel_Perf = PIRC_reg_Channel_Perf.coef_
PIRC_b0_Channel_Perf= PIRC_reg_Channel_Perf.intercept_

    
# #------ (18) - PRY -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(PRY)
scaled_df = pd.DataFrame(d)

PRY_T = scaled_df.T
PRY_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
PRY_X_Risk = PRY_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PRY_y_Risk = PRY_T[['Credit_Raiting']]
PRY_reg_Risk = linear_model.LinearRegression()
PRY_reg_Risk.fit(PRY_X_Risk,PRY_y_Risk)
PRY_b_Risk = PRY_reg_Risk.coef_
PRY_b0_Risk= PRY_reg_Risk.intercept_

# Performance Regression
PRY_X_Perf = PRY_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PRY_y_Perf = PRY_T[['ROA']]
PRY_reg_Perf = linear_model.LinearRegression()
PRY_reg_Perf.fit(PRY_X_Perf,PRY_y_Perf)
PRY_b_Perf = PRY_reg_Perf.coef_
PRY_b0_Perf= PRY_reg_Perf.intercept_

# Risk Channel Regression:
PRY_X_Channel_Risk = PRY_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PRY_y_Channel_Risk = PRY_T[['Credit_Raiting']]
PRY_reg_Channel_Risk = linear_model.LinearRegression()
PRY_reg_Channel_Risk.fit(PRY_X_Channel_Risk,PRY_y_Channel_Risk)
PRY_b_Channel_Risk = PRY_reg_Channel_Risk.coef_
PRY_b0_Channel_Risk= PRY_reg_Channel_Risk.intercept_

# Performance Channel Regression
PRY_X_Channel_Perf = PRY_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PRY_y_Channel_Perf = PRY_T[['ROA']]
PRY_reg_Channel_Perf = linear_model.LinearRegression()
PRY_reg_Channel_Perf.fit(PRY_X_Channel_Perf,PRY_y_Channel_Perf)
PRY_b_Channel_Perf = PRY_reg_Channel_Perf.coef_
PRY_b0_Channel_Perf= PRY_reg_Channel_Perf.intercept_

    
# #------ (19) - PST -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(PST)
scaled_df = pd.DataFrame(d)

PST_T = scaled_df.T
PST_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
PST_X_Risk = PST_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PST_y_Risk = PST_T[['Credit_Raiting']]
PST_reg_Risk = linear_model.LinearRegression()
PST_reg_Risk.fit(PST_X_Risk,PST_y_Risk)
PST_b_Risk = PST_reg_Risk.coef_
PST_b0_Risk= PST_reg_Risk.intercept_

# Performance Regression
PST_X_Perf = PST_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PST_y_Perf = PST_T[['ROA']]
PST_reg_Perf = linear_model.LinearRegression()
PST_reg_Perf.fit(PST_X_Perf,PST_y_Perf)
PST_b_Perf = PST_reg_Perf.coef_
PST_b0_Perf= PST_reg_Perf.intercept_

# Risk Channel Regression:
PST_X_Channel_Risk = PST_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PST_y_Channel_Risk = PST_T[['Credit_Raiting']]
PST_reg_Channel_Risk = linear_model.LinearRegression()
PST_reg_Channel_Risk.fit(PST_X_Channel_Risk,PST_y_Channel_Risk)
PST_b_Channel_Risk = PST_reg_Channel_Risk.coef_
PST_b0_Channel_Risk= PST_reg_Channel_Risk.intercept_

# Performance Channel Regression
PST_X_Channel_Perf = PST_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
PST_y_Channel_Perf = PST_T[['ROA']]
PST_reg_Channel_Perf = linear_model.LinearRegression()
PST_reg_Channel_Perf.fit(PST_X_Channel_Perf,PST_y_Channel_Perf)
PST_b_Channel_Perf = PST_reg_Channel_Perf.coef_
PST_b0_Channel_Perf= PST_reg_Channel_Perf.intercept_

    
# #------ (20) - RACE -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(RACE)
scaled_df = pd.DataFrame(d)

RACE_T = scaled_df.T
RACE_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
RACE_X_Risk = RACE_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
RACE_y_Risk = RACE_T[['Credit_Raiting']]
RACE_reg_Risk = linear_model.LinearRegression()
RACE_reg_Risk.fit(RACE_X_Risk,RACE_y_Risk)
RACE_b_Risk = RACE_reg_Risk.coef_
RACE_b0_Risk= RACE_reg_Risk.intercept_

# Performance Regression
RACE_X_Perf = RACE_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
RACE_y_Perf = RACE_T[['ROA']]
RACE_reg_Perf = linear_model.LinearRegression()
RACE_reg_Perf.fit(RACE_X_Perf,RACE_y_Perf)
RACE_b_Perf = RACE_reg_Perf.coef_
RACE_b0_Perf= RACE_reg_Perf.intercept_

# Risk Channel Regression:
RACE_X_Channel_Risk = RACE_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
RACE_y_Channel_Risk = RACE_T[['Credit_Raiting']]
RACE_reg_Channel_Risk = linear_model.LinearRegression()
RACE_reg_Channel_Risk.fit(RACE_X_Channel_Risk,RACE_y_Channel_Risk)
RACE_b_Channel_Risk = RACE_reg_Channel_Risk.coef_
RACE_b0_Channel_Risk= RACE_reg_Channel_Risk.intercept_

# Performance Channel Regression
RACE_X_Channel_Perf = RACE_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
RACE_y_Channel_Perf = RACE_T[['ROA']]
RACE_reg_Channel_Perf = linear_model.LinearRegression()
RACE_reg_Channel_Perf.fit(RACE_X_Channel_Perf,RACE_y_Channel_Perf)
RACE_b_Channel_Perf = RACE_reg_Channel_Perf.coef_
RACE_b0_Channel_Perf= RACE_reg_Channel_Perf.intercept_

    
# #------ (21) - REC -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(REC)
scaled_df = pd.DataFrame(d)

REC_T = scaled_df.T
REC_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
REC_X_Risk = REC_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
REC_y_Risk = REC_T[['Credit_Raiting']]
REC_reg_Risk = linear_model.LinearRegression()
REC_reg_Risk.fit(REC_X_Risk,REC_y_Risk)
REC_b_Risk = REC_reg_Risk.coef_
REC_b0_Risk= REC_reg_Risk.intercept_

# Performance Regression
REC_X_Perf = REC_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
REC_y_Perf = REC_T[['ROA']]
REC_reg_Perf = linear_model.LinearRegression()
REC_reg_Perf.fit(REC_X_Perf,REC_y_Perf)
REC_b_Perf = REC_reg_Perf.coef_
REC_b0_Perf= REC_reg_Perf.intercept_

# Risk Channel Regression:
REC_X_Channel_Risk = REC_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
REC_y_Channel_Risk = REC_T[['Credit_Raiting']]
REC_reg_Channel_Risk = linear_model.LinearRegression()
REC_reg_Channel_Risk.fit(REC_X_Channel_Risk,REC_y_Channel_Risk)
REC_b_Channel_Risk = REC_reg_Channel_Risk.coef_
REC_b0_Channel_Risk= REC_reg_Channel_Risk.intercept_

# Performance Channel Regression
REC_X_Channel_Perf = REC_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
REC_y_Channel_Perf = REC_T[['ROA']]
REC_reg_Channel_Perf = linear_model.LinearRegression()
REC_reg_Channel_Perf.fit(REC_X_Channel_Perf,REC_y_Channel_Perf)
REC_b_Channel_Perf = REC_reg_Channel_Perf.coef_
REC_b0_Channel_Perf= REC_reg_Channel_Perf.intercept_
    
# #------ (22) - SPM -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(SPM)
scaled_df = pd.DataFrame(d)

SPM_T = scaled_df.T
SPM_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
SPM_X_Risk = SPM_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
SPM_y_Risk = SPM_T[['Credit_Raiting']]
SPM_reg_Risk = linear_model.LinearRegression()
SPM_reg_Risk.fit(SPM_X_Risk,SPM_y_Risk)
SPM_b_Risk = SPM_reg_Risk.coef_
SPM_b0_Risk= SPM_reg_Risk.intercept_

# Performance Regression
SPM_X_Perf = SPM_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
SPM_y_Perf = SPM_T[['ROA']]
SPM_reg_Perf = linear_model.LinearRegression()
SPM_reg_Perf.fit(SPM_X_Perf,SPM_y_Perf)
SPM_b_Perf = SPM_reg_Perf.coef_
SPM_b0_Perf= SPM_reg_Perf.intercept_

# Risk Channel Regression:
SPM_X_Channel_Risk = SPM_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
SPM_y_Channel_Risk = SPM_T[['Credit_Raiting']]
SPM_reg_Channel_Risk = linear_model.LinearRegression()
SPM_reg_Channel_Risk.fit(SPM_X_Channel_Risk,SPM_y_Channel_Risk)
SPM_b_Channel_Risk = SPM_reg_Channel_Risk.coef_
SPM_b0_Channel_Risk= SPM_reg_Channel_Risk.intercept_

# Performance Channel Regression
SPM_X_Channel_Perf = SPM_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
SPM_y_Channel_Perf = SPM_T[['ROA']]
SPM_reg_Channel_Perf = linear_model.LinearRegression()
SPM_reg_Channel_Perf.fit(SPM_X_Channel_Perf,SPM_y_Channel_Perf)
SPM_b_Channel_Perf = SPM_reg_Channel_Perf.coef_
SPM_b0_Channel_Perf= SPM_reg_Channel_Perf.intercept_

# #------ (23) - SRG -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(SRG)
scaled_df = pd.DataFrame(d)

SRG_T = scaled_df.T
SRG_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
SRG_X_Risk = SRG_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
SRG_y_Risk = SRG_T[['Credit_Raiting']]
SRG_reg_Risk = linear_model.LinearRegression()
SRG_reg_Risk.fit(SRG_X_Risk,SRG_y_Risk)
SRG_b_Risk = SRG_reg_Risk.coef_
SRG_b0_Risk= SRG_reg_Risk.intercept_

# Performance Regression
SRG_X_Perf = SRG_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
SRG_y_Perf = SRG_T[['ROA']]
SRG_reg_Perf = linear_model.LinearRegression()
SRG_reg_Perf.fit(SRG_X_Perf,SRG_y_Perf)
SRG_b_Perf = SRG_reg_Perf.coef_
SRG_b0_Perf= SRG_reg_Perf.intercept_

# Risk Channel Regression:
SRG_X_Channel_Risk = SRG_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
SRG_y_Channel_Risk = SRG_T[['Credit_Raiting']]
SRG_reg_Channel_Risk = linear_model.LinearRegression()
SRG_reg_Channel_Risk.fit(SRG_X_Channel_Risk,SRG_y_Channel_Risk)
SRG_b_Channel_Risk = SRG_reg_Channel_Risk.coef_
SRG_b0_Channel_Risk= SRG_reg_Channel_Risk.intercept_

# Performance Channel Regression
SRG_X_Channel_Perf = SRG_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
SRG_y_Channel_Perf = SRG_T[['ROA']]
SRG_reg_Channel_Perf = linear_model.LinearRegression()
SRG_reg_Channel_Perf.fit(SRG_X_Channel_Perf,SRG_y_Channel_Perf)
SRG_b_Channel_Perf = SRG_reg_Channel_Perf.coef_
SRG_b0_Channel_Perf= SRG_reg_Channel_Perf.intercept_


# #------ (24) - STLA -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(STLA)
scaled_df = pd.DataFrame(d)

STLA_T = scaled_df.T
STLA_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
STLA_X_Risk = STLA_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
STLA_y_Risk = STLA_T[['Credit_Raiting']]
STLA_reg_Risk = linear_model.LinearRegression()
STLA_reg_Risk.fit(STLA_X_Risk,STLA_y_Risk)
STLA_b_Risk = STLA_reg_Risk.coef_
STLA_b0_Risk= STLA_reg_Risk.intercept_

# Performance Regression
STLA_X_Perf = STLA_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
STLA_y_Perf = STLA_T[['ROA']]
STLA_reg_Perf = linear_model.LinearRegression()
STLA_reg_Perf.fit(STLA_X_Perf,STLA_y_Perf)
STLA_b_Perf = STLA_reg_Perf.coef_
STLA_b0_Perf= STLA_reg_Perf.intercept_

# Risk Channel Regression:
STLA_X_Channel_Risk = STLA_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
STLA_y_Channel_Risk = STLA_T[['Credit_Raiting']]
STLA_reg_Channel_Risk = linear_model.LinearRegression()
STLA_reg_Channel_Risk.fit(STLA_X_Channel_Risk,STLA_y_Channel_Risk)
STLA_b_Channel_Risk = STLA_reg_Channel_Risk.coef_
STLA_b0_Channel_Risk= STLA_reg_Channel_Risk.intercept_

# Performance Channel Regression
STLA_X_Channel_Perf = STLA_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
STLA_y_Channel_Perf = STLA_T[['ROA']]
STLA_reg_Channel_Perf = linear_model.LinearRegression()
STLA_reg_Channel_Perf.fit(STLA_X_Channel_Perf,STLA_y_Channel_Perf)
STLA_b_Channel_Perf = STLA_reg_Channel_Perf.coef_
STLA_b0_Channel_Perf= STLA_reg_Channel_Perf.intercept_

# #------ (25) - STM -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(STM)
scaled_df = pd.DataFrame(d)

STM_T = scaled_df.T
STM_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
STM_X_Risk = STM_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
STM_y_Risk = STM_T[['Credit_Raiting']]
STM_reg_Risk = linear_model.LinearRegression()
STM_reg_Risk.fit(STM_X_Risk,STM_y_Risk)
STM_b_Risk = STM_reg_Risk.coef_
STM_b0_Risk= STM_reg_Risk.intercept_

# Performance Regression
STM_X_Perf = STM_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
STM_y_Perf = STM_T[['ROA']]
STM_reg_Perf = linear_model.LinearRegression()
STM_reg_Perf.fit(STM_X_Perf,STM_y_Perf)
STM_b_Perf = STM_reg_Perf.coef_
STM_b0_Perf= STM_reg_Perf.intercept_

# Risk Channel Regression:
STM_X_Channel_Risk = STM_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
STM_y_Channel_Risk = STM_T[['Credit_Raiting']]
STM_reg_Channel_Risk = linear_model.LinearRegression()
STM_reg_Channel_Risk.fit(STM_X_Channel_Risk,STM_y_Channel_Risk)
STM_b_Channel_Risk = STM_reg_Channel_Risk.coef_
STM_b0_Channel_Risk= STM_reg_Channel_Risk.intercept_

# Performance Channel Regression
STM_X_Channel_Perf = STM_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
STM_y_Channel_Perf = STM_T[['ROA']]
STM_reg_Channel_Perf = linear_model.LinearRegression()
STM_reg_Channel_Perf.fit(STM_X_Channel_Perf,STM_y_Channel_Perf)
STM_b_Channel_Perf = STM_reg_Channel_Perf.coef_
STM_b0_Channel_Perf= STM_reg_Channel_Perf.intercept_

# #------ (26) - TEN -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(TEN)
scaled_df = pd.DataFrame(d)

TEN_T = scaled_df.T
TEN_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
TEN_X_Risk = TEN_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TEN_y_Risk = TEN_T[['Credit_Raiting']]
TEN_reg_Risk = linear_model.LinearRegression()
TEN_reg_Risk.fit(TEN_X_Risk,TEN_y_Risk)
TEN_b_Risk = TEN_reg_Risk.coef_
TEN_b0_Risk= TEN_reg_Risk.intercept_

# Performance Regression
TEN_X_Perf = TEN_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TEN_y_Perf = TEN_T[['ROA']]
TEN_reg_Perf = linear_model.LinearRegression()
TEN_reg_Perf.fit(TEN_X_Perf,TEN_y_Perf)
TEN_b_Perf = TEN_reg_Perf.coef_
TEN_b0_Perf= TEN_reg_Perf.intercept_

# Risk Channel Regression:
TEN_X_Channel_Risk = TEN_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TEN_y_Channel_Risk = TEN_T[['Credit_Raiting']]
TEN_reg_Channel_Risk = linear_model.LinearRegression()
TEN_reg_Channel_Risk.fit(TEN_X_Channel_Risk,TEN_y_Channel_Risk)
TEN_b_Channel_Risk = TEN_reg_Channel_Risk.coef_
TEN_b0_Channel_Risk= TEN_reg_Channel_Risk.intercept_

# Performance Channel Regression
TEN_X_Channel_Perf = TEN_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TEN_y_Channel_Perf = TEN_T[['ROA']]
TEN_reg_Channel_Perf = linear_model.LinearRegression()
TEN_reg_Channel_Perf.fit(TEN_X_Channel_Perf,TEN_y_Channel_Perf)
TEN_b_Channel_Perf = TEN_reg_Channel_Perf.coef_
TEN_b0_Channel_Perf= TEN_reg_Channel_Perf.intercept_

# #------ (27) - TIT -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(TIT)
scaled_df = pd.DataFrame(d)

TIT_T = scaled_df.T
TIT_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
TIT_X_Risk = TIT_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TIT_y_Risk = TIT_T[['Credit_Raiting']]
TIT_reg_Risk = linear_model.LinearRegression()
TIT_reg_Risk.fit(TIT_X_Risk,TIT_y_Risk)
TIT_b_Risk = TIT_reg_Risk.coef_
TIT_b0_Risk= TIT_reg_Risk.intercept_

# Performance Regression
TIT_X_Perf = TIT_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TIT_y_Perf = TIT_T[['ROA']]
TIT_reg_Perf = linear_model.LinearRegression()
TIT_reg_Perf.fit(TIT_X_Perf,TIT_y_Perf)
TIT_b_Perf = TIT_reg_Perf.coef_
TIT_b0_Perf= TIT_reg_Perf.intercept_

# Risk Channel Regression:
TIT_X_Channel_Risk = TIT_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TIT_y_Channel_Risk = TIT_T[['Credit_Raiting']]
TIT_reg_Channel_Risk = linear_model.LinearRegression()
TIT_reg_Channel_Risk.fit(TIT_X_Channel_Risk,TIT_y_Channel_Risk)
TIT_b_Channel_Risk = TIT_reg_Channel_Risk.coef_
TIT_b0_Channel_Risk= TIT_reg_Channel_Risk.intercept_

# Performance Channel Regression
TIT_X_Channel_Perf = TIT_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TIT_y_Channel_Perf = TIT_T[['ROA']]
TIT_reg_Channel_Perf = linear_model.LinearRegression()
TIT_reg_Channel_Perf.fit(TIT_X_Channel_Perf,TIT_y_Channel_Perf)
TIT_b_Channel_Perf = TIT_reg_Channel_Perf.coef_
TIT_b0_Channel_Perf= TIT_reg_Channel_Perf.intercept_

# #------ (28) - TRN -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from sklearn import preprocessing
d = preprocessing.normalize(TRN)
scaled_df = pd.DataFrame(d)

TRN_T = scaled_df.T
TRN_T.columns = ['Credit_Raiting','ROA','CSR_Score','ESG_Score','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']

# Risk Regression:
TRN_X_Risk = TRN_T[['ROA','ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TRN_y_Risk = TRN_T[['Credit_Raiting']]
TRN_reg_Risk = linear_model.LinearRegression()
TRN_reg_Risk.fit(TRN_X_Risk,TRN_y_Risk)
TRN_b_Risk = TRN_reg_Risk.coef_
TRN_b0_Risk= TRN_reg_Risk.intercept_

# Performance Regression
TRN_X_Perf = TRN_T[['ESG_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TRN_y_Perf = TRN_T[['ROA']]
TRN_reg_Perf = linear_model.LinearRegression()
TRN_reg_Perf.fit(TRN_X_Perf,TRN_y_Perf)
TRN_b_Perf = TRN_reg_Perf.coef_
TRN_b0_Perf= TRN_reg_Perf.intercept_

# Risk Channel Regression:
TRN_X_Channel_Risk = TRN_T[['ROA','E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TRN_y_Channel_Risk = TRN_T[['Credit_Raiting']]
TRN_reg_Channel_Risk = linear_model.LinearRegression()
TRN_reg_Channel_Risk.fit(TRN_X_Channel_Risk,TRN_y_Channel_Risk)
TRN_b_Channel_Risk = TRN_reg_Channel_Risk.coef_
TRN_b0_Channel_Risk= TRN_reg_Channel_Risk.intercept_

# Performance Channel Regression
TRN_X_Channel_Perf = TRN_T[['E_Score','S_Score','G_Score','Asset_E_Ratio','Debt_E_Ratio','Quick_Ratio','Tot_Revenue','Tot_Asset','Tot_Equity']]
TRN_y_Channel_Perf = TRN_T[['ROA']]
TRN_reg_Channel_Perf = linear_model.LinearRegression()
TRN_reg_Channel_Perf.fit(TRN_X_Channel_Perf,TRN_y_Channel_Perf)
TRN_b_Channel_Perf = TRN_reg_Channel_Perf.coef_
TRN_b0_Channel_Perf= TRN_reg_Channel_Perf.intercept_





