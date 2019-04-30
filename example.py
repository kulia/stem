import matplotlib.pyplot as plt
import stem
import os

def main():
    y = [
        2.,         2.58778525, 2.95105652, 2.95105652, 2.58778525, 2.,
        1.41221475, 1.04894348, 1.04894348, 1.41221475, 2.,         2.58778525,
        2.95105652, 2.95105652, 2.58778525, 2.,         1.41221475, 1.04894348,
        1.04894348, 1.41221475]

    fig, ax = plt.subplots()

    ax.plot(y, '--k', label='continous')
    stem(y, baseline=0, ax=ax, label='stem')

    ax.legend()

    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Magnitude')

    fig_path = './fig/'
    if not os.path.isdir(fig_path):
        os.mkdir(fig_path)

    fig.savefig(fig_path+'example.png', dpi=360, transparent=True)

    plt.show()

if __name__ == '__main__':
    main()
