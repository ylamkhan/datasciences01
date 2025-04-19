from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
import signal
import sys


# Signal Handlers
def handle_sigint(sig, frame):
    print("\n\033[91mInterrupted with Ctrl+C. Exiting gracefully.\033[0m")
    sys.exit(0)


def handle_sigtstp(sig, frame):
    text = "Stopped with Ctrl+Z (SIGTSTP). Exiting gracefully."
    print(f"\n\033[91m{text}\033[0m")
    sys.exit(0)


def zoom_image(
        image: np.ndarray,
        zoom_size: int = 400, channel: int = 0) -> np.ndarray:
    """ in defuction using Zoome"""
    try:
        if image is None:
            raise AssertionError("Image is None.")
        if not isinstance(image, np.ndarray):
            raise AssertionError("Image is not a NumPy array.")
        if image.ndim != 3 or image.shape[2] != 3:
            raise AssertionError("Image does not have 3 channels.")
        if not (0 <= channel < 3):
            text = "Channel index must be 0 (Red), 1 (Green), or 2 (Blue)."
            raise AssertionError(text)

        h, w = image.shape[:2]
        start_y = max((h // 2) - (zoom_size // 2), 0)
        start_x = max((w // 2) - (zoom_size // 2), 0)
        end_y = min(start_y + zoom_size, h)
        end_x = min(start_x + zoom_size, w)

        zoomed = image[start_y:end_y, start_x:end_x, channel]
        zoomed = zoomed[..., np.newaxis]

        print("New shape after slicing:", zoomed.shape)
        print(zoomed)
        return zoomed
    except AssertionError as e:
        print("\033[91mAssertionError:\033[0m", e)
        return None


if __name__ == "__main__":
    # Register signals
    try:
        signal.signal(signal.SIGINT, handle_sigint)
        signal.signal(signal.SIGTSTP, handle_sigtstp)
        img = ft_load("/home/ylamkhan/Downloads/animal.jpeg")
        print(type(img))
        if img is not None:
            print("The shape of image is: ", img.shape)
            print(img)
            zoomed_img = zoom_image(img, zoom_size=400, channel=0)
            if zoomed_img is not None:
                plt.imshow(zoomed_img.squeeze(), cmap='gray')
                plt.title("Zoomed Red Channel")
                plt.axis("on")
                plt.show()
            gray = img.convert('L')
            print("The shape of image gray is: ", gray.shape)
            print(gray)
    except EOFError:
        print("\n\033[91mReceived EOF (Ctrl+D). Exiting.\033[0m")
        sys.exit(0)
