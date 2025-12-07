import load
import talking
import sys

load.starting()
talking.Human()
talking.Human()
print('나:target(all),input(무슨 일이세요?)')
print('이름모르는 이가:별일 아닐세.')
new_man = input('이름모르는 이가:새로 오신 분인가? ')
if new_man == "네":
    input('빌:나는 빌이라네.여기는 각자 할 일이 있다네.그래서 직업을 얻어야지.')
    input('나:네.알겠어요.')
else:
    input('이름모르는 이가:그래?알겠어.')
input('나:직업을 얻고 싶다!!!')
load.job()  # 함수로 호출해야 합니다.
input('나:바이러스를 죽이자!')
input('나:바이러스가 L3에 있어!')
gunuse = input('나:어디를 공격하지?\n1.왼쪽3번\n2.오른쪽2번\n3.왼쪽2번\n선택(숫자만 입력): ')
if gunuse == '1':
    input('나:잡았다!')
else:
    input('나:회피했네.')
    input('바이러스:하하하~')
    input('나:there are two virus in the turminul')
    choose = input('나:누구를 공격하지?\n1.turminul안의 두 바이러스\n2.turminul안의 두 벌어스\n3.turminul안의 두 바이러쉬\n선택(숫자만 입력): ')
    if choose == '1':
        input('나:제대로 죽였네~')
    else:
        sys.exit('으악!')
input('어쨌든 바이러스가 사라지긴 했어.근데 갑자기 탁자가 생겼고,그 위에 컴퓨터가 있어')
choosi = input('컴퓨터를 살펴볼까? (살피기 또는 아니요): ')
if choosi == "살피기":
    input('나:102030!외우자!')
else:
    input('그냥 가자')
input('나:@#$ @#$ @#$#@')
input('@#$ virus:@## ^& $%#^@')
input('에라 모르겠다~print(maker)!')
input('앱 엑세스:무엇을 하실 건가요?')
input('나:이 거대한 바이러스를 어떻게좀 해봐!')
input('sudo:비밀번호를 입력하십시오.')
num = input('비밀번호: ')
try:
    if int(num) == 102030:
        input('나:바이러스를 무찌렀다!')
        print('그렇게 이 이야기는 이렇게 끝이 납니다.')
        print('thank you for playing')
    else:
        input('바이러스:어라?그렇게 된다고?죽어라!')
        print('그렇게 주인공은 죽었답니다.')
except ValueError:
    input('입력 형식이 잘못되었습니다. 숫자 비밀번호를 입력해야 합니다.')
    print('그렇게 주인공은 죽었답니다.')