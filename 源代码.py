print('欢迎使用工具箱，请输入执行选项，然后按回车键。')
while True:
    select = int(input('\n输入选项以继续，输入其他数字以返回\n1.求解数学问题\n2.关于\n\n选项：'))
    if select == 1:
        while True:
            select_in_1 = int(input('\n输入选项以继续，输入其他数字以返回\n1.鸡兔同笼\n2.解方程\n3.素数\n\n选项：'))
            if select_in_1 == 1:
                while True:
                    x = int(input('\n头的个数:'))
                    y = int(input('脚的个数:'))
                    # x=鸡+兔
                    # y=2鸡+4兔
                    鸡 = 2 * x - y / 2
                    兔 = y / 2 - x
                    if 鸡 % 1 == 0 and 兔 % 1 == 0 and 鸡 >= 0 and 兔 >= 0:
                        鸡 = int(鸡)
                        兔 = int(兔)
                        print('\n鸡的个数:', 鸡, '兔的个数:', 兔)
                    else:
                        print('\n无解')
                    if_continue = int(input('\n执行完毕，输入1以继续，输入其他数字以返回\n'))
                    if if_continue == 1:
                        pass
                    else:
                        break
            elif select_in_1 == 2:
                while True:
                    print('\n方程为ax^2+bx+c=0 请在下面输入相关数据后回车')
                    a = float(input('a='))
                    if a == 0:
                        b = float(input('b='))
                        if b == 0:
                            c = float(input('c='))
                            if c == 0:
                                print('成立')
                            else:
                                print('不成立')
                        else:
                            c = float(input('c='))
                            print('x=', -c / b)
                    else:
                        b = float(input('b='))
                        c = float(input('c='))
                        if b ** 2 == 4 * a * c:
                            print('x1=x2=', -b / 2 / a)
                        else:
                            print('x1=', -b / 2 * a + (b ** 2 - 4 * a * c) ** 0.5 / (2 * a))
                            print('x2=', -b / 2 * a - (b ** 2 - 4 * a * c) ** 0.5 / (2 * a))
                    if_continue = int(input('\n执行完毕，输入1以继续，输入其他数字以返回\n'))
                    if if_continue == 1:
                        pass
                    else:
                        break
            elif select_in_1 == 3:
                while True:
                    a = 0
                    first_number = int(input('\n请输入要判断的第一个数字：'))
                    last_number = int(input('请输入要判断的最后一个数字：'))
                    if 2 <= first_number <= last_number:
                        for number in range(first_number, last_number + 1):
                            for divide in range(2, number):
                                if number % divide != 0:
                                    pass
                                else:
                                    a += 1
                                    break
                            if a == 0:
                                print(number)
                            else:
                                pass
                            a = 0
                    else:
                        print('请输入正确的数字。')
                    if_continue = int(input('\n执行完毕，输入1以继续，输入其他数字以返回\n'))
                    if if_continue == 1:
                        pass
                    else:
                        break
            else:
                break
    elif select == 2:
        print('\n版本：1.0')
    else:
        print('\n感谢使用，请按回车键退出')
        input()
        break

