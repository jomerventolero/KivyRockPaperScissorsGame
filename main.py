#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy


import kivy
kivy.require('1.0.6')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from random import randint 


class GameBoxLayout(BoxLayout):
    
    def com(self, userpick):
        picks = ['ROCK', 'PAPER', 'SCISSOR']
        pick = picks[randint(0,2)]
        pc = 'You Lose!'
        pl = 'You Win!'
        cpick = self.ids.compick
        winner = self.ids.result
        if userpick == pick:
            winner.text = 'Draw!'
            cpick.text = pick
        elif (userpick == 'SCISSOR') and (pick == 'ROCK'):
            winner.text = pc 
            cpick.text = pick
        elif (userpick == 'ROCK') and (pick == 'SCISSOR'):
            winner.text == pl
            cpick.text = pick
        elif (userpick == 'SCISSOR') and (pick == 'PAPER'):
            winner.text = pl
            cpick.text = pick
        elif (userpick == 'PAPER') and (pick == 'SCISSOR'):
            winner.text = pc
            cpick.text = pick
        elif (userpick == 'ROCK') and (pick == 'PAPER'):
            winner.text = pc
            cpick.text = pick
        elif (userpick == 'PAPER') and (pick == 'ROCK'):
            winner.text = pl
            cpick.text = pick
           
        return self
        
        
class GameApp(App):
    def build(self):
        gn = GameBoxLayout()
        Clock.schedule_interval(gn.com, 1)
        return gn


if __name__ == '__main__':
    GameApp().run()

