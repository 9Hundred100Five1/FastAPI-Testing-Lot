a = int(input("몇개를 출력 할까요?: "))

for i in range(a):
    # 짝수 = 2로 나눈 나머지가 0 홀수 그외 전부 0은 자연수가 아니기 때문에 PASS
    print("+" if i%2==0 else "-", end="")