# 모듈 명 출력 __name__ : 최상위 모듈로 실행될 때는 __main__, 다른 묘듈에서 import되었을 때는 파일명 그자체
print("모듈의 이름:", __name__)

# 흐름 제어 (조건문, 반복문)
def if_statement():
    """
    조건문
    """
    # 키보드로부터 금액 입력, 10000원 이상이면 by taxi, 2000원이면 by bus, 그렇지 않으면 On foot
    print("======if elif else")
    # 키보드에서 금액 입력
    money = input("얼마 가지고 있니?")
    money = int(money) # 문자형으로 input 되기 때문에 int 형으로 형변환
    message = ""
    if money >= 10000:
        message = "By Taxi"
    elif money >= 2000:
        message = "By Bus"
    else:
        message = "On Foot"
    print("가지고 있는 돈 : {}, 이동 방법 : {}".format(money, message))

def if_expr():
    """
    조건 표현식
    """
    print("======if elif else")
    money = int(input("얼마 가지고 있니?"))
    message = "By Taxi" if money >= 10000 \
                        else "By Bus" if money >= 2000 \
                        else "On Foot"
    print("가지고 있는 돈 : {}, 이동 방법 : {}".format(money, message))

def for_ex():
    """
    for 반복문
    """
    # 인덱스 반복 구문은 없고 순차자료형의 각 요소를 순회하는 loop
    a = ["개", "고양이", "소", "말"]
    for animal in a :
        print("item:", animal)
    else :
        print("for문이 정상적으로 종료 되었을 때 한번 실행")

    # 값과 함께 인덱스도 필요한 경우 : enumarate 함수(인덱스, 요소값)
    for index, animal in enumerate(a):
        print("{}번째 동물은 {}(이)다".format(index+1, animal))
    else:
        print("for문이 정상적으로 종료 되었을 때 한번 실행")

    # dict의 순회 -> key 목록 loop
    dct = {"name":"홍길동", "age":"25", "job":"도둑"}
    for key in dct:
        # 사전의 키가 할당
        print("KEY : {} -> VALUE : {}".format(key, dct[key]))

    # dct 순회시 key와 value가 함께 필요한 경우
    for key, value in dct.items(): # 키와 벨류의 쌍튜플
        print("KEY : {} -> VALUE : {}".format(key, dct[key]))

    # 범위의 loop -> range(시작, 끝경계, 간격)
    r = range(1, 101)
    # 1 ~ 101 까지의 수 중 짝수의 합
    total = 0
    for num in r :
        if num % 2 == 0:
            total += num
    print("1~100까지 짝수의 합:", total)
    # continue : 아래에 남아있는 문장은 더이상 실행하지 않고 다음번 loop로 이동
    # break : 루프를 더이상 진행하지 않고 루프 밖으로 탈출

    # 연습문제1. 구구단출력
    dans = range(2, 10)
    dans2 = range(1, 10)
    for dan in dans :
        for dan2 in dans2 :
            print("{}단 * {} = {}".format(dan, dan2, dan*dan2))

    # 연습문제2. * 을 이용해 삼각형 출력
    """
    *****
    ****
    ***
    **
    *
    """

def while_ex():
    """
    while 반복문
    - 특정 조건이 만족되는 동안 루프를 실행
    - 조건을 True로 부여하면 무한루프가 생성
    """
    # 1~100에서 짝수만 합산
    i = 1
    total = 0
    while i <= 100:
        if i % 2 == 0:
            total += i
        i += 1
    else:
        print("루프가 정상 종료 되었습니다")
        print(total)

def list_comp():
    """
    List Comprehension
    - 기존 순자차료형을 기반으로 조건에 맞는 데이터 추출
    - 연산식을 수행하여 새로운 리스트를 만들어보자
    - Syntax : [표현식 for 항목 in 순회가능 객체 if 조건]
    """
    # 기존 방식
    data = range(1, 11)
    # data 객체를 제곱해서 새 리스트 생성
    result = []
    for num in data:
        result.append(num * num)
    print("RESULT:", result)

    # 리스트 내포 방식
    results = [num**2 for num in data]
    print("RESULTS(내포):", results)

    # 내포시 if 표현식을 연결하면 조건에 맞는 데이터만 추출해서 연산에 포함시킬 수 있다
    words = "a as bat cat dove python".split() # 리스트
    print("WORDS:", words)
    # words(str list)에서 요소의 길이가 3글자 이상인 요소들만 추출해서 새 list 만들기
    filtered = [word.upper() for word in words if len(word)>=3]
    print("Filtered words:", filtered)

    # 연습문제 : 1~100까지의 수 중에서 짝수의 리스트를 새로 만들기

def set_comp():
    """
    Set Comprehension
    - Syntax : {표현식 for 객체 in 순회가능객체}
    """
    # words list 안에서 길이가 2글자 이하인 set
    words = "a cat python as bat cat dove python".split()  # 리스트
    filtered = {word.upper() for word in words if len(word)<=2}
    print("filtered set:", filtered)

    # 문자열 리스트에서 문자열의 길이를 set으로 저장
    filtered = {len(word) for word in words}
    print("filtered set length:", filtered)

def dict_comp():
    """
    사전의 내포
    - Syntax : {카표현식:값표현식 for 객체 in 순회기능객체}
    """
    words = "Life is too shoer you need python".upper().split()
    print("words:", words)
    # 키로는 개별 단어 값으로는 해당 단어의 길이
    dct = {word:len(word) for word in words}
    print("dict comp:", dct)

if __name__ == "__main__":
    #if_statement()
    #if_expr()
    for_ex()
    #while_ex()
    #list_comp()
    #set_comp()
    #dict_comp()