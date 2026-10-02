import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("cleaned_customer_data.csv")

print("========== DATASET ==========")
print(df)

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATES ==========")
print(df.duplicated().sum())


# ==========================================
# VISUALIZATION 1: AGE DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=6, kde=True)
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.show()


# ==========================================
# VISUALIZATION 2: INCOME DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))
sns.histplot(df["Income"], bins=6, kde=True)
plt.title("Income Distribution of Customers")
plt.xlabel("Income")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("income_distribution.png")
plt.show()


# ==========================================
# VISUALIZATION 3: PURCHASE AMOUNT
# ==========================================

plt.figure(figsize=(8, 5))
sns.histplot(df["PurchaseAmount"], bins=6, kde=True)
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("purchase_distribution.png")
plt.show()


# ==========================================
# VISUALIZATION 4: CUSTOMERS BY CITY
# ==========================================

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="City")
plt.title("Number of Customers by City")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customers_by_city.png")
plt.show()


# ==========================================
# VISUALIZATION 5: PURCHASE BY GENDER
# ==========================================

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Gender", y="PurchaseAmount")
plt.title("Purchase Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Purchase Amount")
plt.tight_layout()
plt.savefig("purchase_by_gender.png")
plt.show()


# ==========================================
# VISUALIZATION 6: INCOME VS PURCHASE
# ==========================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Income",
    y="PurchaseAmount",
    hue="Gender"
)
plt.title("Income vs Purchase Amount")
plt.xlabel("Income")
plt.ylabel("Purchase Amount")
plt.tight_layout()
plt.savefig("income_vs_purchase.png")
plt.show()


# ==========================================
# VISUALIZATION 7: AGE VS PURCHASE
# ==========================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Age",
    y="PurchaseAmount",
    hue="Gender"
)
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.tight_layout()
plt.savefig("age_vs_purchase.png")
plt.show()


print("\n==========================================")
print("EDA VISUALIZATION COMPLETED")
print("Charts saved successfully.")
print("==========================================")
# ==========================================
# EDA VISUALIZATIONS
# ==========================================

# 1. Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=6, kde=True)
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.close()

# 2. Income Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Income"], bins=6, kde=True)
plt.title("Income Distribution of Customers")
plt.xlabel("Income")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("income_distribution.png")
plt.close()

# 3. Purchase Amount Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["PurchaseAmount"], bins=6, kde=True)
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("purchase_distribution.png")
plt.close()

# 4. Customers by City
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="City")
plt.title("Number of Customers by City")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("customers_by_city.png")
plt.close()

# 5. Purchase Amount by Gender
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Gender", y="PurchaseAmount")
plt.title("Purchase Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Purchase Amount")
plt.tight_layout()
plt.savefig("purchase_by_gender.png")
plt.close()

# 6. Income vs Purchase Amount
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Income", y="PurchaseAmount", hue="Gender")
plt.title("Income vs Purchase Amount")
plt.xlabel("Income")
plt.ylabel("Purchase Amount")
plt.tight_layout()
plt.savefig("income_vs_purchase.png")
plt.close()

# 7. Age vs Purchase Amount
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Age", y="PurchaseAmount", hue="Gender")
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.tight_layout()
plt.savefig("age_vs_purchase.png")
plt.close()

print("\n==========================================")
print("EDA VISUALIZATION COMPLETED")
print("Charts saved successfully.")
print("==========================================")