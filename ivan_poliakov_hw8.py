"""Task 1"""
# task a
print('1.a. Создать пример со значениями True и False: ')
print(all([True, True]))
print(all([False, True]))
print(all([False, False]))
print(all([]))
# task b
print('1.b. Создать пример со значениями заменяющими True False. Любой объект в пайтон можно представить как бул объект: ')
print(any([bool([]), bool(''), bool(0)]))

"""Task 2"""
# task a
print('2.a Повторить примеры как в функции all():')
print(any([True, True]))
print(any([False, True]))
print(any([False, False]))
print(any([]))

"""Task 3"""
print('3.a Создать примеры со всеми известными вами объектами в пайтон.')
print(isinstance('Hello', str))
print(isinstance(5, int))
print(isinstance(5.5, float))
print(isinstance([5.5, 'Hi'], list))
print(isinstance({'1': '11', 1: 11}, dict))
print(isinstance((1, '22', {22}), tuple))

"""Task 4"""
# Done

"""Task 5"""
print("5. Написать функцию бутерброд внутри себя определяет другую функцию колбаса и возвращает ее объект")
def buterbrod():
    def kolbasa(x):
        return x + 1
    return kolbasa
print(buterbrod())

"""Task 6"""
# done
