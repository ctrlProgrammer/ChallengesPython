# Calcular determinante de una matriz

# To do
# Refactorizar codigo para calcular cualquier tipo de matriz


class Matriz:

    # cofactor de una matriz
    def get_confactor(self, m, x, y):
        cof = []
        for i in range(1, len(m)):
            vec = []
            for j in range(0, len(m[i])):
                if (i != x and j != y):
                    vec.append(m[i][j])
            cof.append(vec)
        return cof

    # calcular determinante de matriz 5 x 5
    def calc_det_5_x_5(self, m):
        res = []
        total = 0
        for i in range(0, len(m)):
            cof = self.get_confactor(m, 0, i)
            a = m[0][i] * self.calc_det_4_x_4(cof)
            res.append(a)

        for i in range(0, len(res)):
            total = total + ((-1)**i) * (res[i])

        return total

    # calcular determinante de matriz 4 x 4
    def calc_det_4_x_4(self, m):
        res = []
        total = 0
        for i in range(0, len(m)):
            cof = self.get_confactor(m, 0, i)
            a = m[0][i] * self.calc_det_3_x_3(cof)
            res.append(a)

        for i in range(0, len(res)):
            total = total + ((-1)**i) * (res[i])

        return total

    # calcular determinante de matriz 3 x 3
    def calc_det_3_x_3(self, m):

        if(len(m) == 3):

            res = []
            total = 0
            for i in range(0, len(m)):
                cof = self.get_confactor(m, 0, i)
                a = m[0][i] * self.calc_det_2_x_2(cof)
                res.append(a)

            for i in range(0, len(res)):
                total = total + ((-1)**i) * (res[i])

            return total

        else:
            print('Tu matriz no es 3 x 3')

    # Calcular determinante de una matriz 2 x 2
    def calc_det_2_x_2(self, m):
        if(len(m) == 2):
            return (m[0][0]*m[1][1] - m[0][1]*m[1][0])
        else:
            print('Tu matriz no es 2 x 2')


# Matriz establecida
# 4x4
m_1 = [[5, 3, 1, 0], [-1, 2, 5, -2], [3, -1, -2, 0], [-5, 0, -3, 1]]
m_2 = [[4, 7, -2, 0], [3, -5, 1, 3], [-8, 6, 9, 8], [3, -5, 3, 5]]
# 3x3
m_3 = [[2, -3, 5], [1, 0, 4], [3, -3, 9]]
m_4 = [[4, 7, -2], [3, -5, 1], [-8, 6, 9]]
# 2x2
m_5 = [[2, -3], [1, 0]]
m_6 = [[4, -8], [3, 5]]
# 5x5
m_7 = [[5, 3, 1, 0, 4], [8, -1, 2, 5, -2], [9, 3, -1, -2, 0],
       [-5, -5, 0, -3, 1], [-9, -8, 6, -3, 1]]
m_8 = [[4, 7, -2, 0, 9], [6, 3, -5, 1, 3],
       [6, -8, 6, 9, 8], [-5, 3, -5, 3, 5], [-6, -3, 4, -3, 3]]

mat = Matriz()

print(mat.calc_det_3_x_3(m_4))
