time_as_seconds = int(input())

hours = time_as_seconds // 3600
minutes = (time_as_seconds - hours * 3600) // 60
seconds = time_as_seconds - hours * 3600 - minutes * 60

print(f'{hours}:{minutes}:{seconds}')
