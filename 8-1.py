import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Чтение данных из файла settings.txt
with open('settings.txt', 'r') as settings_file:
    sampling_frequency = float(settings_file.readline().strip())  # Частота дискретизации
    adc_quantization_step = float(settings_file.readline().strip())  # Шаг квантования АЦП

# Чтение данных из файла data.txt
adc_data = np.loadtxt('data.txt')

# Перевод показаний АЦП в Вольты, номеров отсчётов в секунды
voltage_data = adc_data * adc_quantization_step
time_data = np.arange(0, len(voltage_data)) / sampling_frequency

# Создание графика
fig, ax = plt.subplots()

# Построение зависимости напряжения от времени с настройками цвета и формы линии, размера и цвета маркеров, частоты отображений маркеров и легенды
ax.plot(time_data, voltage_data, color='green', linestyle='-', marker='o', markersize=5, markerfacecolor='green', label='V(t)', markevery=40)

# Задание максимальных и минимальных значений для шкалы
x_min, x_max = np.min(time_data), np.max(time_data)
y_min, y_max = np.min(voltage_data), 3.5
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Подписи осей
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')

# Название графика с настройками его месторасположения и переносом текста на следующую строку
title = "Зависимость напряжения от времени"
ax.set_title(title, loc='center', wrap=True)

# Наличие сетки (главной и дополнительной), настройка ее цвета и стиля
ax.grid(True, linestyle='-', color='gray', alpha=0.5)
ax.grid(True, linestyle=':', color='gray', alpha=0.5, which='minor')

# Текст с временем зарядки и разрядки
max_adc_index = np.argmax(adc_data)
charge_time = max_adc_index / sampling_frequency
discharge_time = (len(adc_data) - max_adc_index) / sampling_frequency
text = f"Зарядка: {charge_time:.2f} с\nРазрядка: {discharge_time:.2f} с"
ax.text(0.95, 0.85, text, transform=ax.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='right', bbox={'facecolor': 'white', 'alpha': 0.7})

# Вывод легенды
ax.legend()

# Настройка дополнительной сетки
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

# Настройка осей
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Сохранение графика в файл в формате .svg
plt.savefig('voltage_vs_time.svg', format='svg')

# Отображение графика
plt.show()
