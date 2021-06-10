# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    _lenght = 0
    _width = 0
    def __init__(self,length_data, width_data):
        Road._lenght = length_data
        Road._width = width_data


    def Asfalt_mass(self):
        result = Road._width * Road._lenght * 25 * 5
        return result

some_road = Road(5000,20)
print(f'Масса асфальта для покрытия дороги - {some_road.Asfalt_mass()} кг')

