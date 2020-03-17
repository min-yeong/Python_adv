# 객체의 이해
# global 변수 : 모듈 전체에서 공유되는 심볼
g_a = 1
g_b = "홍길동"

def func():
    # 내부의 로컬 심볼 영역 생성
    # 객체에 접근할 경우 로컬 영역을 먼저 확인, 없으면 상위로 이동하여 검색
    l_a = 1
    l_b = "임꺽정"
    # 로컬 영역 심볼 테이블 확인
    print(locals())

class MyClass:
    x = 10
    y = 20

def symbol_table():
    # 전역 변수 심볼 테이블 출력
    print(globals())
    print(type(globals())) # dict형식으로 반환(포함ㅇ ㅕ부 확인가능), 앞 뒤에 __ -> 파이선 내부에서 사용하는 심볼, 변경불가
    # 사용자 정의 함수 실행
    func()
    # global의 포함여부 확인
    print("g_a in global?", "g_a" in globals())
    # 내부에 __dict__ 을 확인하면 해당 객체 내부의 심볼 테이블 확인 가능
    # 사용자 정의함수 func 의 심볼 테이블 확인
    print(func.__dict__)
    print(MyClass.__dict__)

def object_id():
    # 변수는 심볼명과 객체의 주소값을 함께 가지고 관리가 됨 (심볼 테이블 안에서)
    # id()함수로 객체의 주소 확인 가눙, is 연산자로 두 객체의 동일성을 확인 할 수 있다
    i1 = 10
    i2 = int(10)
    print("int:", hex(id(i1)), hex(id(i2)))
    print(id(i1)==id(i2)) # 두개의 아이디값이 같다 -> 같은 객체다
    print(i1 is i2) # 두 객체가 동일 객체인지(같은 주소) 확인

    # mutable 객체
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print("lst1 == lst2?", lst1==lst2)
    print("lst1 is lst2?", lst1 is lst2)
    # == : 동등성의 비교, is : 동일성의 비교

def object_copy():
    a = [1, 2, 3]
    b = a # 단순 레퍼런스 복사
    print(a, b)
    b[0]= 4
    print(a, b) # 두개가 같은 객체가 되기 때문에 같이 바뀜

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b, 100]
    print(c)

    # 객체 복제를 위한 copy 모듈
    import copy
    # c를 복제를 해서 d 생성
    d = copy.copy(c)
    print(d)
    d[2] = 10
    print(c, d) # c 객체는 변하지 않고 보존됌
    d[1][0] = 10
    print(c, d)
    print("얕은 복제 : c is d?", c is d)
    print("얕은 복제 : c[0] is d[0]?", c[0] is d[0])
    # c객체의 값도 변경됌, 새 객체를 만들지만 내부에 있는 요소의 주소값을 그대로 복제한다 -> 얕은 복제
    d = copy.deepcopy(c) # 위의 문제를 해결하기 위한 깊은 복제
    print(c, d)
    print("깊은 복제 : c is d?", c is d)
    print("깊은 복제 : c[0] is d[0]?", c[0] is d[0])

if __name__ == "__main__":
    #symbol_table()
    #object_id()
    object_copy()