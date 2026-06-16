# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# We have a to take only those schools with the best maths results (> 80% of 800). First step of the line we take filter by the 'average_math'. 
# Then we take only "school_name" and "average_math" columns sorted by the math average score.
best_math_schools = schools[schools['average_math'] >= 640][['average_math','school_name']].sort_values('average_math', ascending=False)

print(best_math_schools)

# In this case, we create the column 'total_SAT' being the sum of the average of maths, reading and writing.
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
# Now we can sort it by the SAT scores.
schools_sat = schools.sort_values('total_SAT' , ascending = False)
# Now we take only the school name and the SAT score columns
schools_sat_names = schools_sat[['total_SAT','school_name']]
# We create top_10_school
top_10_schools = schools_sat_names[:10]
print(top_10_schools)
