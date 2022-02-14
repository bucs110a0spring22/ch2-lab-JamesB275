
#Part A
import random
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost Per Week:", cost_per_week, type(cost_per_week))
classes_per_week = (3)
print("Classes Per Week:",classes_per_week,type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print("Cost Per Class(hey, that's pretty cheap!):",cost_per_class, type(cost_per_class))
#Part B
list_1=(22, "dickass computer", 43, "hey man",5)
random_list=(random.choice(list_1))
print(random_list,type(random_list))