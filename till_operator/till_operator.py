from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.lang import Builder
import re
from pymongo import MongoClient
from kivy.uix.floatlayout import FloatLayout # for further development using float buttons

Builder.load_file('till_operator/operator.kv')


class OperatorWindow(BoxLayout, FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        client = MongoClient()
        self.db = client.silverpos
        self.stocks = self.db.stocks

        self.cart = []
        self.qty = []
        self.total = 0.00

    def logout(self):
        self.ids.disc_inp.text = ''
        self.ids.disc_perc_inp.text = ''
        self.ids.qty_inp.text = ''
        self.ids.price_inp.text = ''
        self.ids.vat_inp.text = ''
        self.ids.total_inp.text = ''
        self.ids.code_inp.text = ''
        self.ids.cur_product.text = '' 
        self.ids.receipt_preview.text = ''
        self.cart = []
        self.qty = []
        self.total = 0.00        
        self.ids.products.clear_widgets()
        self.ids.cur_price.text = ''
        self.ids.receipt_preview.text = 'AAST RETAILER\n\nThe Collector\n123 Main St\nKnowhere, Space\n\nTel: (555)-123-456\nReceipt No: \nDate: \n\n'
        self.parent.parent.current = 'scrn_si'  
        self.parent.parent.parent\
                        .ids.scrn_list.children[0]\
                            .ids.list_preview .text = ''
        self.parent.parent.parent\
                        .ids.scrn_list.children[0]\
                            .ids.choose_item.text= 'Product List'
        self.parent.parent.parent\
                        .ids.scrn_map.children[0]\
                            .ids.scrn_mngr.current = 'full_map'
                           
    def navigate(self):
        self.parent.parent.current = 'scrn_map'
    def navigate2(self):
        self.parent.parent.current = 'scrn_list'
    def print_receipt(self):
        print('Receipt is printed') 

    def update_purchases(self):
        pcode = self.ids.code_inp.text
        products_container = self.ids.products

        target_code = self.stocks.find_one({'product_code': pcode})
        if target_code == None:
            pass
        else:
            details = BoxLayout(size_hint_y=None, height=30, pos_hint={'top': 1})
            products_container.add_widget(details)

            code = Label(text=pcode, size_hint_x=.2, color=(.06, .45, .45, 1))
            name = Label(text=target_code['product_name'], size_hint_x=.3, color=(.06, .45, .45, 1))
            qty = Label(text='1', size_hint_x=.1, color=(.06, .45, .45, 1))
            disc = Label(text='0.00', size_hint_x=.1, color=(.06, .45, .45, 1))
            price = Label(text='$'+target_code['product_price'],
                          size_hint_x=.1, color=(.06, .45, .45, 1))
            total = Label(text='0.00', size_hint_x=.2, color=(.06, .45, .45, 1))
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)

            # Update Preview
            pname = name.text
            pprice = float(price.text[1:9])
            pqty = str(1)
            self.total += pprice
            roun = 0
            roun += round(self.total,2)
            purchase_total = '`\n\nTOTAL\t\t\t\t\t\t\t\t$'+str(roun)
            self.ids.cur_product.text = pname
            self.ids.cur_price.text = '$'+str(pprice)
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]

            ptarget = -1
            for i, c in enumerate(self.cart):
                if c == pcode:
                    ptarget = i

            if ptarget >= 0:
                pqty = self.qty[ptarget]+1
                self.qty[ptarget] = pqty
                expr = '%s\t\tx\d\t' % (pname)
                rexpr = pname+'\t\tx'+str(pqty)+'\t'
                nu_text = re.sub(expr, rexpr, prev_text)
                preview.text = nu_text + purchase_total
            else:
                self.cart.append(pcode)
                self.qty.append(1)
                nu_preview = '\n'.join([prev_text, pname+'\t\tx'+pqty +
                                        '\t\t'+'$'+str(pprice), purchase_total])
                preview.text = nu_preview

            self.ids.disc_inp.text = '0.00'
            self.ids.disc_perc_inp.text = '0'
            self.ids.qty_inp.text = str(pqty)
            self.ids.price_inp.text = '$'+str(pprice)
            self.ids.vat_inp.text = '15%'
            self.ids.total_inp.text = '$'+str(pprice)
            self.ids.code_inp.text = '' 
class ImageButton(ButtonBehavior, Image):
        def on_press(self):
            pass

class Interface(BoxLayout):
    pass


 
class OperatorApp(App):
    def build(self):
        return OperatorWindow()


if __name__ == "__main__":
    oa = OperatorApp()
    oa.run()
