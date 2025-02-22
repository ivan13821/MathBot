from keyboard_factory.keyboard_factory_main import KeyBoardFactory



class ExampleKeyboard:


    @staticmethod
    def start_keyboard():
        return KeyBoardFactory.create_reply_keyboard([
            ['Тренировка', 'Мой уровень']
        ])



    @staticmethod
    def training():
        return KeyBoardFactory.create_inline_keyboard([
            ['Сложение:-)tr_plus', 'Вычитание:-)tr_minus'],
            ['Умножение:-)tr_multi', 'Деление:-)tr_division']
        ])



    @staticmethod
    def stop():
        return KeyBoardFactory.create_reply_keyboard([
            ['Закончить']
        ])

