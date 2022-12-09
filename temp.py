class CustomButton:
    def __init__(self, text, **kwargs):
        self.text = text
        for args in kwargs.items():
            print(args[0], args[1])

btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa', test="abcd", temp=None)