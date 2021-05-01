import pyupbit

access = "iMmQZkfooVW0nZswPxjgvzWxbeG5xcxX0xQzl9qx"          # 본인 값으로 변경
secret = "Pue8o8YVEx0CRCnQgvCThxOuFiYPCsBMGx2sgeJx"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

