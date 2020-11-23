default = int(input('Enter value in seconds'))
hh = default // 3600
mm = default % 3600 // 60
ss = default % 3600 % 60
if hh < 10:
    h = f'0{hh}'
else:
    h = hh
if mm < 10:
    m = f'0{hh}'
else:
    m = mm
if ss < 10:
    s = f'0{hh}'
else:
    s = ss
print(f'{h}:{m}:{s}.')
