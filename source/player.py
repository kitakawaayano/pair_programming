def pon():
    print('１．グー')
    print('２．チョキ')
    print('３．パー')
    
    you = int(input('あなたの手を選択してください'))
    if you == 1 or you == 2 or you == 3:
        return you
    else:
        print('正しい値を入力してください。')
        pon()
