# %%
import pandas as pd
import io
from ipywidgets import FileUpload
from IPython.display import display

# %%
uploader = FileUpload(
    accept='.csv',
    multiple=False
)

# %%
#Upload the csv file
display(uploader)

# %%
#Make pandas read the csv files counting in tuples
if uploader.value:
    try:
        if isinstance(uploader.value, tuple) and len(uploader.value) > 0:
            first_item = uploader.value[0]
            if isinstance(first_item, dict) and 'content' in first_item:
                content = io.BytesIO(first_item['content'])
                df = pd.read_csv(content)
                print("File uploaded and dataframe created")
                print(df.head())
            elif isinstance(first_item, bytes):
                content = io.BytesIO(first_item)
                df = pd.read_csv(content)
                print("File uploaded and dataframe created")
                print(df.head())
            else:
                print(f"Unexpected structure of uploader.value[0]: {type(first_item)}")
        else:
            print(f"Unexpected structure of uploader.value[0]: {type(uploader.value)}")
            
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
else:
    print("No file uploaded.")

# %%
print(df.isnull().sum()) #Shows missing values in the dataframe

# %%
# Removing all the missing values in the dataframe

cols_to_fill_zero = [
    'PURCHASE_COUNT_DELIVERY', 'PURCHASE_COUNT_TAKEAWAY', 'BREAKFAST_PURCHASES',
    'LUNCH_PURCHASES', 'EVENING_PURCHASES', 'DINNER_PURCHASES',
    'LATE_NIGHT_PURCHASES', 'TOTAL_PURCHASES_EUR', 'DISTINCT_PURCHASE_VENUE_COUNT',
    'MIN_PURCHASE_VALUE_EUR', 'MAX_PURCHASE_VALUE_EUR', 'AVG_PURCHASE_VALUE_EUR',
    'IOS_PURCHASES', 'WEB_PURCHASES', 'ANDROID_PURCHASES', 'AVERAGE_DELIVERY_DISTANCE_KMS'
]
df[cols_to_fill_zero] = df[cols_to_fill_zero].fillna(0)

df['FIRST_PURCHASE_DAY'] = df['FIRST_PURCHASE_DAY'].fillna('Never Purchased')
df['LAST_PURCHASE_DAY'] = df['LAST_PURCHASE_DAY'].fillna('Never Purchased')
df['MOST_COMMON_HOUR_OF_THE_DAY_TO_PURCHASE'] = df['MOST_COMMON_HOUR_OF_THE_DAY_TO_PURCHASE'].fillna('No Purchase')
df['MOST_COMMON_WEEKDAY_TO_PURCHASE'] = df['MOST_COMMON_WEEKDAY_TO_PURCHASE'].fillna('No Purchase')
df['AVG_DAYS_BETWEEN_PURCHASES'] = df['AVG_DAYS_BETWEEN_PURCHASES'].fillna('Not Applicable')
df['MEDIAN_DAYS_BETWEEN_PURCHASES'] = df['MEDIAN_DAYS_BETWEEN_PURCHASES'].fillna('Not Applicable')

df['PREFERRED_RESTAURANT_TYPES'] = df['PREFERRED_RESTAURANT_TYPES'].fillna('Unknown')

# %%
df['PREFERRED_DEVICE'] = df['PREFERRED_DEVICE'].fillna(df['PREFERRED_DEVICE'].mode()[0])

# %%
print(df.isnull().sum()) #Shows that the missing values are now corrected

# %%
print(df.head())

# %%
print(df.describe())

# %%
print(df['PURCHASE_COUNT'].mean())
print(df['TOTAL_PURCHASES_EUR'].median())
print(df['REGISTRATION_COUNTRY'].value_counts())

# %%
subset_df = df[['REGISTRATION_COUNTRY', 'PURCHASE_COUNT', 'TOTAL_PURCHASES_EUR']]
print(subset_df.head())

# %%
import seaborn as sns
import matplotlib.pyplot as plt

# %%
sns.boxplot(x='PREFERRED_DEVICE', y='TOTAL_PURCHASES_EUR', data=df)

plt.title('Purchase Value Distribution by Device')
plt.xlabel('Preferred Device')
plt.ylabel('Total Purchases (EUR)')
plt.show()

# %%
sns.countplot(x='PREFERRED_DEVICE', data=df)

plt.title('Distribution of Preferred Devices')
plt.xlabel('Device')
plt.ylabel('Count')
plt.show()

# %%



