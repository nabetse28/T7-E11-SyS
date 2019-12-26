from matplotlib import pyplot as plt


def circular_shift(n_list):
    temp = n_list.pop()
    n_list.reverse()
    n_list.append(temp)
    n_list.reverse()


text_list = [
    "0x1 + 0x1 + 0x2 + 0x1 = 0", "0x1 + 0x1 + 0x2 + 0x1 = 0",
    "0x1 + 0x1 + 0x2 + 0x1 = 0", "0x1 + 0x1 + 0x2 + 0x1 = 0",
    "0x1 + 0x1 + 0x2 + 0x1 = 0", "0x1 + 0x1 + 0x2 + 1x1 = 1",
    "0x1 + 0x1 + 1x2 + -1x1 = 1", "0x1 + 1x1 + -1x2 + 0x1 = -1",
    "1x1 + -1x1 + 0x2 + 0x1 = 0", "-1x1 + 0x1 + 0x2 + 1x1 = 0",
    "0x1 + 0x1 + 1x2 + 1x1 = 3", "0x1 + 1x1 + 1x2 + 0x1 = 3",
    "1x1 + 1x1 + 0x2 + 0x1 = 2", "1x1 + 0x1 + 0x2 + 0x1 = 1",
    "0x1 + 0x1 + 0x2 + 0x1 = 0", "0x1 + 0x1 + 0x2 + 0x1 = 0",
    "0x1 + 0x1 + 0x2 + 0x1 = 0"
]
# Funcion x[n]
x_n = [1, 2, 1, 1]
x_n1 = [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x_n2 = [1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Funcion h[n]
h_n = [0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 0, 0, 0]
h_n2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 0, 0]

# Constant List

const = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
const1 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

# X[n]
plt.figure(1)
plt.title("x[n]")
plt.xlim(-5, 20)
plt.ylim(-2, 4)
plt.grid()
plt.stem(x_n1, markerfmt='x', use_line_collection=True)
plt.get_current_fig_manager().full_screen_toggle()
plt.show()

# H[n]
plt.figure(2)
plt.title("h[n]")
plt.xlim(-3, 4)
plt.ylim(-2, 4)
plt.grid()
plt.stem(h_n, markerfmt='x', use_line_collection=True)
plt.get_current_fig_manager().full_screen_toggle()
plt.show()

# X[-n]
plt.figure(3)
plt.title("x[-n] (Reflejar la señal)")
plt.xlim(-3, 4)
plt.ylim(-2, 4)
plt.grid()
plt.stem(x_n2, markerfmt='x', use_line_collection=True)
plt.get_current_fig_manager().full_screen_toggle()
plt.show()

y_n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x_n_inv = x_n[::-1]

size_x = len(x_n)
size_h = len(h_n)

# Convolucion de y[n] = x[n] * h[n]
for i in range(0, size_h - 4):
    conv = 0
    circular_shift(x_n2)
    for j in range(0, size_x):
        conv += x_n_inv[j] * h_n[i + j]

    y_n[i] = conv

    plt.figure(1)
    plt.title("x[n] and h[n]")
    plt.xlim(-10, 9)
    plt.ylim(-2, 4)
    plt.grid()
    plt.stem(const1, x_n2, markerfmt='x', use_line_collection=True)
    plt.stem(const1,
             h_n2,
             linefmt=('g', '--'),
             markerfmt='.',
             use_line_collection=True)
    plt.text(8, 3, text_list[i], horizontalalignment='center')
    plt.get_current_fig_manager().full_screen_toggle()
    plt.show()

    plt.figure(2)
    plt.title("Convolucion: y[n] = x[n] * h[n]")
    plt.xlim(-6, 11)
    plt.ylim(-2, 4)
    plt.grid()

    plt.stem(const, y_n, use_line_collection=True)

    plt.get_current_fig_manager().full_screen_toggle()

    plt.show()