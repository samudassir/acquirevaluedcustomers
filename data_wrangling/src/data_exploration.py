#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:38:34 2018

@author: syedm
"""
from collections import Counter
from matplotlib.pyplot import *
import numpy as np

hist = pd.read_csv("trainHistory10000.csv")

offers = pd.read_csv("offers.csv")

trans = pd.read_csv("transactions10000.csv")


hist_offer = hist.merge(offers,left_on='offer',right_on='offer')
replace_repeater = {"repeater":     {"t": 1, "f": 0}}
hist_offer.replace(replace_repeater,inplace=True)
hist_offer.head()

c = Counter()

c.update(hist_offer['repeater'])
print(c)

lab = []
valu = []
for label, val in c.items():
    lab.append(label)
    valu.append(val)

indexes = np.arange(len(lab))
width = 0.5

plt.bar(indexes, valu, width)
plt.xticks(lab)
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('returning_customers.png', bbox_inches='tight')
plt.show()

hist_offer['m']=1
trans['m']=1
hist_offer.groupby(["category"])["m"].count().plot(kind='barh',legend=True)
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('popular_category.png', bbox_inches='tight')
plt.show()

hist_offer.groupby(["offer"])["m"].count().plot(kind='barh',legend=True)
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('popular_offer.png', bbox_inches='tight')
plt.show()

hist_offer.groupby(["offer","category"])["m"].count().plot(kind='barh',legend=True)
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('popular_offer_category.png', bbox_inches='tight')
plt.show()


trans_plt = trans.groupby(["category"])["m"].count().reset_index()
t_plt = trans_plt.nlargest(50,'m')
t_plt.groupby(["category"])["m"].sum().plot(kind='barh',legend=True)
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('popular_trans_category.png', bbox_inches='tight')
plt.show()

trans_high_amt = trans.groupby(["category"])["purchaseamount"].sum().reset_index()
trans_high_amt_plt = trans_high_amt.nlargest(50,'purchaseamount')
trans_high_amt_plt_1 = trans_high_amt.nsmallest(50,'purchaseamount')

trans_high_amt_plt.groupby(["category"])["purchaseamount"].sum().plot(kind='barh',legend=True)
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('unpopular_trans_category_purchase_amount.png', bbox_inches='tight')
plt.show()

trans_high_amt_plt_1.groupby(["category"])["purchaseamount"].sum().plot(kind='barh',legend=True)
_ = plt.rcParams['figure.figsize'] = [20, 15]
savefig('unpopular_trans_category_purchase_amount.png', bbox_inches='tight')
plt.show()