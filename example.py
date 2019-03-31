import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

import stem

def main():
    n = 20
    Ts = 0.1

    t = np.arange(n)*Ts
    y = np.sin(2*pi*t)+2

    fig, ax = plt.subplots()

    stem(y, baseline=0, ax=ax)
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Magnitude')

    plt.show()

if __name__ == '__main__':
    main()
