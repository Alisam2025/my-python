#using individual values from a list using fstring
bicycle = ['trek', 'cannondale', 'red', 'mountain bike']    
message = f"My first bicycle is a {bicycle[0]}."
print(message)
message = f"My second bicycle is a {bicycle[1]}."
print(message)
message = f"My third bicycle is a {bicycle[2]}."
print(message)
message = f"My fourth bicycle is a {bicycle[3]}."
print(message)
print()
print()
# USING NEGATIVE INDEXING
message = f"My first bicycle is a {bicycle[-4]}."
print(message)
message = f"My second bicycle is a {bicycle[-3]}."
print(message)
message = f"My third bicycle is a {bicycle[-2]}."
print(message)
message = f"My fourth bicycle is a {bicycle[-1]}."
