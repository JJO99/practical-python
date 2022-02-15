import csv

types = [str, int, float]
f = open('./Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

r = list(zip(types,row))

converted = []
for func, val in zip(types, row):
    converted.append(func(val))

#########
temp = dict(zip(headers,converted))
temp2 = {name: func(val) for name, func, val in zip(headers, types, row)}

#########
f2 = open('./Data/dowstocks.csv')
rows2 = csv.reader(f2)
headers2 = next(rows2)
row2 = next(rows2)

types2 = [str, float, str, str, float, float, float, float, int]
converted2 = [func(val) for func, val in zip(types2, row2)]
# type2에서 하나, row2에서 하나 원소를 가져와 zip해서 튜플로 반환
# 그걸 다시 func와 val에 담고
# func(val) 형태로 함수를 가동한 다음
# 그 값을 converted2 리스트에 담는다.
# 예를 들어 str('AA') 형태
# 굳이 이래야 하는 이유는, 기본적으로 받은 숫자도 전부 str 타입이기 때문이다.
# 그래서 원소로 계산을 하려면 이렇게 타입을 적절한 것으로 바꿔치기 해줘야함.
record2 = dict(zip(headers2, converted2))