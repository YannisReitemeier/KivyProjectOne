from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout


class FirstPage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.top_widget = TopRow()
        self.top_widget.size_hint = (1, 0.1)

        self.button_one = Button(text='Button One', size_hint=(1, 0.7))

        self.bottom_widget = BottomRow()
        self.bottom_widget.size_hint = (1, 0.2)

        self.add_widget(self.top_widget)
        self.add_widget(self.button_one)
        self.add_widget(self.bottom_widget)


class TopRow(GridLayout):
    def __init__(self):
        super().__init__()
        self.cols = 2
        self.left_label = Label(text='Left Label', size_hint=(1, 0.2))
        self.right_label = Label(text='Right Label', size_hint=(1, 0.2))

        self.add_widget(self.left_label)
        self.add_widget(self.right_label)


class BottomRow(FloatLayout):
    def __init__(self):
        super().__init__()
        self.shop_button = Button(text='Shop', size_hint=(0.2, 1), pos_hint={'center_x': 0.9, 'center_y': 0.5})
        self.shop_button.bind(on_press=self.to_shop)
        self.bottom_label = Label(text='Bottom Label', size_hint=(0.8, 1), pos_hint={'center_x': 0.4, 'center_y': 0.5})

        self.add_widget(self.shop_button)
        self.add_widget(self.bottom_label)

    def to_shop(self, item):
        myapp.screen_manager.transition = SlideTransition(direction='left')
        myapp.screen_manager.current = 'shop_screen'


class ShopPage(BoxLayout):
    def __init__(self):
        super().__init__()
        self.back_button = Button(text='Back', size_hint=(1, 0.2))
        self.back_button.bind(on_press=self.to_start)

        self.add_widget(self.back_button)

    def to_start(self, item):
        myapp.screen_manager.transition = SlideTransition(direction='right')
        myapp.screen_manager.current = 'first_screen'


class MainApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.first_page = FirstPage()
        screen_one = Screen(name='first_screen')
        screen_one.add_widget(self.first_page)
        self.screen_manager.add_widget(screen_one)

        self.shop_page = ShopPage()
        screen_shop = Screen(name='shop_screen')
        screen_shop.add_widget(self.shop_page)
        self.screen_manager.add_widget(screen_shop)

        return self.screen_manager


myapp = MainApp()
myapp.run()
