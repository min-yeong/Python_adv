"""
Class
- 새로운 이름 공간을 지원하는 단위 : 데이터의 설계도
- 새로운 클래스는 새로운 자료형을 정의한느 것
- 인스턴스는 이 자료형의 객체를 생성하는 것
- 클래스와 인스턴스는 직접적인 연관관계를 갖는다
- 인스턴스에서 클래스 멤버의 접근은 가능하지만 클래스 멤버에서 인스턴스 멤버의 접근은 불가
"""
class MyString(str): #str을 상속받은 새로운 클래스
    pass

# 특정 클래스를 상속받지 않을 경우, object 상속
s = MyString() # 생성자 호출
print(type(s))

# 어떤 클래스를 상속 받은 클래스인가?
# __bases__ -> 부모의 목록을 튜플로 반환
print("MyString의 부모:", MyString.__bases__)

# 특정 부모를 상속받지 않을 경우 () 는 없어도 된다
class myobj: # 기본적으로 object를 상속
    pass

print(myobj.__bases__)

# 파이썬은 여러 부모로부터의 상속을 허용한다
class Complex(str, myobj):
    # str로부터 모든 멤버들,
    # myobj로부터 모든 멤버들을 물려받는다
    pass

print("Complex의 부모:", complex.__bases__)

# 특정 클래스가 다른 클래스의 자식인지 확인
# issubclass 함수
print("Complex가 str의 자식인가?", issubclass(Complex, str))

# 클래스의 생성
# 인스턴스를 위한 멤버는 항상 self를 붙여준다
class Point:
    # 클래스 멤버:
    # 클래스 이름 공간 내에 생성
    # 모든 인스턴스 멤버 공유
    # 클래스 멤버는 인스턴스 생성 없이도 사용할 수 있다
    instance_count = 0

    def __init__(self, x=0, y=0): # 생성자
        # 파이썬은 여러 개의 생성자를 만들 수 없으므로
        # 범용적으로 사용될 수 있는 유일한 생성자를 작성
        self.x = x
        self.y = y
        Point.instance_count += 1

    def __del__(self): # 소멸자
        # 객체가 제거될 때 호출
        Point.instance_count -= 1
    def __str__(self): # 문자열 출력
        # str() 호출 혹은 print를 할때 사용되는
        # 비공식 문자열( 일반 사용자 대신
        return "Point x={}, y={}".format(
            self.x, self.y
        )

    def __repr__(self): # 문자열 출력
        # 개발자용, 공식문자열
        # repr() 함수로 전달받을 수 있다
        # 이 문자열로 해당 객체를 복원해 낼 수 있어야 한다
        return "Point({}, {})".format(
            self.x, self.y
        )

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # 연산자 오버로딩 : 새로운 데이터 타입에 필요한 연산자의 행동을 재정의하는 것
    # 산술연산자 오버로딩 예제
    def __add__(self, other):
        # Point(self) + other
        # other의 타입을 점검해서 각기 다른 행동을 취하도록 구분
        if isinstance(other, Point):
            # 합산된 객체가 Point
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int):
            self.x += other
            self.y += other
        else:
            self += other
        return self

    # 역이항 연산자 : other + point
    def __radd__(self, other):
        if isinstance(other, str):
            return other + str(self)
        elif isinstance(other, int):
            self.x += other
            self.y += other
        else:
            self + other
        return self

def bound_class_method():
    # 생성된 인스턴스를 통해 직접 매서드에 접근하는 방법
    p = Point()
    # bound 방식의 경우, 첫 번째 인자 self는 전달하지 않아도 된다
    p.setX(10)
    p.setY(20)

    print("Point p: {}, {}".format(p.getX(), p.getY()))
    print(p.getX, p.getY())

# bound_class_method()

def unbound_class_method():
    # 클래스를 통해 우회 접근하는 경우
    # 메서드에 부여된 self 인자에 실제 객체의 주소 전달
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)

    print("Point p: {}, {}".format(Point.getX(p),Point.getY(p)))
    print(Point.getX, Point.getY)

# unbound_class_method()

def class_member():
    p1 = Point()
    p2 = Point()

    # 클래스 멤버는 모든 인스턴스에서 접근 가능
    # 생성 없이도 직접 접근가능

    print("p1의 instance_count의 주소:", id(p1.instance_count))
    print("p2의 instance_count의 주소:", id(p2.instance_count))
    # 클래스 멤버의 변경
    # 공유 메모리 영역으로 활용할 수 있다
    Point.instance_count += 1
    print("p2의 instance_count:", p2.instance_count)

# class_member()

def lifecycle():
    # 생성자와 소멸자 테스트
    p1 = Point() # 생성자의 기본값이 사용
    print(p1)
    print("instance_count:", Point.instance_count)

    p2 = Point(x=20, y=30)
    print("instance_count:", Point.instance_count)

    del p2
    print("instance_count:", Point.instance_count)

# lifecycle()

def str_repr():
    p = Point(10,20)
    print(p) # __str__ 호출

    print("포인트 p="+str(p)) #__str__

    # repr 함수를 사용하면 __repr__ 문자열을 얻을 수 있다
    print("repr of p:", repr(p))

    #eval 함수를 사용하면 파이썬 코드를 테스트할 수 있다
    # 이떄 repr 로 전달받은 문자열(개발자용)을 넘겨주면
    #같은 객체가 복원되어야 한다
    p_repr = eval(repr(p))
    print(p_repr, type(p_repr))

#str_repr()

def test_overloading():
    # 연산자 오버로딩
    p = Point(10, 20)
    print("p:", p)
    p2 = Point(30, 40)
    print("산술연산자 테스트:", p+p2)
    print("Point + int:", p+20)

    print("int + Point", 20+p)
    # int입장에서 point와의 + 불가, point입장에서 int 합산을 재정의 : 역이항
    print("Point p ="+p)

test_overloading()