import math

def annuittyPayment():
    unknown = int(input('\nВыберите неизвестную величину\n1 - Сумма кредита\n2 - Процентная ставка\n3 - Срок выплаты кредита\n4 - Платежи по кредиту\n5 - Вернуться в главное меню\n'))
    if unknown == 1:
        summCredit()
    elif unknown == 2:
        percent()
    #elif unknown == 3:
        #paymentTerm()
    elif unknown == 4:
        tranche()
    elif unknown == 5:
        main()
    else:
        print('Ошибка ввода! Повторите попытку.')
        annuittyPayment()

def summCredit():
    percent = float(input('\nПроцентная ставка: '))
    payment_term = int(input('Срок выплаты кредита: '))
    tranche = float(input('Транши по кредиту: '))

    if percent > 0 and payment_term > 0 and tranche > 0:
        summ_percent = 1
        for n in range(1, payment_term):
            summ_percent += (percent / 100 + 1) ** n

        summ_credit = round((tranche * summ_percent) / (percent / 100 + 1) ** payment_term, 2)
    
        print('Сумма кредита: ', summ_credit, 'рублей')

        choice = int(input('\nВыберите\n1 - Снова решить подобную задачу задачу с этой неизвестной\n2 - Решить задачу на аннуитетный платеж с другой неизвестной\n3 - Выход в главное меню\n'))
        if choice == 1:
            summCredit()
        elif choice == 2:
            annuittyPayment()
        elif choice == 3:
            main()
        else:
            print('Ошибка ввода! Повторите попытку.')            
    else:
        print('Ошибка ввода! Вводите положительные числа.')

def percent():
    print('Берут кредит на 2 года(месяца)')
    summ_credit = float(input('\nСумма кредита: '))    
    tranche1 = float(input('Введите первый платеж: '))
    tranche2 = float(input('Введите второй платеж: '))

    if summ_credit > 0 and tranche1 > 0 and tranche2 > 0:
        tranche1 *= -1
        tranche2 *= -1
            
        d = tranche1 ** 2 - 4 * summ_credit * tranche2
        if d < 0:
          print('Корней нет')
        elif d == 0:
          x = (-tranche1) / (2 * summ_credit)
          res = round((x - 1) * 100, 2)
          print('Процентная ставка: ', res, '%')
        else:
          x1 = (-tranche1 + math.sqrt(d)) / (2 * summ_credit)
          x2 = (-tranche1 - math.sqrt(d)) / (2 * summ_credit)
          res = round((x1 - 1) * 100, 2)
          print('Процентная ставка: ', res, '%')

        choice = int(input('\nВыберите\n1 - Снова решить подобную задачу задачу с этой неизвестной\n2 - Решить задачу на аннуитетный платеж с другой неизвестной\n3 - Выход в главное меню\n'))
        if choice == 1:
            percent()
        elif choice == 2:
            annuittyPayment()
        elif choice == 3:
            main()
        else:
            print('Ошибка ввода! Повторите попытку.') 
            
    else:
        print('Ошибка ввода! Вводите положительные числа.')

def tranche():
    summ_credit = float(input('\nСумма кредита: ')) 
    percent = float(input('Процентная ставка: '))
    payment_term = int(input('Срок выплаты кредита: '))

    if summ_credit > 0 and percent > 0 and payment_term > 0:
        tranche = (summ_credit * (1 + percent / 100) ** payment_term * (percent / 100)) / ((1 + percent / 100) ** payment_term - 1)
        print('Платеж по кредиту:', round(tranche,2))

        choice = int(input('\nВыберите\n1 - Снова решить подобную задачу задачу с этой неизвестной\n2 - Решить задачу на аннуитетный платеж с другой неизвестной\n3 - Выход в главное меню\n'))
        if choice == 1:
            tranche()
        elif choice == 2:
            annuittyPayment()
        elif choice == 3:
            main()
        else:
            print('Ошибка ввода! Повторите попытку.')
    else:
        print('Ошибка ввода! Вводите положительные числа.')

def main():
    choice = int(input('Выберите \n1 - Аннуитетный платеж \n2 - Дифференцированный платеж \n'))
    if choice == 1:
        annuittyPayment()
    #elif choice == 2:
        #differentiatedPayment()
    else:
        print('Ошибка ввода! Повторите попытку.')
        main()

main()