import sys
import sympy
input = lambda: sys.stdin.readline().rstrip()


def func():
    # 변수 지정
    x, y = sympy.symbols("x y")

    # 계산기 3을 입력 받을 때 까지 계속 돌림
    while True:
        print("=" * 100)
        print("""Sympy 을 이용한 수식계산기 입니다. 
원하는 옵션을 선택하세요.
(참고 : 제곱은 x ** 2로 나타낼수 있으며 루트는 x ** 0.5 로 나타낼수 있습니다.)

1. 방정식 (변수: x)
2. 연립 방정식 (변수: x, y)  
3. 종료 """)
        print("=" * 100)
        try:
            num = int(input())
        except:
            print("잘못된 입력 입니다. 다시 시도해 주세요.")

        # 변수 x 을 사용한 방정식 풀이
        if num == 1:
            print("식을 입력하여 주세요 : ", end="")
            math_ex = input().split("=")

            try:
                math_ex[0] = sympy.sympify(math_ex[0])
                math_ex[1] = sympy.sympify(math_ex[1])
                f = sympy.Eq(math_ex[0], math_ex[1])
                print(f"x 의 값은 : {sympy.solve(f)}")
                print("\n" * 5)

            except:
                print("잘못된 수식 입력입니다. 처음으로 돌아갑니다.")
                print("\n" * 5)
                continue

        # 변수 x, y 을 사용한 방정식 풀이
        elif num == 2:

            print("첫번 째 식을 입력하여 주세요 : ", end="")
            math_ex1 = input().split("=")

            print("첫번 째 식을 입력하여 주세요 : ", end="")
            math_ex2 = input().split("=")

            try:
                math_ex1[0] = sympy.sympify(math_ex1[0])
                math_ex1[1] = sympy.sympify(math_ex1[1])

                math_ex2[0] = sympy.sympify(math_ex2[0])
                math_ex2[1] = sympy.sympify(math_ex2[1])

                f1 = sympy.Eq(math_ex1[0], math_ex1[1])
                f2 = sympy.Eq(math_ex2[0], math_ex2[1])

                print(f"x, y의 값은 : {sympy.solve([f1, f2])}")
                print("\n" * 5)

            except:
                print("잘못된 수식 입력입니다. 처음으로 돌아갑니다.")
                print("\n" * 5)
                continue

        elif num == 3:
            print("시스템을 종료 합니다. ")
            exit()
        else:
            print("잘못된 입력 입니다. 다시 시도해 주세요.")
            print("\n" * 5)


if __name__ == "__main__":
    func()
