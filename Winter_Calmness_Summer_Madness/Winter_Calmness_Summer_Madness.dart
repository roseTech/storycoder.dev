/*  Documentation: Bus: Every three minutes, starting with 2 people, every 15 min + 12 people
12.00: 2p     12.15: 14p      12.30: 26p
12.03: 2p     12.18: 14p      12.33: 26p
12.06: 2p     12.21: 14p      ...
12.09: 2p     12.24: 14p
12.12: 2p     12.27: 14p

Cars: Every min 1p, every 6th minute 5p
12.00: 1p     12.07: 1p       12.13: 1p
12.01: 1p     12.08: 1p       12.14: 1p
12.02: 1p     12.09: 1p       ...
12.03: 1p     12.10: 1p
12.04: 1p     12.11: 1p
12.05: 1p     12.12: 5p
12.06: 5p

Walkers: Every min + 1 walker until 11th min, then restart cycle
12.00: 1p     12.11: 1p
12.01: 2p     12.12: 2p
12.02: 3p     12.13: 3p
12.03: 4p     12.14: 4p 
12.04: 5p     ...
12.05: 6p
12.06: 7p
12.07: 8p
12.08: 9p
12.09: 10p
12.10: 11p

Time: 12.00 till 18.00 = 6 hours 
Print: Total amount of p*/
