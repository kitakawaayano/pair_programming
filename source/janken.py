import player
import computer
import janken_judge
def janken_main():
    count = 0
    enemy_count = 0
    for i in range(1,4):
        print(f'----- ラウンド {i} -----')
        you = player.pon()
        enemy = computer.pon()
        
        if you == 1:
            you_hand = 'グー'
        elif you == 2:
            you_hand = 'チョキ'
        elif you == 3:
            you_hand = 'パー'
        else:
            print('不正な入力です。')
            continue
            
        if enemy == 1:
            enemy_hand = 'グー'
        elif enemy == 2:
            enemy_hand = 'チョキ'
        elif enemy == 3:
            enemy_hand = 'パー'
        
        
        print(f'あなたの手：{you_hand}')
        print(f'コンピュータの手：{enemy_hand}')
        output = janken_judge.judge(you,enemy)
        if output == '引き分け':
            print('引き分けです。\n')
        elif output == '勝ち':
            print('あなたの勝ちです。\n')
            count += 1
        elif output == '負け':
            print('コンピュータの勝ち。\n')
            enemy_count += 1

    print('【最終結果】')
    print(f'あなた：{count}')
    print(f'コンピュータ：{enemy_count}')
    
    if count == enemy_count:
        print('引き分けです。')
        
    elif count > enemy_count:
        print('あなたの総合勝利です。')
    else:
        print('コンピュータの総合勝利です。')
            
if __name__ == '__main__':

    janken_main()