import math


def center_point_calc(x1,y1,x2,y2):

    return [math.sqrt(x1**2+y1**2),math.sqrt(x2**2+y2**2)]

point_x1 = float(input())
point_y1 = float(input())
point_x2 = float(input())
point_y2 = float(input())

calc_1,calc_2 = center_point_calc((point_x1),(point_y1),(point_x2),(point_y2))

if calc_1 <= calc_2:
    print(f"({int(point_x1)}, {int(point_y1)})")
else:
    print(f"({int(point_x2)}, {int(point_y2)})")