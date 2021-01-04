import pandas as pd

# 시리즈 : 레이블과 값이 모두 표시되는 형태
ser = pd.Series([5,7,9])
ser2 = ser + ser
ser3 = ser.add(ser)

# iloc : 행의 인덱스를 읽음

df = pd.DataFrame(ser)
print(df[0])
print(df.iloc[0])
print(df.iloc[0,0])
print(df[0][1:2])

# 인덱스를 관리하는 속성 이해

df = pd.DataFrame(data=[[0, 1, 2], [3, 4, 5]], index=list('ab'), columns=list('cde'))
print(df)