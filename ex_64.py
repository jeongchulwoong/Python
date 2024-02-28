#lambda 매개변수 : 리턴값

power = lambda x : x*x

# def power(item) : 
#     return item*item

under_3 = lambda x : x < 3
# def under_3(item) :
#     return item < 3

list_input_a = [1,2,3,4,5]

# map() 함수 : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운
#리스트를 구성
output_a = map(power,list_input_a)
print(list(output_a))
#filter() 함수 : 조건 값만 거르고 출력
output_b = list(filter(under_3, list_input_a))
print(output_b)

