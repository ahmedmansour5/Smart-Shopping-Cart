import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from collections import OrderedDict
from pymongo import MongoClient


Builder.load_file('my_list/list_1.kv')

class listWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        client = MongoClient()
        db = client.silverpos
        self.users = db.users
        self.products = db.stocks

        product_code = []
        product_name = []
        spinvals = []
        for product in self.products.find():
            product_code.append(product['product_code'])
            name = product['product_name']
            if len(name) > 30:
                name = name[:30] + '...'
            product_name.append(name)
        for x in range(len(product_code)):
            spinvals.append(product_name[x])
        self.ids.choose_item.values = spinvals

    def go_backk(self):
        self.parent.parent.current = 'scrn_op'
    
    def remove_list(self):
        self.ids.list_preview.text = ''
    
    def add_fav(self):
        pass
    
    def preview_fav(self):
        self.ids.list_preview.text = '* Purity Fruity Custard\n\n* Nestle Cerelac Wheat\n\n* Mamas Peanut Butter\n\n* Blueland M/Flat Spread\n\n* Sun Mixed Fruit Jam\n\n* Top Chef Jasmine Rice\n_'

    def add_list(self):
        choose_item = self.ids.choose_item.text
        preview = self.ids.list_preview
        prev_text = preview.text   
        _prev = prev_text.find('_')
        if _prev > 0:
            prev_text = prev_text[:_prev]
        purchase_total = '_'
        if choose_item == 'Product List':
            pass
        else:
            nu_preview = '\n'.join([prev_text,'*  '+choose_item,purchase_total])
            
            preview.text = nu_preview

                               
class listApp(App):
    def build(self):
        return listWindow()

if __name__=='__main__':
    sa = listApp()
    sa.run()


    