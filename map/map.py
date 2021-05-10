import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('map/Map_1.kv')

class MapWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def go_back(self):
        self.parent.parent.current = 'scrn_op'
           

    def change_screen(self, instance):
        if instance.text == 'Full Map':
            self.ids.scrn_mngr.current = 'full_map'
        elif instance.text == 'Go to Luggage':
            self.ids.scrn_mngr.current = 'luggage_map'
        elif instance.text == 'Go to Automotive':
            self.ids.scrn_mngr.current = 'automotive_map'
        elif instance.text == 'Go to Housewares':
            self.ids.scrn_mngr.current = 'housewares_map'
        elif instance.text == 'Go to Infants':
            self.ids.scrn_mngr.current = 'infants_map'            
        elif instance.text == 'Go to Home storage':
            self.ids.scrn_mngr.current = 'home_storage_map'
        elif instance.text == 'Go to Seasonal':
            self.ids.scrn_mngr.current = 'seasonal_map'
        elif instance.text == 'Go to Boys section':
            self.ids.scrn_mngr.current = 'boys_section_map'
        elif instance.text == 'Go to Home Floral':
            self.ids.scrn_mngr.current = 'home_floral_map'
        elif instance.text == 'Go to Pet supplies':
            self.ids.scrn_mngr.current = 'Pet_supplies_map'
        elif instance.text == 'Go to Music and Movies section':
            self.ids.scrn_mngr.current = 'music_movies_map'
        else:
            self.ids.scrn_mngr.current = 'intimate_apparel_map'
class MapApp(App):
    def build(self):
        return MapWindow()

if __name__=='__main__':
    sa = MapApp()
    sa.run()


    