from keyboard_factory.reply_keyboard_factory import ReplyKeyboardFactory
from keyboard_factory.inline_keyboard_factory import InlineKeyboardFactory




class KeyBoardFactory:


    """ Создает все кнопки, какие вашей душе угодно)))"""


    @staticmethod 
    def create_inline_keyboard(mass: list):

        """ Создает inline кнопку с call_bcak_data """

        return InlineKeyboardFactory.create_inline_keyboard(mass=mass)
    



    @staticmethod
    def create_reply_keyboard(mass: list):

        """ Создает reply кдавиатуру """

        return ReplyKeyboardFactory.create_reply_keyboard(mass=mass)