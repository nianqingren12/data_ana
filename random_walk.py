from random import choice

class RandomWalk:
    '''生成一个随机游走数据的类'''
    def __init__(self,num_points = 5000):
        #所有随机游走数都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]
        self.num_points = num_points
    def fill_walk(self):
        '''计算随机游走包含的所有点'''
        #不断游走直到列表达到的指定长度
        while len(self.x_values) < self.num_points:
            #决定前进方向以及沿这个方向前进的距离
            x_dirction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_dirction * x_distance

            y_dirction = choice([1,-1])
            y_distance = choice([1,2,3,4])
            y_step = y_dirction * y_distance
            #拒绝原地踏步
            if x_step == 0 and y_step ==0:
                continue
            #计算下一个点的x坐标值与y坐标值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
        