def test() : 
    print("funtion call.")
    yield "test2"        #generator
print("Passed A point")
test()

print("Passed B point")
test()

print(test())   #None


