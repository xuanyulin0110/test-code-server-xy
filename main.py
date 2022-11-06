import random

def point_address(a,b):
    return (a - 1) * 21 + 4 * b - 4
ooxx = '  |   |   \n--+---+--\n  |   |   \n--+---+--\n  |   |   '
print(ooxx)
while 1:
    textinput = input('請輸入')
    if len(textinput) == 9:
        if textinput[0:3] == 'put':
            if textinput[4] == 'o':
                x = int(textinput[6])
                y = int(textinput[8])
                if x > 0 and x <= 3 and y > 0 and y <= 3:
                    if ooxx[point_address(x,y)] == 'o' or ooxx[point_address(x,y)] == 'x':
                        break
                    ooxx = ooxx[0:point_address(x,y)] + 'o' + ooxx[point_address(x,y)+1:]


                print(ooxx)
                print('*'*10)
                x_ = random.randint(1,3)
                y_ = random.randint(1,3)
                while ooxx[point_address(x_,y_)] == 'o' or ooxx[point_address(x_,y_)] == 'x':
                    x_ = random.randint(1, 3)
                    y_ = random.randint(1, 3)


                if ooxx[point_address(x,y)] == ooxx[point_address(x,y+1)] and ooxx[point_address(x,y+2)] != 'x':
                    x_ = x
                    y_ = y + 2



                ooxx = ooxx[0:point_address(x_, y_)] + 'x' + ooxx[point_address(x_, y_) + 1:]
                print(ooxx)
