my_list=[10,25,85,63]
new_list=set(my_list)
new_list.remove(max(new_list))
print("Second largest no is",max(new_list))