class CustomButton:
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            self.key = value

    def config(self, **kwargs):
        for key, value in kwargs.items():
            self.key = value

    def click(self):
        try:
            self.command()
        except:
            raise AttributeError("Кнопка не настроена")


def func():
	print('Готово')
btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
btn.click() # Кнопка не настроена
btn.config(command=func)
btn.click() # Готово