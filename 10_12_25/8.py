i = 10
F = 30000
t = 150
V = i * F * t * 2
S = 140000
t_per = (V / S) * 12
V2 = 1 * (F / 1.5) * (i / 5) * (t / 3)
t_per2 = (V2 / S) * 12
print((t_per - t_per2) // 3600)