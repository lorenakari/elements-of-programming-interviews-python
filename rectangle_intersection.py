from collections import namedtuple

Rect = namedtuple("Rect", ["x", "y", "width", "height"])


def check_intersection(Rect_1: Rect, Rect_2: Rect) -> Rect | None:
    """Check if two rectangles whose sides are parallel to the X-axis and Y-axis
    have a nonempty intersection. If the intersection is nonempty, return the
    rectangle formed by their intersection."""
    x1, x2 = Rect_1.x, Rect_2.x
    min_x = min(x1, x2)
    if min_x == x1:
        if x2 <= min_x + Rect_1.width:
            x_intersect = x2
            width_intersect = min_x + Rect_1.width - x2
        else:
            return None
    else:
        if x1 <= min_x + Rect_2.width:
            x_intersect = x1
            width_intersect = min_x + Rect_2.width - x1
        else:
            return None

    y1, y2 = Rect_1.y, Rect_2.y
    min_y = min(y1, y2)
    if min_y == y1:
        if y2 <= min_y + Rect_1.height:
            y_intersect = y2
            height_intersect = min_y + Rect_1.height - y2
        else:
            return None
    else:
        if y1 <= min_y + Rect_2.height:
            y_intersect = y1
            height_intersect = min_y + Rect_2.height - y1
        else:
            return None

    return Rect(x_intersect, y_intersect, width_intersect, height_intersect)


if __name__ == "__main__":
    Rect1 = Rect(1, 1, 2, 2)
    Rect2 = Rect(2, 2, 2, 2)
    intersection = check_intersection(Rect1, Rect2)
    if intersection:
        print(intersection)
