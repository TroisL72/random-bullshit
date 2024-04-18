import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("amazon_reviews.csv")

# Dataset Info:
print(df.info())
print(df.describe())

# Overall rating distribution:
plt.hist(df['overall'], bins=5, edgecolor='black')
plt.xlabel('Overall rating')
plt.ylabel('Frequency')
plt.title('Distribution of overall ratings')
plt.show()

# Verified vs unverified reviews:
# verified_counts = df['verified'].value_counts()
# plt.bar(verified_counts.index, verified_counts.values)
# plt.xlabel('Verification status')
# plt.ylabel('Number of reviews')
# plt.title('Verified vs unverified reviews')
# plt.xticks([0, 1], ['Unverified', 'Verified'])
# plt.show()

# Review counts per product:
# product_review_counts = df['product'].value_counts().head(10)
# plt.bar(product_review_counts.index, product_review_counts.values)
# plt.xlabel('Product')
# plt.ylabel('Number of reviews')
# plt.title('Top 10 reviewed products')
# plt.xticks(rotation=45, ha='right')
# plt.show()

# Product gets the most 5 stars:
# five_stars = df[df['overall'] == 5]
# product_counts_5 = five_stars['product'].value_counts().head(10)
# plt.bar(product_counts_5.index, product_counts_5.values)
# plt.xlabel('Product')
# plt.ylabel('Number of 5-Star reviews')
# plt.title('Top 10 products with most 5-stars reviews') 
# plt.xticks(rotation=45, ha='right')
# plt.show()

# Product gets the most 1 star:
# one_star = df[df['overall'] == 1]
# product_counts_1 = one_star['product'].value_counts().head(10)
# plt.bar(product_counts_1.index, product_counts_1.values)
# plt.xlabel('Product')
# plt.ylabel('Number of 5-Star Reviews')
# plt.title('Top 10 products with most 1-star reviews')
# plt.xticks(rotation=45, ha='right')
# plt.show()

# Relationship between overall rating and review length
# df['review_length'] = df['reviewText'].apply(lambda x: len(str(x)))
# plt.scatter(df['overall'], df['review_length'], alpha=0.5)
# plt.xlabel('Overall rating')
# plt.ylabel('Review length')
# plt.title('Relationship between overall rating and review length')
# plt.show()

# Average rating for top 10 products
# average_rating = df.groupby('product')['overall'].mean().sort_values(ascending=False)
# plt.figure(figsize=(10, 10))
# average_rating.head(30).plot(kind='bar')
# plt.xlabel('Product')
# plt.ylabel('Average rating')
# plt.title('Average rating for top 10 products')
# plt.xticks(rotation=90)
# plt.show()







