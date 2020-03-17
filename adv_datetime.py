# datetime은 날짜를 위한 date 객체, 시간을 위한 time 객체를 합친 것이다. -> 모듈을 import해서 사용
import datetime # 내장 객체

def get_datetime():
    # 시간의 획득
    # 현재 시간 datetime의 now() 메서드
    dt = datetime.datetime.now()
    print("now:", dt)

    # 특정 날짜와 시간을 얻을 때는 생성자를 활용, 최소 년월일은 지정해야한다
    dt = datetime.datetime(1999, 12, 31)
    print("dt:", dt)
    # 만약 실존하지 않는 날짜일 경우 ValueError발생
    #dt = datetime.datetime(1999, 12, 55)
    #print("dt:", dt) -> ERROR

    # 주요 속성들로 year, month, day, hour, minute, second, microsecond
    print("dt의 연월일:", dt.year, dt.month, dt.day)

    # 요일의 확인 weekday() 메서드
    # 월 : 0~ 일 : 6
    print("1999-12-31일의 요일:", dt.weekday()) # -> 4 : 금요일

    # datetime에서 날짜만 확인 date() -> date 객체 확인
    # datetime에서 시간만 확인 time() -> time 객체 확인
    nowdate = datetime.datetime.now().date()
    nowtime = datetime.datetime.now().time()
    print("NOWDATE:", nowdate, type(nowdate), "NOWTIME:", nowtime, type(nowtime))
    # date 객체는 datetime이 가진 year, month, day 등 날짜 관련 속성들을 가지고 있다
    # time 객체는 datetime이 가진 시간관련 속성과 메서드들을 그대로 사용

def timedelta_ex():
    # timedelta : 두 datetime의 차이값
    current = datetime.datetime.now() # 현재 날짜 시간
    past = datetime.datetime(2001,1,1) # 과거 날짜 시간
    # 두 날짜는 대소 비교가 가능 : 미래 > 과거
    print(current > past) # current가 past보다 미래인가
    # 두 datetime은 차이값을 구할 수 있다 : timedelta
    diff = current - past
    print(diff, type(diff))

    # timedelta의 total_seconds -> 모든 속성을 합산 초단위로 반환
    print(diff.days, diff.seconds, diff.microseconds, diff.total_seconds())

    # datetime과 timedelta의 합산은 미래의 어떤 datetime이 된다
    # current로부터 365일이 지난 사람의 datetime
    print("current:", current)
    future = current + datetime.timedelta(days=365, seconds=0, microseconds=0)
    print("future:", future)

def format_date():
    """
    날짜의 포매팅 -> 문자열로 반환 :strftime
    """
    # 현재 datetime을 년- 월-일 시:분:초 형식으로 바꿔 봅니다
    current = datetime.datetime.now()
    # 문자열로 포매팅
    print(current.strftime("%Y-%m-%d %H:%M:%S"))

    # 포매팅 -> 0000년 00월 00일
    # locale Error(한글 윈도우:MS949)
    import locale
    locale.setlocale(locale.LC_ALL, "ko_KR.UTF-8")
    print(current.strftime("%Y년 %m월 %d일"))

    # 문자열로 된 날 짜 정보 -> datetime : strptime
    # strptime(문자열, 해독을 위한 형식문자열)
    s = "2019/11/20 16:00"
    dt = datetime.datetime.strptime(s, "%Y/%m/%d %H:%M")
    print("해독된 datetime:", dt)

if __name__ == "__main__":
    #get_datetime()
    #timedelta_ex()
    format_date()