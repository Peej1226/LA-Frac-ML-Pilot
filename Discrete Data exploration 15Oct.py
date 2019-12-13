#!/usr/bin/env python
# coding: utf-8

# # Introduction
#
# This is mostly just uploading and sorting lists stored in .xlsx files
# from Knowledge Net


import pandas as pd
import pandas_profiling
# import openpyxl
# import matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# pulling in only discrete tab, create a series of panda excel file objects


# In[data 01]:
xlsx01 = pd.ExcelFile(
        "http://usbdbanapp1001.corp.inbaxalta.com:18080/discoverant-kn/Results/maherp/FML%20AG%2001_D/FML%20AG%2001_D.xlsx")

discrete_01 = pd.read_excel(
        xlsx01, sheet_name='Discrete', skiprows=1, header=0, index_col=0)

# col_titles = []
# for col in discrete_01.columns:
#     col_titles.append(col)
# col_titles

discrete_01.head(3)
discrete_01.describe()

profile = discrete_01.profile_report(style={'full_width': True})
profile.to_file(
        output_file="C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/Discrete1.html",
        silent=False)
# In[data 04]:

xlsx04 = pd.ExcelFile(
        "http://usbdbanapp1001.corp.inbaxalta.com:18080/discoverant-kn/Results/maherp/FML%20AG%2004_D/FML%20AG%2004_D.xlsx")

discrete_04 = pd.read_excel(
        xlsx04, sheet_name='Discrete', skiprows=1, header=0, index_col=0)

discrete_04.head(3)
discrete_04.describe()

profile = discrete_04.profile_report(style={'full_width': True})
profile.to_file(
        output_file="C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/Discrete4.html",
        silent=False)

# In[data 05]:

xlsx05 = pd.ExcelFile(
        "http://usbdbanapp1001.corp.inbaxalta.com:18080/discoverant-kn/Results/maherp/FML%20AG%2005_D/FML%20AG%2005_D.xlsx")

discrete_05 = pd.read_excel(
        xlsx05, sheet_name='Discrete', skiprows=1, header=0, index_col=0)

discrete_05.head(3)
discrete_05.describe()

profile = discrete_05.profile_report(style={'full_width': True})
profile.to_file(
        output_file="C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/Discrete5.html",
        silent=False)

# In[data 06]:

xlsx06 = pd.ExcelFile(
        "http://usbdbanapp1001.corp.inbaxalta.com:18080/discoverant-kn/Results/maherp/FML%20AG%2006_D/FML%20AG%2006_D.xlsx")

discrete_06 = pd.read_excel(
        xlsx06, sheet_name='Discrete', skiprows=1, header=0, index_col=0)

discrete_06.head(3)
discrete_06.describe()

profile = discrete_06.profile_report(style={'full_width': True})
profile.to_file(
        output_file="C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/Discrete6.html",
        silent=False)

# In[data 07]:

xlsx07 = pd.ExcelFile(
        "http://usbdbanapp1001.corp.inbaxalta.com:18080/discoverant-kn/Results/maherp/FML%20AG%2007_D/FML%20AG%2007_D.xlsx")

discrete_07 = pd.read_excel(
        xlsx07, sheet_name='Discrete', skiprows=1, header=0, index_col=0)

discrete_07.head(3)
discrete_07.describe()

profile = discrete_07.profile_report(style={'full_width': True})
profile.to_file(
        output_file="C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/Discrete7.html",
        silent=False)

# In[data 08]:

xlsx08 = pd.ExcelFile(
        "http://usbdbanapp1001.corp.inbaxalta.com:18080/discoverant-kn/Results/maherp/FML%20AG%2008_D/FML%20AG%2008_D.xlsx")

discrete_08 = pd.read_excel(
        xlsx08, sheet_name='Discrete', skiprows=1, header=0, index_col=0)

discrete_08.head(3)
discrete_08.describe()

profile = discrete_08.profile_report(style={'full_width': True})
profile.to_file(
        output_file="C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/Discrete8.html",
        silent=False)

# In[data REF]:

xlsxRf = pd.ExcelFile(
        "http://usbdbanapp1001.corp.inbaxalta.com:18080/discoverant-kn/Results/maherp/FML%20AG%20Reference/FML%20AG%20Reference.xlsx")

discrete_Rf = pd.read_excel(
        xlsxRf, sheet_name='Discrete', skiprows=1, header=0, index_col=0)

discrete_Rf.head(3)

discrete_Rf.describe()

profile = discrete_Rf.profile_report(style={'full_width': True})
profile.to_file(
        output_file="C:/Users/maherp/Documents/GitHub/LA-Frac-ML-Pilot/EDA Reports/DiscreteRf.html",
        silent=False)
