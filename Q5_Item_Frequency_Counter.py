def count_items(items_list):      # function to count frequency of items

count = {}                        # empty dictionary to store count

for item in items_list:          # checking each item   
    count[item] = count.get(item, 0) + 1       # increase count if item exists

return count

items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']   # testing values

print(count_items(items))
