import numpy as np
from Crypto.Hash import SHA512
from itertools import chain

def PIL2ary(PILimg):
    return(np.array(PILimg))

def rand_sel(read_len_pixel=10, loc=None, im2arr=None):
    print('-'*40)
    print('**Random selecting**')
    h,w,c = im2arr.shape
    if loc == None:
        temp_a = int(np.random.randint(h, size=1))
        temp_b = int(np.random.randint(w, size=1))
        dir_sel = int(np.random.randint(2,size=1))
    else:
        temp_a, temp_b, dir_sel = loc

    if dir_sel == 0:
        if temp_b < w-read_len_pixel:
            sel_vec = np.mean(im2arr[temp_a, temp_b:temp_b+read_len_pixel,:], axis=1)
        else:
            sub = read_len_pixel - w + temp_b
            sel_vec = np.mean(im2arr[temp_a, temp_b:,:], axis=1)
            if temp_a < h - 1:
                sel_vec = np.concatenate([sel_vec, np.mean(im2arr[temp_a+1, :sub,:], axis=1)])
            else:
                sel_vec = np.concatenate([sel_vec, np.mean(im2arr[0, :sub,:], axis=1)])
    else:
        if temp_a < h - read_len_pixel:
            sel_vec = np.mean(im2arr[temp_a:temp_a+10, temp_b,:], axis=1)
            # debug
        else:
            sub = read_len_pixel - h + temp_a
            sel_vec = np.mean(im2arr[temp_a:, temp_b,:], axis=1)
            if temp_b < w - 1:
                sel_vec = np.concatenate([sel_vec, np.mean(im2arr[:sub, temp_b+1,:], axis=1)])
            else:
                sel_vec = np.concatenate([sel_vec, np.mean(im2arr[:sub, 0,:], axis=1)])
    sel_vec = sel_vec.round().astype(int)
    return sel_vec

def hash(sel_vec):
    sel_str = [""+str(x) for x in sel_vec]
    hash_object = SHA512.new(data=(''.join(sel_str)).encode())
    return(hash_object)

def conversion(out_mode, hash_object, length_required):
    """
    out_mode : 0 -- binary
             : 1 -- decimal
             : 2 -- hex
             : 3 -- character
    return   : output in string format
    """
    hex_out = hash_object.hexdigest()
    bin_out = bin(int(hex_out, 16))[2:].zfill(len(hex_out)*4)
    if out_mode == 0:
        return(bin_out[-length_required:])
    elif out_mode == 2:
        return(hex_out[-length_required:])
    elif out_mode == 1:
        return(str(int(bin_out, 2))[-length_required:])
    elif out_mode == 3:
        hex_vec = []
        for i in range(int(len(hex_out) / 2)):
            idx = 2 * i
            hex_vec.append(int(hex_out[idx:idx+2],16))
        chr_vec = [chr(x) for x in hex_vec]
        d = ''.join(chr_vec)
        concatenated = chain(range(48,58), range(65, 91), range(97, 123))
        availset = [chr(x) for x in concatenated]
        chr_vec_sel = ''.join([x for x in d if x in availset])
        while (length_required > len(chr_vec_sel)):
            length_required = int(input('Unit-8 character does not meet the length with {}\n'
                                        'Instead input a length which needs to be smaller than {}\nInput here: '.format(length_required,len(chr_vec_sel)+1)))
        return(chr_vec_sel[-length_required:])

def out_bound_check(im2arr, loc):
    y, x, dir = loc
    max_y, max_x, n_channel = im2arr.shape
    retr_flg = False
    if (y >= max_y) | (y < 0):
        print("y is out of the range, should"
              " be within {}~{}".format(0, max_y))
        retr_flg = True
    elif (x >= max_x) | (x < 0):
        print("x is out of the range, should"
              " be within {}~{}".format(0, max_x))
        retr_flg = True
    elif dir not in range(0, 2):
        print("dir is out of the range, should"
              " be within {}~{}".format(0, 1))
        retr_flg = True

    return(retr_flg)