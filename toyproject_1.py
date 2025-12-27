import time
password = 11234561
season = input("계절을 입력하세요.")
people = int(input("인원 수를 입력하세요."))
if season == "여름":
    a =0
    for i in range(people):
        x = int(input("18/19/20/21/22/23중 하나 선택하시오"))
        if x == 18:
            a += 18
        elif x == 19:
            a += 19
        elif x == 20:
            a += 20
        elif x == 21:
            a += 21
        elif x == 22:
            a += 22
        elif x == 23:
            a += 23
    print(f"{a/people}도로 설정온도가 설정되었습니다.")

elif season == "겨울":
    a = 0
    for i in range(people):
        x = int(input("23/24/25/26중 하나 선택하시오"))
        if x == 23:
            a += 23
        elif x == 24:
            a += 24
        elif x == 25:
            a += 25
        elif x == 26:
            a += 26
    print(f"{a/people}도로 설정온도가 설정되었습니다.")
start = time.time()
while True:
    if time.time()-start>=5:
        print("5초가 지나 종료합니다")
        break
    passwoord = int(input("비밀번호입력:"))
    if passwoord == password:
        answer = int(input("설정온도를 입력하세요."))
        print(f"설정온도가 {answer}도로 설정되었습니다.")
    else:
        print("비밀번호가 일치하지 않습니다")