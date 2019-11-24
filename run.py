import reader as rder
from PIL import Image
import numpy as np

ip, out_mode, length_required, sampleID = np.repeat(-1, 4)
e1, e2, e3, e4 = np.repeat(0, 4)

print('-'*40)


while sampleID not in range(1,52):
    if e4 != 0:
        print("Unknown command, plz retype the selection mode\n")
    sampleID = int(input('Enter the number of sampleID: 1~51\nInput here: '))
    e4 += 1

PILimg = Image.open('./dendrites/' +
                    str(sampleID) + '.tif')
im2arr = rder.PIL2ary(PILimg)

while ip not in range(0,3):
    if e1 != 0:
        print("Unknown command, plz retype the selection mode\n")
    ip = int(input('Choose "1" for random selection,'
                   ' "2" for determistic selection\nInput here: '))
    if ip == 2:
        loc = input("type in location in format *(y, x, dir)*\n"
                    " dir :\n   0 : by row \n   1 : by column\nInput here: ").split(',')
        loc_new = tuple([int(x) for x in loc])
        while rder.out_bound_check(im2arr, loc_new):
            loc = input("type in location in format *(y, x, dir)*\n"
                        " dir :\n   0 : by row \n   1 : by column\n"
                        "Input here: ").split(',')
            loc_new = tuple([int(x) for x in loc])
    else:
        loc_new = None
    e1 += 1

while out_mode not in range(0,4):
    if e2 != 0:
        print("Unknown command, plz retype the selection mode\n")
    out_mode = int(input('Select the output format\n   0'
                     '  :  Binary\n   1  :  Decimal\n   2'
                     '  ： Hexdecimal\n   3  :  Character\nInput here: '))
    e2 += 1

while length_required not in range(1,65):
    if e3 != 0:
        print("Unknown command, plz retype the selection mode\n")
    length_required = int(input('Enter the number of characters: 1~64\nInput here: '))
    e3 += 1

sel_vec = rder.rand_sel(loc=loc_new, im2arr=im2arr)
hashbject = rder.hash(sel_vec)
print(rder.conversion(out_mode=out_mode,
                      hash_object=hashbject,
                      length_required=length_required))

print('-'*40)
