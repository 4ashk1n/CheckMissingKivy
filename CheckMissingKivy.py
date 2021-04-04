from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')
Window.size = (400,800)

Builder.load_file('CM.kv')

sm = ScreenManager()

students = []

missing = []

misslist = 'Все на месте!'

class PeopleScreen(Screen):
    def fill(self):
        global students
        id = 0
        for std in students:
            self.people.add_widget(
                ToggleButton(
                    text=std,
                    on_press=lambda: self.addmiss(id),
                    on_release=lambda: self.remmiss(id)
                )
            )
            id+=1

    def checkmissing(self):
        global misslist
        for wd in self.children[0].children[0].children:
            if wd.state == 'normal':
                missing.append(wd.text)
            missing.sort()
            try:
                missing.remove('Кого нет?')
            except:
                pass
            if len(missing)!=0:
                misslist = ''
            for std in missing:
                misslist+=std+'\n'

        self.children[0].clear_widgets()
        # self.children[0].children[1].children[0].text = 'Отсутствующие бойцы'
        # print(self.ids)
        # self.lbl.text = 'Отсутствующие бойцы'
        self.children[0].add_widget(
            TextInput(
                text=misslist,
            )
        )

class PeopleButton(ToggleButton):
    pass


class GroupScreen(Screen):
    def groupAll(self, instance):
        global students
        students = ["Алексей Зубков", "Али Закиров", "Альберт Гусейнов",
                    "Андрей Артемов", "Андрей Демьянюк", "Андрей Стец",
                    "Андрей Швецов", "Артем Фоломеев", "Василий Чирвинский",
                    "Денис Густомясов", "Дмитрий Лемешев",
                    "Дмитрий Щагин", "Евгения Елистратова", "Елена Никуленко",
                    "Елизавета Тимофеева", "Захар Куликов",
                    "Кристина Столярова", "Максим Бычков", "Мария Никитина",
                    "Михаил Захаров", "Олег Леоненко",
                    "Павел Брусиловский", "Сергей Осипов", "Федор Царев"]
        # print(len(self.students)) 24
        PeopleScreen().fill()
    def group1(self, instance):
        global students
        students = ["Алексей Зубков", "Андрей Артемов", "Дмитрий Щагин",
                    "Евгения Елистратова", "Елена Никуленко", "Елизавета Тимофеева",
                    "Кристина Столярова", "Максим Бычков",
                    "Мария Никитина", "Михаил Захаров",
                    "Олег Леоненко", "Сергей Осипов",
                    "Федор Царев"]
        # print(len(self.students)) 13
        PeopleScreen().fill()
    def group2(self, instance):
        global students
        students = ["Али Закиров", "Альберт Гусейнов", "Андрей Демьянюк",
                    "Андрей Стец", "Андрей Швецов", "Артем Фоломеев",
                    "Василий Чирвинский", "Денис Густомясов", "Дмитрий Лемешев",
                    "Захар Куликов", "Павел Брусиловский"]
        # print(len(self.students)) 11
        PeopleScreen().fill()

class GroupAllScreen(PeopleScreen):
    pass
class Group1Screen(PeopleScreen):
    pass
class Group2Screen(PeopleScreen):
    pass

class CMApp(App):
    def build(self):
        sm.add_widget(GroupScreen(name='group'))
        sm.add_widget(GroupAllScreen(name='all'))
        sm.add_widget(Group1Screen(name='first'))
        sm.add_widget(Group2Screen(name='second'))

        return sm





if __name__ == "__main__":
    CMApp().run()