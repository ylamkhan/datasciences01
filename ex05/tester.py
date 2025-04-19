from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt
import signal
import sys


# Signal Handlers
def handle_sigint(sig, frame):
    print("\n\033[91mInterrupted with Ctrl+C. Exiting gracefully.\033[0m")
    sys.exit(0)


def handle_sigtstp(sig, frame):
    print("\n\033[91mStopped with Ctrl+Z (SIGTSTP).Exiting gracefully.\033[0m")
    sys.exit(0)


def main():
    try:
        signal.signal(signal.SIGINT, handle_sigint)
        signal.signal(signal.SIGTSTP, handle_sigtstp)
        array = ft_load("/home/ylamkhan/Downloads/landscape.jpg")
        print("The shape of image is: ", array.shape)
        print(array)
        img = ft_invert(array)
        plt.imshow(img)
        plt.title("invert")
        plt.axis("on")
        plt.show()
        img = ft_red(array)
        plt.imshow(img)
        plt.title("invert")
        plt.axis("on")
        plt.show()
        img = ft_green(array)
        plt.imshow(img)
        plt.title("invert")
        plt.axis("on")
        plt.show()
        img = ft_blue(array)
        plt.imshow(img)
        plt.title("invert")
        plt.axis("on")
        plt.show()
        img = ft_grey(array)
        plt.imshow(img)
        plt.title("invert")
        plt.axis("on")
        plt.show()
    except EOFError:
        print("\n\033[91mReceived EOF (Ctrl+D). Exiting.\033[0m")
        sys.exit(0)


if __name__ == "__main__":
    main()
