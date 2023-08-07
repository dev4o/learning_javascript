lg_width = int(input())
lg_height = int(input())
sm_widht = int(input())
sm_height = int(input())

horizontal = lg_width // sm_widht
vertical = lg_height // sm_height

pieces = horizontal * vertical
print(pieces)
print(vertical)
