import pandas as pd

df = pd.read_csv('Indian_Kids_Screen_Time.csv')

# print(df.head(10))
# cleaning column names structuring them
df.columns = [col.strip().lower() for col in df.columns]
# print(df.columns)

# Checking nulls
# print(df.isnull().sum().sort_values(ascending=False))
# health_impacts                       3218

# dealing with null values
df['health_impacts'] = df['health_impacts'].fillna("Not Reported")


# rechecking the null's
# print(df.isnull().sum()) all set
# print(df.head(10))

df['gender'] = df['gender'].str.capitalize().str.strip()
df['primary_device'] = df['primary_device'].str.title().str.strip()
df['urban_or_rural'] = df['urban_or_rural'].str.title().str.strip()

df = df[(df['age'] >= 5) & (df['age'] <= 18)]
df = df[(df['avg_daily_screen_time_hr'] >= 0) & (df['avg_daily_screen_time_hr'] <= 24)]

df['exceeded_recommended_limit'].unique()

df['health_impacts'] = df['health_impacts'].fillna("Not Reported")
df['poor_sleep'] = df['health_impacts'].str.contains('Poor Sleep', case=False, na=False)
df['eye_strain'] = df['health_impacts'].str.contains('Eye Strain', case=False, na=False)
df['anxiety'] = df['health_impacts'].str.contains('Anxiety', case=False, na=False)
df['obesity_risk'] = df['health_impacts'].str.contains('Obesity Risk',case=False,na=False)

def screen_time_level(hr):
    if hr <= 1:
        return 'Low'
    elif hr <= 3:
        return 'Moderate'
    else:
        return 'High'

df['screen_time_level'] = df['avg_daily_screen_time_hr'].apply(screen_time_level)

df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['avg_daily_screen_time_hr'] = pd.to_numeric(df['avg_daily_screen_time_hr'], errors='coerce')

print(df.head(10))

def age_group(age):
    if age <= 10:
        return "5-10"
    elif age <= 14:
        return "11-14"
    else:
        return "15-18"

df['age_group'] = df['age'].apply(age_group)

df.to_csv("cleaned_dataset.csv",index=False)

