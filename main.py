from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from map.map import MapWindow
from admin.admin import AdminWindow
from signin.signin import SigninWindow
from till_operator.till_operator import OperatorWindow
from my_list.list import listWindow

class MainWindow(BoxLayout):

    admin_widget = AdminWindow()
    signin_widget = SigninWindow()
    operator_widget = OperatorWindow()
    Map_widget = MapWindow()
    List_widget = listWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.scrn_si.add_widget(self.signin_widget)
        self.ids.scrn_admin.add_widget(self.admin_widget)
        self.ids.scrn_op.add_widget(self.operator_widget)
        self.ids.scrn_map.add_widget(self.Map_widget)
        self.ids.scrn_list.add_widget(self.List_widget)

class MainApp(App):
    def build(self):

        return MainWindow()

if __name__=='__main__':
    MainApp().run()
    