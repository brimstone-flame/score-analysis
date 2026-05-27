import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores.csv')
df['total_score'] = df['chinese'] + df['math'] + df['english']

print("===== original data =====")
print(df)
print("\n")


print("===== Statistics of all subject scores =====")
subjects = ['chinese', 'math', 'english', 'total_score']
des = df[subjects].describe()
print(round(des.loc[["mean", "max", "min"]], 2 ))
print("\n")

print("===== The average scores of all subjects in each class =====")
class_avg = df.groupby('class')[subjects].mean().round(2)
print(class_avg)
print("\n")

print("===== The number of people who failed in each subject =====")
fail_chinese = df[df['chinese'] < 60].shape[0]
fail_math = df[df['math'] < 60].shape[0]
fail_english = df[df['english'] < 60].shape[0]
print(f"pepple failed in chinese:{fail_chinese}")
print(f"pepple failed in math:{fail_math}")
print(f"pepple failed in english:{fail_english}")
print("\n")

print("===== Rank by total score =====")
rank_df = df.sort_values('total_score', ascending=False)[['name', 'class', 'total_score']]
print(rank_df.reset_index(drop=True))

class_avg['total_score'].plot(kind="bar", title="The average total score of each class")
plt.ylabel("Average score")
plt.show()

gender_avg = df.groupby('gender')[subjects].mean().round(2)
gender_avg[['chinese', 'math', 'english', 'total_score']].plot(kind="bar", title="Male and female comparison")
plt.ylabel("Average score")
plt.show()