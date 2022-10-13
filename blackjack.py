import random
import time
def cardValue(card):
    value=0
    for i in card:
        if type(i)==int:
            value+=i
        elif i=='J' or i=='Q' or i=='K':
            value+=10
        else:
            value+=11
    return value

def win(myMoney, dellorCard, playerCard): 
    print(f'Dellor: {dellorCard} 카드합: {cardValue(dellorCard)}')
    print(f'Player: {playerCard} 카드합: {cardValue(playerCard)}')
    print(f'money: {myMoney}')
    print('승리!')
    print('-------------------------------------------------------')

def draw(myMoney, dellorCard, playerCard):   
    print(f'Dellor: {dellorCard} 카드합: {cardValue(dellorCard)}')
    print(f'Player: {playerCard} 카드합: {cardValue(playerCard)}')
    print(f'money: {myMoney}')
    print('비겼습니다.')
    print('-------------------------------------------------------')

def lose(myMoney, dellorCard, playerCard):
    print(f'Dellor: {dellorCard} 카드합: {cardValue(dellorCard)}')
    print(f'Player: {playerCard} 카드합: {cardValue(playerCard)}')
    print(f'money: {myMoney}')
    print('패')
    print('-------------------------------------------------------')

print('-------------Black Jack-------------')
myMoney = 100 # 초기 자금
while 1: # 1판이 끝날때마다 초기화되는 스페이스
    if myMoney == 0:  # 게임이 완전히 끝나는 조건
        print('You Lose!')
        break
    elif myMoney >= 200:
        print('You Win!')
        break
    round=0 # hit한 후 double하는 것을 막기 위해 설정 (hit를 하면 round+=1이 되어 double 선택을 제한함)
    deck=[] # 한 판마다 초기화 하기 위해 빈 리스트 생성
    dellorCard=[] 
    playerCard=[]
    for i in range(4): # 새로운 카드 덱을 만듦
        for j in ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"):
            deck.append(j)
    random.shuffle(deck) # 덱을 랜덤하게 섞음
    dellorCard.append(deck.pop()) # 딜러와 플레이어는 카드를 각 두 장씩 뽑음
    dellorCard.append(deck.pop())
    playerCard.append(deck.pop())
    playerCard.append(deck.pop()) 
    while 1: # 게임 시작 전 베팅과 예외처리
        print(f'money:{myMoney}') # 베팅 시 남은자금 표시
        bet=input('베팅할 금액을 입력하세요<1~20>: ') # 게임 시작 전 배팅
        if not bet.isdigit(): # bet에 입력된 값이 int형인지 아닌지를 판단
            print()
            print('1~20의 정수를 입력하세요.')
            print()
            continue
        elif int(bet)>myMoney: # 보유자금보다 베팅금액이 크면 다시 베팅
            print()
            print('자금이 부족합니다.')
            print()
        elif int(bet)>20 or int(bet)<1: # 베팅 금액이 1보다 작거나 20보다 클경우 다시 배팅
            print()
            print('1~20의 정수를 입력하세요.')
            print()
            continue
        else: # 정상적인 값이 입력되었을 경우
            bet=int(bet) # bet을 string으로 입력받았기 때문에 계산하기위해 int형으로 변환
            myMoney = myMoney-bet # 베팅 한 만큼 보유자금에서 차감
            break
    while 1: # 구체적인 플레이가 이뤄지는 스페이스
        print() # 가독성을 위해 한줄씩 띄움
        print('Dellor:  ?', dellorCard[1]) # 딜러의 첫 패는 히든 -> ?와 두번째 패를 출력
        print('Player: ', *playerCard) # 리스트 앞에 *붙여 괄호 제거 -> 첫번째와 두번째 패 출력
        print(f'money: {myMoney} / betting: {bet}') # 남은 자금과 현재 베팅한 금액 표시
        if cardValue(playerCard)==21: # 초기지급 카드 두장 합이 21이면 바로 승리
            print('Black Jack!')
            myMoney+=bet*2
            break
        print('<Stay: "s" / Hit: "h" / Double: "d">') # stay, hit, double중 하나 pick
        pick=input()
        print()
        if pick=='s' or pick=='S': # Stay를 골랐을때
            while 1:
                if cardValue(dellorCard)<=16: #딜러의 카드가 16이하일 경우 17이상이 될 때까지 카드를 뽑음
                    print('Dellor: ', dellorCard)
                    time.sleep(1.5) # 딜러가 카드를 받을 때 1.5초씩 딜레이를 줌
                    dellorCard.append(deck.pop())
                elif cardValue(dellorCard)>=22: #딜러의 카드가 22이상이면 바로 플레이어 승리
                    myMoney = myMoney+bet*2
                    win(myMoney, dellorCard, playerCard)
                    break
                elif cardValue(dellorCard)>=17: #딜러의 카드가 17~21이면 플레이어의 카드와 비교후 승패 나뉨
                    if cardValue(playerCard)==cardValue(dellorCard):
                        myMoney = myMoney+bet
                        draw(myMoney, dellorCard, playerCard)
                        break
                    elif cardValue(playerCard)>cardValue(dellorCard):
                        myMoney = myMoney+bet*2
                        win(myMoney, dellorCard, playerCard)
                        break
                    else:
                        lose(myMoney, dellorCard, playerCard)
                        break
        elif pick=='h' or pick=='H': # Hit를 골랐을때
            round+=1
            playerCard.append(deck.pop()) # 카드 1장을 뽑음
            if cardValue(playerCard)<=20: # 플레이어의 카드합이 20이하이면 계속진행
                continue
            elif cardValue(playerCard)==21: # 플레이어의 카드합이 21이면 바로 플레이어 승
                myMoney = myMoney+bet*2
                win(myMoney, dellorCard, playerCard)
                break
            else: # 플레이어의 카드합이 22이상이면 바로 플레이어 패
                lose(myMoney, dellorCard, playerCard)
                break
        elif (pick=='d' and round!=0) or (pick=='D' and round!=0):
            print()
            print('Hit 한 후 Double을 선택할 수 없습니다. Stay 혹은 Hit 중에서 선택하세요.')
            continue
        elif (bet<=myMoney and pick =='d') or (bet<=myMoney and pick=='D'): # 더블은 베팅을 두배로 늘리는 대신 무조건 카드 한장만 더 받고 턴종료
            myMoney-=bet # 베팅을 두 배로 늘림
            bet*=2
            playerCard.append(deck.pop()) # 카드 한 장을 받음
            while 1:
                if cardValue(playerCard)==21: # 플레이어 카드합이 21일경우 바로 승리
                    myMoney= myMoney+bet*2
                    win(myMoney, dellorCard, playerCard)
                    break
                if cardValue(playerCard)>21: # 플레이어 카드 합이 22이상일 경우 바로 패배
                    lose(myMoney, dellorCard, playerCard)
                    break
                if cardValue(dellorCard)<=16: #딜러의 카드가 16이하일 경우 17이상이 될 때까지 카드를 뽑음
                    print('Dellor: ', dellorCard)
                    time.sleep(1.5) # 딜러가 카드를 받을 때 1.5초씩 딜레이를 줌
                    dellorCard.append(deck.pop())
                elif cardValue(playerCard)<=20 and cardValue(dellorCard)<=21: # 플레이어 카드합 20이하, 딜러 카드합 21 이하일 경우 카드합 비교해서 승패 나눔
                    if cardValue(playerCard)==cardValue(dellorCard):
                        myMoney = myMoney+bet
                        draw(myMoney, dellorCard, playerCard)
                        break
                    elif cardValue(playerCard)>cardValue(dellorCard):
                        myMoney = myMoney+bet*2
                        win(myMoney, dellorCard, playerCard)
                        break
                    else:
                        lose(myMoney, dellorCard, playerCard)
                        break
                else: # 딜러의 카드합이 22이상일 경우 승리
                    myMoney= myMoney+bet*2
                    win(myMoney, dellorCard, playerCard)
                    break
        elif (bet>myMoney and pick =='d') or (bet>myMoney and pick=='D'): # 현재 베팅된 금액보다 보유자금이 적을경우 double선택 불가
            print('자금이 부족합니다.')
            continue
        else: # 잘못된 값 입력될 경우 재선택
            print()
            print('"s" , "h" , "d"중 한가지로 입력하십시오.')
            continue
        break