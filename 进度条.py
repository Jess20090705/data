from time import sleep

def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('[', '☆' * left, ' ' * right, ']',
          f' {percent:.0f}%\n',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)
