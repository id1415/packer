from kivymd.app import MDApp
from kivy.lang import Builder
import json

with open('crans.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class MyApp(MDApp):
    reductor = False
    pr = False
    forteca = False
    pn25 = False

    def build(self):
        return Builder.load_file('kv.kv')


    def fort(self):
        if self.forteca == True:
            self.forteca = False
        else:
            self.forteca = True

    def reduc(self):
        if self.reductor == True:
            self.reductor = False
        else:
            self.reductor = True

    def pr_gross(self):
        if self.pr == True:
            self.pr = False
        else:
            self.pr = True

    def pn(self):
        if self.pn25 == True:
            self.pn25 = False
        else:
            self.pn25 = True

    def show(self):
        name = self.root.ids.text_field.text
        if name == '':
            self.root.ids.label.text = f'Ошибка!\nВведена пустая строка.'
        else:
            if self.pr:
                name += ' pr'
                if self.reductor:
                    name += ' reductor'
            elif self.forteca:
                name += ' forteca'
                if self.reductor:
                    name += ' reductor'
                elif self.pn25:
                    name += ' pn25'
            else:
                name += ' temper'
                if self.reductor:
                    name += ' reductor'
            try:
                if data[name][0] == 'коробка':
                    vsego = data[name][1]
                    v_korobke = data[name][2]
                    korobok = data[name][3]
                    self.root.ids.label.text = f'Всего - {vsego}\nКоробок - {korobok}\nВ коробке - {v_korobke}'
                elif data[name][-1] == '+':
                    vsego = data[name][0]
                    v_ryadu = data[name][1]
                    ryadov = int(vsego / v_ryadu)
                    self.root.ids.label.text = f'Всего - {vsego}+\nРядов - {ryadov}\nВ ряду - {v_ryadu}'
                else:
                    vsego = data[name][0]
                    v_ryadu = data[name][1]
                    ryadov = int(vsego / v_ryadu)
                    self.root.ids.label.text = f'Всего - {vsego}\nРядов - {ryadov}\nВ ряду - {v_ryadu}'
            except KeyError:
                self.root.ids.label.text = f'Ошибка!\nКрана нет в базе.'

if __name__ == "__main__":
    MyApp().run()
