#ソリティアの処理部分　Jsonで出力？してjsに渡す

from random import shuffle

class Trump:
    """
    トランプカード1枚
    trump(mark, number)
    mark: 1-♣ 2-♡ 3-♠ 4-♢
    number: 1から13の値
    マークと数字のタプル
    """
    def __init__(self, mark: int, number: int):
        marks = ["♣", "♡", "♠", "♢"]
        numbers = [ i for i in range(1, 14)]
        self.mark = marks[mark-1]
        self.number = numbers[number-1]
        self.state: bool = False    
    
    def __repr__(self):
        return (self.mark, self.number)
    
    def mark_color(self):
        red_mark = ["♡", "♢"]
        black_mark = ["♣", "♠"]
        if self.mark in black_mark:
            return "black"
        elif self.mark in red_mark:
            return "red"

class Deck:
    """
    トランプカードnセット
    deck(n)
    """

    def __init__(self, qty: int) -> list: 
        self.qty = qty
        self = [Trump(mark, number) for mark in range(1, 5) for number in range(1, 14)]
    
    def shuffle(self):
        shuffle(self)

    def get_card_from_top(self, num_card: int):
        """
        上から<num_card>枚のカードを取る
        :リストの後ろから<num_card>回Trumpオブジェクトをpopする
        """
        popped_item = []
        while i <= num_card:
            popped_item = self.pop()
            i+=1
        return popped_item
    
class Taebleu:  #場札
    def __init__(self, number:int) -> list:
        self = Deck.get_card_from_top(number)
    
    def where_trump(self, target_trump: Trump):
        for i in range(0, len(self)):
            if self[i] == target_trump:
                return i

    #放り込むもの：移動する（クリックする）トランプのindex
    #返してほしいもの：実際に移動する塊->list
    #中でやること：それがopenなのか？→クリックするトランプがリストのどこにあるのか？→それより後ろは全部openか？→それを含めてそれより後ろの塊をすべて返す
    def moving_stack(self, target_index) -> list:
        for i in range(target_index, len(self)):
            if self[i].state == False:
                print("Error: Bafuda.moving_stack cannot include 'closed' Trump.")
                break
        return  self[target_index:]

    @property
    def trump_top(self):
        return self[len(self)-1]


deck = Deck(1)
deck.shuffle

def printField(s, fc, fh, fs, fd):
    print("")
    print(" +-D----+             +-F()--+------+------+------+")
    print(" | stock|             |   C  |   H  |   S  |   D  |")
    print(" +------+             +------+------+------+------+")
    f'|  {s} |             |   {fc}   |   {fh}   |   {fs}   |   {fd}   |"'
    #print("| ---- |             | ---- | ---- | ---- | ---- |")
    print(" +------+             +------+------+------+------+")
    print("")

result = False
while result == False:
    inp = input("コマンドを入力してください。コマンドの一覧を見るにはhelpを入力。")
    if inp == "help":
        result == True
        print("山札をめくる: t or turn")
        print("カードを移動する: (動かしたいカードの位置) -> (動かしたい位置)")


'''
旧案
class stock:
    """
    山札
    """
    def __init__(self, rest_of_deck: Deck) -> list:
        self = rest_of_deck.get_card_from_top(len(rest_of_deck))
        #stockというリストの前のほうがトップ、後が底になる。（deckと逆順だが、この順だと後ろから前へ操作しないといけないので逆転させる）
        from collections import deque
        self.open_cards = []
        self.close_cards = deque([x for x in self])

    def flip_stock(self):
        if self.close_cards == []:
            self.close_cards = [x for x in self.open_cards]
        else:
            self.open_cards.append(self.close_cards.popleft())


class tableau:
    """
    場札
    """
    def __init__(self, num: int = 7) -> list:
        for i in range(num+1):
            self[i] = Deck.get_card_from_top(i)

    def display(self, index: int):
        display_list = []
        for card in self[index]:
            if card.state:
                display_list.append(card)
            else:
                display_list.append("(*,*)")
        return display_list
    
    def add(self, cards: list, index_move_to: int):
        if cards[0].mark

class foundation:
    """
    組札
    """
'''