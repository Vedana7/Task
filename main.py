import numpy as np  # импортируем библиотеку numpy для работы с массивами
import matplotlib.pyplot as plt  # импортируем библиотеку matplotlib для построения графиков
from mpl_toolkits.mplot3d import Axes3D  # импортируем 3д инструменты из matplotlib

#создаем параметры для цилиндра
z = np.linspace(-1, 1, 100)  # создаем 100 точек по оси Z от -1 до 1
theta = np.linspace(0, 2 * np.pi, 100)  # создаем 100 точек угла от 0 до 2π
theta_grid, z_grid = np.meshgrid(theta, z)  # создаем сетку углов и Z

# вычисляем координаты X и Y для цилиндра
x_grid = np.cos(theta_grid)  # координаты X
y_grid = np.sin(theta_grid)  # координаты Y

# создаем фигуру и 3D оси
fig = plt.figure(figsize=(10, 7))  # задаем размер графика
ax = fig.add_subplot(111, projection='3d')  # добавляем 3D оси

# строим 3D цилиндр
ax.plot_surface(x_grid, y_grid, z_grid, color='cyan', alpha=0.7)  # alpha - прозрачность

# добавляем заголовок и подписи к осям
ax.set_title('3D Cylinder', fontsize=16)  # заголовок графика
ax.set_xlabel('X Axis', fontsize=14)  # подпись оси X
ax.set_ylabel('Y Axis', fontsize=14)  # подпись оси Y
ax.set_zlabel('Z Axis', fontsize=14)  # подпись оси Z

#устанавливаем равные масштабы для всех осей
ax.set_box_aspect([1, 1, 2])  #устанавливаем соотношение сторон

plt.show()  # отобраажем график