import colorgram

rgb_color = []
colors = colorgram.extract('image.jpg',25)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_color.append(new_color)

# print(rgb_color)

color_list = [(189, 164, 21), (199, 171, 123), (145, 75, 39), (17, 40, 87), (130, 83, 96), (13, 60, 34), (126, 25, 20), (21, 97, 141), (182, 143, 150), (5, 97, 13), (90, 119, 85), (86, 19, 48), (35, 39, 116), (154, 204, 219), (145, 178, 195), (217, 202, 140), (147, 172, 148), (100, 17, 14), (3, 78, 120), (116, 23, 38), (103, 144, 105)]
