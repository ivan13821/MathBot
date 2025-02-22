from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class InlineKeyboardFactory:

    """ Создание inline клавиатур """




    @staticmethod 
    def create_inline_keyboard(mass: list) -> InlineKeyboardMarkup:

        """ 
        Создание inline клавиатуры из двойного списка и числа строк (Которые должны быть в итоговой клавиатуре)
        Пример списка [['hi:-)hi', 'no:-)no'], ['yes:-)yes']...] (':-)' разделяет text и call back data)

        """

        

        result = []

        for i in mass:
            res = []
            for j in i:

                text, call_back_data = j.split(':-)')

                res.append(InlineKeyboardButton(text=text, callback_data=call_back_data))
            
            result.append(res)
        
        
        return InlineKeyboardMarkup(inline_keyboard=result)
                