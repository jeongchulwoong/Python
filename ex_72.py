# books = [{
#     "Title" : "Study Python alone",
#     "Price" : 18000
    
# }, {"Title" : "Study Machine Learning + Deep Learning alone",
#     "Price" : 26000
    
# }, {
#     "Title" : "Study JavaScript alone",
#     "Price" : 24000
# }]

# def price_function(book) :
#     return book["Price"]

# print("most chip book")
# print(min(books,key = price_function))
# print()
# print("most expensive book")
# print(max(books,key = price_function))
# print()
# print(books)

# books = [{
#     "Title" : "Study Python alone",
#     "Price" : 18000
    
# }, {"Title" : "Study Machine Learning + Deep Learning alone",
#     "Price" : 26000
    
# }, {
#     "Title" : "Study JavaScript alone",
#     "Price" : 24000
# }]

# # def price_function(book) :
# #     return book["Price"]

# price_function = lambda book : book["Price"]        #**lambda** 

# print("most chip book")
# print(min(books,key = price_function))
# print()
# print("most expensive book")
# print(max(books,key = price_function))
# print()
# print(books)

books = [{
    "Title" : "Study Python alone",
    "Price" : 18000
    
}, {"Title" : "Study Machine Learning + Deep Learning alone",
    "Price" : 26000
    
}, {
    "Title" : "Study JavaScript alone",
    "Price" : 24000
}]

print("Sort by price ascending")
#sort
books.sort(key = lambda book : book["Price"])

for book in books :
    print(book["Price"])
print()
#reverse
books.sort(key = lambda book : book["Price"], reverse = True)

for book in books :
    print(book["Price"])








