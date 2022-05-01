a = int(input('정수 a의 값을 입력하세요.'))
b = int(input('정수 b의 값을 입력하세요.'))
c = int(input('정수 c의 값을 입력하세요.'))

if a > b and a > c:
    print(f'최댓값은 {a}입니다.')
elif b > a and b > c:
    print(f'최댓값은 {b}입니다.')
elif c > a and c > b:
    print(f'최댓값은 {c}입니다.')