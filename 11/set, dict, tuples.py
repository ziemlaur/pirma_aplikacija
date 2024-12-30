# a_set = {1,2,3,4, 'a'}
# b_set = {1,2,3,5,6, 'b'}

# print(a_set.union(b_set))
# print(b_set.intersection(a_set))
# print(a_set.difference(b_set))
# print(a_set.symmetric_difference(b_set))


# l = [1,1,2,2,3,4,5,5,5,8,8,1,2]
# l = set(l)
# print(l)


                                # dict
# d1 = {'cost_price': 32.67, 
# 'sell_price': 45.00, 
# 'inventory': 1200
# }    

# d2 = {'cost_price': 225.89, 
# 'sell_price': 550.22, 
# 'inventory': 100
# }   

# d3 = {'cost_price': 2.77, 
# 'sell_price': 7.95, 
# 'inventory': 8500
# }   
# pelnas = 0

# pelnas = (((d1['sell_price'] - d1['cost_price'])*d1['inventory']) +
# ((d2['sell_price'] - d2['cost_price'])*d2['inventory']) +
# ((d3['sell_price'] - d3['cost_price'])*d3['inventory'])
# )

# print(pelnas)
                                    # su for loopu 

prekes  =[{'cost_price': 32.67, 
'sell_price': 45.00, 
'inventory': 1200
},    

{'cost_price': 225.89, 
'sell_price': 550.00, 
'inventory': 100
},   

{'cost_price': 2.77, 
'sell_price': 7.95, 
'inventory': 8500}   
]

pelnas = 0
for i in prekes: 
    pelnas += (i['sell_price'] - i['cost_price'])*i['inventory']
print(pelnas)