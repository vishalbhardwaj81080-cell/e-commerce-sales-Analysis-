#!/usr/bin/env python
# coding: utf-8

# # E-Commerece Sale EDA

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[4]:


df = pd.read_csv(r"C:\Users\HP\Downloads\ecommerce_sales_messy.csv")
df.head(10)


# In[5]:


df.shape


#    # Data Cleaning and Processing

# In[7]:


df.isnull().sum()


# In[ ]:


df["product_category"].fillna(df["product_category"].mode()[0],inplace=True)
df["payment_method"].fillna(df["payment_method"].mode()[0],inplace=True)
df["quantity"].fillna(df["quantity"].median(),inplace=True)
df["discount"].fillna(df["discount"].mode()[0],inplace=True)
df["order_status"].fillna("unknown",inplace=True)
df["rating"].fillna(df["rating"].median(),inplace=True)


# In[9]:


df.isnull().sum()


# In[10]:


df.head(20)


# In[11]:


df.tail(20)


# In[12]:


df.info()


# In[14]:


df["order_date"]=pd.to_datetime(df["order_date"])
df["quantity"] = df["quantity"].astype(int)
df["discount"] = df["discount"].astype(int)
df["rating"] = df["rating"].astype(int)


# In[15]:


df.info()


# In[18]:


df.duplicated().sum()


# In[19]:


df.describe()


#   # Oder By Product Category

# In[20]:


plt.figure(figsize=(5,4))
df["product_category"].value_counts().plot(kind="bar")
plt.xlabel("product_category")
plt.ylabel("number of order")
plt.title("Number by Product Category")
plt.show()


# In[21]:


df["product_category"].value_counts()


#   # Payment Method Distribution

# In[22]:


plt.figure(figsize=(5,4))
df["payment_method"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.title("Payment Mathod Distribution")
plt.ylabel("")
plt.show()


#   # Order Status Analysis

# In[23]:


plt.figure(figsize=(5,4))
df["order_status"].value_counts().plot(kind="bar")
plt.xlabel("Order_status")
plt.ylabel("Count")
plt.title("Order Status Distribution")
plt.show()


# In[24]:


df["order_status"].value_counts()


#   # Customer Rating Distribution

# In[25]:


plt.figure(figsize=(5,4))
df["rating"].plot(kind="hist",bins=10)
plt.xlabel("Rating")
plt.ylabel("frequency")
plt.title("Customer Rating Distribution")
plt.show()


# In[26]:


df["rating"].value_counts()


#   # Price VS Average Quantity

# In[27]:


plt.figure(figsize=(5,4))
plt.scatter(df["price"],df["quantity"])
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.title("Price vs Quantity")
plt.show()


# In[28]:


df[["price","quantity"]].value_counts().head(20)


#   # Discount VS Average Quantity

# In[41]:


plt.figure(figsize=(5,4))
df.groupby("discount")["quantity"].mean().plot(kind="line",marker=".")
plt.xlabel("Discount")
plt.ylabel("Average")
plt.title("Discount vs Average Quantity")
plt.show()


#   # Multiple Charts In ONE Figure (subplots)

# In[52]:


# 👇 MAIN FIX
fig, axes = plt.subplots(3, 2, figsize=(18, 14))
fig.suptitle("E-Commerce Sales EDA Dashboard", fontsize=18)

# Order by Product Category
df['product_category'].value_counts().plot(
    kind='bar', ax=axes[0, 0]
)
axes[0, 0].set_title("Orders by Product Category")
axes[0, 0].set_xlabel("Category")
axes[0, 0].set_ylabel("Orders")

# Payment Method
df['payment_method'].value_counts().plot(
    kind='pie', autopct='%1.1f%%', ax=axes[0, 1]
)
axes[0, 1].set_title("Payment Method Distribution")
axes[0, 1].set_ylabel("")

# Order Status
df['order_status'].value_counts().plot(
    kind='bar', ax=axes[1, 0]
)
axes[1, 0].set_title("Order Status Distribution")
axes[1, 0].set_xlabel("Status")
axes[1, 0].set_ylabel("Count")

# Rating Distribution
axes[1, 1].hist(df['rating'], bins=5)
axes[1, 1].set_title("Customer Rating Distribution")
axes[1, 1].set_xlabel("Rating")
axes[1, 1].set_ylabel("Frequency")

# Price vs Quantity
axes[2, 0].scatter(df['price'], df['quantity'])
axes[2, 0].set_title("Price vs Quantity")
axes[2, 0].set_xlabel("Price")
axes[2, 0].set_ylabel("Quantity")

# Discount vs Avg Quantity
df.groupby('discount')['quantity'].mean().plot(
    kind='line', ax=axes[2, 1]
)
axes[2, 1].set_title("Discount vs Average Quantity")
axes[2, 1].set_xlabel("Discount")
axes[2, 1].set_ylabel("Avg Quantity")

# SPACING FIX
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


# In[ ]:




