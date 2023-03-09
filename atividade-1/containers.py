a, b, c = map(int, input().split())
x, y, z = map(int, input().split())


containers_x = x // a
containers_y = y // b
containers_z = z // c

total_containers = containers_x * containers_y * containers_z

print(total_containers)

