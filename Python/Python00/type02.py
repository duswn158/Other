# 문자 (single quotation/double quotation 의 차이 없음)

#single * 1
a = 'Hello, Python!'
print(a)

#single * 3
b = '''python's
Hello, world!        !!!!!
    Hello, Python '''
print(b)

c = 'python\'s \nHello, World!'
print(c)

#double * 1
d = "python's\nHello, World!"
print(d)

e =  '\"python\'s \nHello, World!\"'
print(e)

#double * 3
dd = """ python's
"Hello, World!" """
print (dd)

ee = "D:\\test"
print(ee)

        # raw string : \를 문자로 인식
f = r"c:\test"
print(f)

str01 = "Hello, "
str02 ="World!"
print(str01 + str02)
# 문자열에*가 됨
print(str01 * 3 + str02)
