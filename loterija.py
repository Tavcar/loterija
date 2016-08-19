# -*- coding: utf-8 -*-
import random

print("Dobrodošli v ustvarjalcu Loto števil.")

while True:
    stevila = int(raw_input("Koliko števil želite (največ 50): "))
    print(random.sample(range(1, 51), stevila))

    ponovno = raw_input("Želite generirati nova Loto števila (da/ne)? ")

    if ponovno.lower() == "ne":
        break

print("Nasvidenje.")