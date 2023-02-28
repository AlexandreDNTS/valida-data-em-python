def DataValida(data):
    dia,mes,ano = map(int,data.split('/'))

    if mes <=0 or mes > 31 and ano <=0:
        return False
    if mes in (1,3,5,7,8,10,12):
        UltimoDia = 31
    elif mes == 2:
        if ano%4 == 0 and ano % 100 != 0 or ano % 400 ==0:
            UltimoDia = 29
        else:
            UltimoDia = 28
    else:
        UltimoDia = 30
    
    if dia <=0 or dia > UltimoDia:
        return False
    return True

d = input('data: ')
dv = DataValida(d)
if dv == True:
    print('data valida')
else:
    print('data invalida')