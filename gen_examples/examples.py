from random import choice




class Examples:


    @staticmethod
    def plus(level: int):

        num1, num2 = choice(list(range(round((level+1)**1.5)))), choice(list(range(round((level+1)**1.5))))

        example = f'{num1} + {num2} = ?'

        answer = str(num1 + num2)

        return (example, answer)


    @staticmethod
    def minus(level: int):


        num1, num2 = choice(list(range(round((level + 1) ** 1.5)))), choice(list(range(round((level + 1) ** 1.5))))

        if num1 < num2:
            num1, num2 = num2, num1

        example = f'{num1} - {num2} = ?'

        answer = str(num1 - num2)

        return (example, answer)



    @staticmethod
    def multi(level: int):

        num1, num2 = choice(range(level//5+1, level//5+2)), choice(range(10))

        example = f'{num1} * {num2} = ?'

        answer = str(num1 * num2)

        return (example, answer)



    @staticmethod
    def division(level: int):

        num1, num2 = choice(range(1, level // 5 + 2)), choice(range(1, 10))

        result = num1 * num2

        num = choice([num1, num2])

        example = f'{result} : {num} = ?'

        answer = str(result//num)

        return (example, answer)
