squared = []

for n in range(11):
    squared.append(n**2)
#uncomment to run this
#print(squared)

#var_name = [ out_exp for loop_var in collection cond ]

squared = [ n**2 for n in range(11) if n % 2 is 0]
print(squared)
