from sys import argv
name, hours, wrate, prem = argv
hours = int(hours)
wrate = int(wrate)
prem = int(prem)
print(argv)
print(hours * wrate + prem)
