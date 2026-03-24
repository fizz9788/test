

import numpy as np

# list=np.array(['a','b','c','d','e',1,2,3,4,5,6,'u','i',1.2])
list=np.array([1,2,3,4,5,6,1.2])
new_list=np.where(list>3)
print(type(new_list))
print(new_list)
where_list=list[new_list]
print(where_list)
print(type(where_list))
