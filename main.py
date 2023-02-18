from kivymd.app import MDApp
from kivy.lang import Builder
import json

with open('crans.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


KV = '''
MDFloatLayout:
    MDTextField:
        id: text_field
        hint_text: ''
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
        font_size: 30
        mode: 'round'
        size_hint_x: None
        width: 150
        on_text_validate: app.show()

    MDIconButton:
        icon: 'check-circle-outline'
        icon_size: "56sp"
        pos_hint: {'center_x': 0.9, 'center_y': 0.9}
        on_release: app.show()

    MDLabel:
        id: label
        text: ""
        pos_hint: {'center_x': .6, 'center_y': 0.30}
        font_size: 30
    
    CheckBox:
        pos_hint: {'center_x': .9, 'center_y': .75}
        size_hint: (None, None)
        size: (48, 48)
        group: 'type'
        on_active: app.pr_gross()
        color: 'black'
    MDLabel:
        text: "PR/Gross"
        pos_hint: {'center_x': .6, 'center_y': .75}
        font_size: 30

    CheckBox:
        pos_hint: {'center_x': .9, 'center_y': .65}
        size_hint: (None, None)
        size: (48, 48)
        group: 'type'
        on_active: app.fort()
        color: 'black'
    MDLabel:
        text: "Forteca"
        pos_hint: {'center_x': .6, 'center_y': .65}
        font_size: 30
    
    CheckBox:
        pos_hint: {'center_x': .9, 'center_y': .55}
        size_hint: (None, None)
        size: (48, 48)
        on_active: app.reduc()
        color: 'black'
    MDLabel:
        text: "С редуктором"
        pos_hint: {'center_x': .6, 'center_y': .55}
        font_size: 30

    CheckBox:
        pos_hint: {'center_x': .9, 'center_y': .45}
        size_hint: (None, None)
        size: (48, 48)
        on_active: app.pn()
        color: 'black'
    MDLabel:
        text: "25 давление"
        pos_hint: {'center_x': .6, 'center_y': .45}
        font_size: 30
'''


class MyApp(MDApp):
    reductor = False
    pr = False
    forteca = False
    pn25 = False

    def build(self):
        return Builder.load_string(KV)


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
