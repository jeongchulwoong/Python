#format()함수로 숫자를 문자열로 변환
string_a = "{}".format(10)
print(type(string_a), string_a)

format_a="{}만원".format(5000)
print(format_a)
format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
print(format_b)
format_c = "{}{}{}".format(3000,4000,5000)
print(format_c)

format_d = "{}{}{}".format(1, "문자열", True)
print(format_d)

output_a = "{:d}".format(52)
print("#기본")
print(output_a)

output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)
print("#특정 칸에 출력하기")
print(output_b)
print(output_c)
print()

output_d = "{:05d}".format(52)
output_e = "{:05d}".format(52)
print("#빈칸을 0으로 출력하기")
print(output_d)
print(output_e)
print()

output_f = "{:=+05d}".format(52)    #기호를 앞으로 밀기 : 양수
output_g = "{:=-05d}".format(-52)   #기호를 앞으로 밀기 : 음수
print(output_f)
print(output_g)
print()

output_h="{:f}".format(52.273)
output_i="{:15f}".format(52.273)    #15칸 만들기
output_j="{:+15f}".format(52.273)   #15칸 부호추가하기
output_k="{:=+015}".format(52.273)  #15칸에 부호 추가하고 0으로 채우기
print(output_h)
print(output_i)
print(output_j)
print(output_k)

output_l="{:15.3f}".format(52.273)      #소수점 아래자리수 지정
output_m="{:15.2f}".format(52.273)    
output_n="{:15.1f}".format(52.273)   
print(output_l)
print(output_m)
print(output_n)
print()

output_o = 52.0
output_p = "{:g}".format(output_o)      #의미없는 소수점 제거
print(output_o)
print(output_p)



