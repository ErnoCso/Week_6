# Task16

# Examine the above code and work out which user-names will be placed in the
# some_users list. What is the condition that has to be met for inclusion?

all_users = ["Josephina", "Joseph", "Joey", "James", "Jovanotti", "Jill", "Jim"]
some_users = [u for u in all_users if len(u) < 8]

print(some_users)

# Only users whose names are less than 7 characters long are included in the list:
# Output: ['Joseph', 'Joey', 'James', 'Jill', 'Jim']