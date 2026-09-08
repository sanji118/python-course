#without choice method
import random
name_list= ('sanji shifa nahid jarif').split()
random.shuffle(name_list)
a= random.randint(0, len(name_list)-1)
b= name_list[a]
print(b)
