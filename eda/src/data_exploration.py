#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:38:34 2018

@author: syedm
"""
from collections import Counter
from matplotlib.pyplot import *
import numpy as np


# Load data
hist = pd.read_csv("../../data/trans_Hist16000.csv")

offers = pd.read_csv("../../data/offers.csv")

trans = pd.read_csv("../../data/transactions_16000.csv")


# replace string with 0 and 1
hist_offer = hist.merge(offers,left_on='offer',right_on='offer')
replace_repeater = {"repeater":     {"t": 1, "f": 0}}
hist_offer.replace(replace_repeater,inplace=True)
hist_offer.head()

c = Counter()

c.update(hist_offer['repeater'])
#c.update(pd.Series(y_pred))
print(c)

labels = ['Non Repeater', 'Repeater']
sizes = []
for label, val in c.items():
    #lab.append(label)
    valu.append(val)


# Pie plot of Train History

sizes = valu
explode = (0, 0.1)  
colors = ['#66b3ff','#ffcc99']
figure(0)
plt.title("Percent Customer Types")
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=colors)
savefig('../../plot/percent_distribution.png', bbox_inches='tight')
plt.show()

"""
figure(0)
indexes = np.arange(len(lab))
width = 0.5
plt.bar(indexes, valu, width)
#plt.xticks(lab)
plt.xticks(lab,('Non Repeat','Repeat'))
plt.title("Buyer Distribution")
plt.ylabel("Demand")
plt.xlabel("Buyer Types")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/returning_customers.png', bbox_inches='tight')
plt.show()

figure(1)
hist_offer.groupby(["category"])["offervalue"].max().sort_values().plot(kind='barh',color='black', alpha=0.4)#hist_offer.groupby(["category"])["m"].count().sort_values().plot(kind='barh',color='orange')
plt.title("Categories with offered quantity")
plt.ylabel("Category")
plt.xlabel("Max quantity")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/offer_category_quantity.png', bbox_inches='tight')
plt.show()

figure(2)
hist_offer['m']=1
offers['m']=1
trans['m']=1

hist_offer.groupby(["category"])["repeattrips"].sum().sort_values().plot(kind='barh',color='#66b3ff', alpha=0.6)#hist_offer.groupby(["category"])["m"].count().sort_values().plot(kind='barh',color='orange')
plt.title("Categories with returning Customers")
plt.ylabel("Category")
plt.xlabel("# repeat trips")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/offer_category_most_returntrips.png', bbox_inches='tight')
plt.show()
# Bar plot for Categories

figure(3)
hist_offer.groupby(["category"])["m"].count().sort_values().plot(kind='pie', autopct='%1.1f%%', shadow=True, explode = (0, 0,0,0,0,0,0,0,0,0,0,0,0.1))
#hist_offer.groupby(["category"])["m"].count().sort_values().plot(kind='barh',color='orange')
plt.title("Most Offered Categories")
plt.ylabel("Category")
plt.xlabel("# of Offers")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/popular_category.png', bbox_inches='tight')
plt.show()


# Bar plot for Offers
figure(4)
hist_offer.groupby(["offer"])["m"].count().sort_values().plot(kind='barh',color='blue', alpha=0.4)
#hist_offer.groupby(["offer"])["m"].count().sort_values().plot(kind='pie', autopct='%1.1f%%', shadow=True, explode = (0, 0,0,0,0,0,0,0,0,0,0,0,0.1))
plt.title("Popular Offers")
plt.ylabel("Offer")
plt.xlabel("# of Customers Received Offer")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/popular_offer.png', bbox_inches='tight')
plt.show()

# Bar plot for Offers and Categories
figure(5)
hist_offer.groupby(["offer","category"])["m"].count().sort_values().plot(kind='barh',color='cyan', alpha=0.4)
plt.title("Popular Offers and Categories")
plt.ylabel("Offer + Category")
plt.xlabel("# of Customers Received Offer For Category")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/popular_offer_category.png', bbox_inches='tight')
plt.show()

# Most Transacted Categories
figure(6)
trans_plt = trans.groupby(["category"])["m"].count().reset_index()
t_plt = trans_plt.nlargest(50,'m')
t_plt.groupby(["category"])["m"].sum().sort_values().plot(kind='barh',color='grey', alpha=0.4)
plt.title("Most Transacted Categories")
plt.ylabel("Category")
plt.xlabel("# of Transactions")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/popular_trans_category.png', bbox_inches='tight')
plt.show()

# Categories with High Total Purchase Amount
figure(7)
trans_high_amt = trans.groupby(["category"])["purchaseamount"].sum().reset_index()
trans_high_amt_plt = trans_high_amt.nlargest(50,'purchaseamount')
trans_high_amt_plt.groupby(["category"])["purchaseamount"].sum().sort_values().plot(kind='barh',color='green', alpha=0.4)
plt.title("Most spend Categories")
plt.ylabel("Category")
plt.xlabel("Total Purchase Amount")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/popular_trans_category_purchase_amount.png', bbox_inches='tight')
plt.show()

# Categories with Least Total Purchase Amount
figure(8)
trans_high_amt_plt_1 = trans_high_amt.nsmallest(50,'purchaseamount')
trans_high_amt_plt_1.groupby(["category"])["purchaseamount"].sum().sort_values().plot(kind='barh',color='red', alpha=0.4)
plt.title("Least spend Categories")
plt.ylabel("Category")
plt.xlabel("Total Purchase Amount")
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('../../plot/unpopular_trans_category_purchase_amount.png', bbox_inches='tight')
plt.show()

del hist_offer['m']
hist_offer['quantity'] = str(hist_offer['quantity'])
figure(9)
sns.heatmap(hist_offer.drop(['id'],axis=1).corr(), square=True, cmap='RdYlGn')
"""