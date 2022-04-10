#!/usr/bin/python3
import wasmtime.loader
import assembly4
import string
import itertools
def init_flag(pair):
    for i in range(len(flag)):
        assembly4.memory.data_ptr[1072+i]=ord(flag[i])
    for j in range(len(flag_so_far)):
        assembly4.memory.data_ptr[1072+8+j]=ord(flag_so_far[j])
    assembly4.memory.data_ptr[1072+8+len(flag_so_far)]=ord(pair[0])
    assembly4.memory.data_ptr[1072+8+len(flag_so_far)+1]=ord(pair[1])

def print_test_flag():
    g=''
    for j in range(1072,1072+8+2+len(flag_so_far)):
        g=g+chr(assembly4.memory.data_ptr[j])
    print(g)

def count_match():
    count = 0
    while (assembly4.memory.data_ptr[1024+count]==assembly4.memory.data_ptr[1072+count]):
        count=count+1
    return count

flag="picoCTF{0123456789abcdef0123456789abcdef"
flag_chars=string.ascii_lowercase+"_"+string.digits+"}\x00"  # that middle character might be a space? unclear
flag_so_far=""
for i in range(24):
    for j in itertools.product(flag_chars,repeat=2):
        init_flag(j)
        assembly4.check_flag()
        if(count_match()>=10+len(flag_so_far)):
            flag_so_far+=(j[0]+j[1])
            print("picoCTF{"+flag_so_far)
            break
