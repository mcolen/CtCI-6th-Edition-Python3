"""Solution to 5.8 Draw Line.

A monochrome screen is stored as a single array of bytes, allowing eight
consecutive pixels to be stored in one byte. The screen has width `w`,
where `w` is divisible by 8 (that is, no byte will be split across
rows). The height of the screen, of course, can be derived from the
length of the aray and the width. Implement a function that draws a
horizontal line from `(x1, y)` to `(x2, y)`.

The method signature should look something like this:

drawLine(byte[] screen, int width, int x1, int x2, int y)
"""


def draw_line(screen: bytearray, width: int, x1: int, x2: int, y: int) -> None:
    """Draws a horizontal line on a monochrome screen.

    Args:
        screen: A bytearray with each bit representing a pixel.
        width: The number of bits in one "row" on the screen. Must be
            divisible by 8. That is, no byte in screen may be split
            across rows.
        x1: Beginning column of horizontal line to draw.
        x2: Ending column of horizontal line to draw (inclusive).
        y: Row in which to draw horizontal line.
    """
    left_pixel, right_pixel = y * width + x1, y * width + x2
    left_byte, right_byte = left_pixel // 8, right_pixel // 8

    left_mask = 0xFF >> left_pixel % 8
    right_mask = (0xFF >> right_pixel % 8 + 1) ^ 0xFF
    if left_byte == right_byte:
        screen[left_byte] |= left_mask & right_mask
    else:
        screen[left_byte] |= left_mask
        for i in range(left_byte + 1, right_byte):
            screen[i] = 0xFF
        screen[right_byte] |= right_mask
