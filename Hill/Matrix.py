class Matrix:
    """This class implements mathematical matrix and enough functions to
    use this matrix to implement Hill cipher
    """
    def __init__(self, rows, columns):

        self.matrix = []
        self.rows = rows
        self.columns = columns
        for i in range(rows):
            self.matrix.append(list())
            for j in range(columns):
                self.matrix[i].append(0)

    # Перегрузка индексации
    def __getitem__(self, key):
        return self.matrix[key]

    # Заполнение матрицы
    def fillMatrix(self):
        print("This matrix has size {0}x{1}".format(self.rows, self.columns))
        for i in range(self.rows):
            row = list(map(int, input().strip().split(" ")))
            self.matrix[i] = row
        
    # Вывод матрицы на экран
    def printMatrix(self):
        for i in range(self.rows):
            row = list(map(str, self.matrix[i]))
            print(" ".join(row))

    # Транспониование матрицы
    def transp(self):
        T = self
        for i in range(self.rows):
            for j in range(i, self.columns):
                temp = T.matrix[i][j]
                T.matrix[i][j] = T.matrix[j][i]
                T.matrix[j][i] = temp
        return T

    # Перегрузка оператора *
    def __mul__(self, other):
        if type(other) == type(self):
            T = Matrix(self.rows, self.columns)
            if self.columns != other.rows:
                return None
            for i in range(self.rows):
                for j in range(self.columns):
                    for k in range(self.columns):
                        T[i][j] = T[i][j] + self.matrix[i][k] * other.matrix[k][j]
        else:
            T = Matrix(self.rows, self.columns)
            for i in range(T.rows):
                for j in range(T.columns):
                    T[i][j] = self.matrix[i][j] * other
        return T
    
    # Функция для поиска минора матрицы
    # Принимает в качестве аргумента индексы элемента по которому строится минор
    def minor(self, a, b):
        m = Matrix(self.rows-1, self.columns-1)
        j = 0
        for q in range(m.columns):
            i = 0
            for p in range(m.rows):
                if (i == a):
                    i += 1
                if (j == b):
                    j += 1
                m.matrix[p][q] = self.matrix[i][j]
                i += 1
            j += 1
        return m
    
    # Функция поиска детерминанта любой матрицы
    def determinant(self):
        det = 0
        if self.rows == 1:
            return self.matrix[0][0]
        if self.rows == 2:
            return self.determinant2x2()
        for n in range(self.columns):
            if n % 2 == 0:
                sign = 1
            else:
                sign = -1
            det = det + sign*self.matrix[0][n] * self.minor(0, n).determinant()
        return det
    
    # Функция поиска детерминанта матрицы 2х2
    def determinant2x2(self):
        det = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        return det
    
    # Перегрузка оператора %
    def __mod__(self, other):
        T = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                T.matrix[i][j] = self.matrix[i][j] % other
        return T

    # Функция поиска матрицы алгебраических дополнений
    def algebDop(self):
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                A = self.matrix[i][j]
                minor = self.minor(i, j)
                A = (-1)**(i+1 + j + 1) * minor.determinant()
                result.matrix[i][j] = A
        return result