def judge(you, enemy):
    if you == enemy:
        output = '引き分け'
    if you == 1 :
        if enemy == 2:
            output = '勝ち'
        elif enemy == 3:
            output = '負け'
                
    if you == 2 :
        if enemy == 3:
            output = '勝ち'
        elif enemy == 1:
            output = '負け'
                
    if you == 3 :
        if enemy == 1:
            output = '勝ち'
        elif enemy == 2:
            output = '負け'
            
    return output

