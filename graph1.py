import matplotlib .pyplot as plt

x = [150,200,250,300,350,400]
y1 = [89 , 92, 90 , 80 , 87 , 90 ] # Random Forest
y2 = [86 , 84 , 84 , 76 , 82 , 89] # SVM
y3 = [84 , 86 , 85 , 74 , 84 , 85] # Decision Tree
y4 = [83 , 90 , 86 , 73 , 81 , 87] # ANN

plt.title('Comparison between algorithms accuracies with different size of dataset ')
plt.plot(x , y1 , marker = '.' , markersize = 6 , label = 'Random Forest')
plt.plot(x , y2  , marker = 'o' , markersize = 6 , label = 'SVM')
plt.plot(x , y3  , marker = 'D' , markersize = 6 , label = 'Decision Tree')
plt.plot(x , y4  , marker = '+' , markersize = 6 , label = 'ANN ')
plt.xlabel('Dataset Size')
plt.ylabel('Accuracy')
plt.legend()

plt.show()


x = [82,85,83,77,80]
# # # y1 = [89 , 92, 90 , 80 , 87 , 90 ]
# # # y2 = [85 , 82 , 86 , 83 , 85 , 87]
# plt.title('Accuracy Line Graph')
# y = ['SVM' , 'Random Forest' , 'Decision Tree' , 'Naive Bayes' , 'ANN']
# plt.plot(y, x ,  linestyle = 'dashed' , marker = '.' , markersize = 8)
# # plt.plot(x , y2  , marker = 'o' , markersize = 8 , label = 'Previous Papers')
# plt.xlabel('Algorithms')
# plt.ylabel('Accuracy')

# plt.show()