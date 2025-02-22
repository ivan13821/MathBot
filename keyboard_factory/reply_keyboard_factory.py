from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



class ReplyKeyboardFactory:

    """ Создание reply клавиатур"""




    @staticmethod
    def create_reply_keyboard(mass: list) -> ReplyKeyboardMarkup:

        """ Создание reply клавиатуры из двойного списка """

        result = []

        for i in mass:
            res = []
            for j in i:

                res.append(KeyboardButton(text=j))
            
            result.append(res)

        
        return ReplyKeyboardMarkup(keyboard=result, resize_keyboard=True)
        
        
        


