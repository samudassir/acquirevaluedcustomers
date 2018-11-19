# Acquire Valued Customers

### Abstract
<p>
Businesses often face a challenge of retaining customers and converting them to be regular purchaser. As a Businesses strategy, companies and stores run discounted sales programs to attract more customers to be repeat purchasers and improve overall sales of the company.
  We use completely anonymized transactional data of customers along with offer details and History of offers given to customers.
  We will use the data to build a machine learning model and predict customers who will be repeat purchase of items when discounts are offered based on different features.
</p>

### Introduction
<p>
Background
Technology has created a huge shift in the way customers can buy products, to adapt to this change consumer brands are also changing their business models to acquire customers.
Consumer brands often offer discounts to attract new shoppers to buy their products. The most valuable customers are those who return after this initial incented purchase.  With enough purchase history, it is possible to predict which shoppers, when presented an offer, will buy a new item.
LAER is a sales term used in any business
</p>

![alt text](plot/LAER.png)
-	**Land**: “All sales and marketing activities required to land the first sale of a solution to a new customer.” When you land the customer, you've successfully convinced the prospect to become a new customer of yours.
-	**Adopt**: “All activities involved in making sure the customer is successfully adopting and expanding their use of the solution.” This is the step where you help the customer that just bought your product.
-	**Expand**: “All activities required to cost-effectively help current customers expand their spending as usage increases, including both cross-selling and upselling.” As you become more invested in the customer’s outcomes, it becomes easier to tie your technology to other projects and initiatives, encouraging your customers to buy more products and services from you the supplier.
- **Renew**: “All activities required to ensure the customer renews their contract(s).” Convincing your customer to renew their relationship with you when it comes time to repurchase.

<p>
All the above aspects of sale are very important, but Renew is extremely critical for businesses to operate in long run.</p>
<p>Related to this is our project where store provides its customers with a discount offer and we will be predicting the possibility of customer returning to the store and buying the same item.</p>
<p>This will be a classification problem where a customer will repeat the purchase or will not be repeating the purchase.</p>
<p>We will be doing feature extraction and applying different machine learning models to derive AUC Score.
</p>

### About Data
The data set is obtained from Kaggle competition, which is publicly available in [kaggle](https://www.kaggle.com/c/acquire-valued-shoppers-challenge/data)<br>
Dataset has four relational files:<br>
- **transactions.csv** - contains transaction history for all customers for a period of at least 1 year prior to their offered incentive
- **trainHistory.csv** - contains the incentive offered to each customer and information about the behavioral response to the offer
- **testHistory.csv** - contains the incentive offered to each customer but does not include their response (predicting the repeater column for each id in this file)
- **offers.csv** - contains information about the offers
<p>
Transaction data has almost 350 million rows of completely anonymized data from over 300,000 shoppers along with offer information and History of offers given to customers.<br>
The size of the dataset if 3GB.<br>
Due to size constraints, we will choose 16000 customers out of 160K who were given a discount voucher/offer.<br>
</p>
