# local -> encloud -> global -> builtin
x = 1 # Global

def scope_func(a):
    print("Scope Function:", locals())
    # a -> 외부로부터 넘어온 객체가 local 심볼에 할당
    # x => Global
    print("x is in global?", "x" in globals())
    return a + x
#scope_func(10)

def scope_func2(a):
    x = 2
    print("scope_func2:", locals())
    return a + x
#print(scope_func2(10))

def scope_func3(a):
    # global 객체를 함수 내부에서 사용하고자 할 경우
    # 할당 이전에 global 을 지정
    global x # local이 아닌 global 객체를 사용할 것을 선언함, 주의 : 가능하면 글로벌 객체를 내부에서 변경하지 않을 것을 권장
    x = 3 # 위의 global 변수도 함께 변경
    print("scope_func3:", locals())
    return a + x
#print(scope_func3(10))
#print("x:", x) # global 영역 값이 나옴

# 함수(기능의 집합)의 선언 (주로 가변인자와 키워드 인자 중심으로 정리)
# 입력값이 없을 수도 잇고 출력이 없을 수도 있다. 함수는 return으로 종료되며 함께 결과값 반환 가능
# 값을 return하지 않았거나 끝날때까지 return 이 없는 경우 -> None 반환
def times(a, b):
    return a * b
# 함수자체도 객체로 판단 -> 다른 식별자에 할당 가능, 다른 함수와 인수로 전달가능
fun = times
print("fun:",  type(fun))
# 객체가 호출 가능한 객체(함수)인지 확인 : callable
print("is fun callable?", callable(fun))
# 만약 객체가 함수인지 판별한 이후에 호출할 경우
if callable(fun): print(fun(10, 20))

# 인수의 기본값
def incr(a, step=1):
    return a+step
print(incr(10)) # 두번째 인자 step이 가본값을 가지고 있으므로 기본값으로 세팅
print(incr(10, 2)) # 기본값을 무시하고 새로운 값을 세팅

# 기본적으로 python은 인수의 이름을 명시해서 인자를 전달 할 수 있다 -> 인자의 순서는 중요하지 않음 -> 가독성증가
print(incr(step=3, a=10))

# 가변인수 : 정해지지 않은 개수의 인자를 받을 때 가변인자를 받을 변수 앞에 * 명시 -> 순차 자료형으로 변환되어 입력
# 여러개의 인자값을 넘겨받아서 해당 인자가 int이거나 float이면 합산, 그렇지 않으면 합산에서 제외 최종합계 return
def get_total(*args):
    total = 0
    #print(args, type(args))
    for x in args:
        # 합산 가능한 타입인지 체크
        if isinstance(x, (int, float)):
            total += x
    return total
print(get_total(1, 2, 3, 4, 5))
print(get_total(1, 2, 3, 4, 5, "Python", (1, 2, 3)))

# 고정인자와 가변인자 키워드 인자 : 순서가 중요함, 고정인자 -> 가변인자 -> 키워드인자
def func_args(a, b, *args, **kwd):
    # a, b는 고정인자로 반드시 넘겨줘야함
    # 나머지 인자는 args로 넘어올것 (tuple), 그 다음인자는 키워드(dict)
    print("고정인자:", a, b)
    print("가변인자:", args)
    print("키워드인자:", kwd)
    if "option1" in kwd:
        print("option1이 {}로 설정되었습니다.".format(kwd['option1']))
func_args(1, 2, 3, 4, 5, 6, option1="옵션1", option2="옵션2")

# 함수도 객체이므로 ㅏ른 함수의 인자로 넘겨줄 수 있다 callback 패턴 구현
def calc(a, b, func):
    # 계산을 위한 수 2개
    # 계산식 함수 func 를 전달
    # 넘겨받은 func가 호출 가능 객체인지 확인
    if callable(func):
        return func(a, b) # 대상함수는 외부로부터 주입
def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
print(calc(10, 20, plus))
print(calc(10, 20, minus))

# Lambda 함수 : 익명 함수
print(calc(10, 20, lambda a,b: a*b)) # 즉석에서 곱셈함수 전달
# Lambda함수를 이용한 sort 키함수 정의
words = "Life is too short you need python".upper().replace(",", "").split()
print("WORDS:", words)
# sort 할때 정렬기준 key 함수를 lambda로 전달, 단의 길이를 역순 정렬 함수를 람다로
sorted_words = sorted(words, key=lambda word:len(word), reverse=True)
print("Sorted Words:", sorted_words)

# 1 ~ 20 까지 수열을 4로 나눴을 때의 나머지 순으로 정렬
nums = range(1, 21)
print("nums:", list(nums))
print("sorted nums % 4 ASC:", sorted(nums, key=lambda n:n%4))