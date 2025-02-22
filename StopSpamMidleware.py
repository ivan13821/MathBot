from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

import time



#Словарь со временем отправки последнего сообщения 
timer = {}



# Это будет outer-мидлварь на любые колбэки
class StopSpamMiddleware(BaseMiddleware):

    """ Класс который останавливает спам """
    
    
    
    
    
    def not_flud(self, event) -> bool:

        """ Функция для отслеживания спама """

        # Проверяем посылал ли бот сообщение боту если нет то пропускаем его
        try:
            time_last_send = timer[event.from_user.id]
        except KeyError:
            timer[event.from_user.id] = time.time()
            return True
        

        #проверяем прошлал и одна секунда после того как пользователь отправил последнее сообщение 
        if time.time() - time_last_send > 0.5:
            timer[event.from_user.id] = time.time()
            return True
        
        else:
            return False
        

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        
        #если пользователь отправлял запрос раньше чем через 1 сек после отправки сообщения то дропаем его (на след. шаге)
        if self.not_flud(event):
            return await handler(event, data)
            

            
        #здесь )))
        await event.answer(
            "Вы отправляете слишком много запросов",
            show_alert=True
        )