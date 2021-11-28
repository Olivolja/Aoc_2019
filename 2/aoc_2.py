import math
insts = [int(x) for x in open("aoc_2019/2/aoc_2.txt").read().split(",")]
# print(insts)

def aoc(op_codes):

    for i in range(0,len(op_codes),4):
        if(op_codes[i] == 99 ):
            #print("halt")
            return op_codes[0] #quit

        if(op_codes[i] == 1): #add
            op_codes[op_codes[i+3]] = op_codes[op_codes[i+1]] + op_codes[op_codes[i+2]]
        elif(op_codes[i] == 2):
            op_codes[op_codes[i+3]] = op_codes[op_codes[i+1]] * op_codes[op_codes[i+2]]

    return op_codes

def aoc2(op_codes):
    for verb in range(0, 99):
        for noun in range(0,99):
            insts = [int(x) for x in open("aoc_2019/2/aoc_2.txt").read().split(",")]
            insts[1] = noun
            insts[2] = verb
            if (aoc(insts) == 19690720):
                print("ok")
                return(100*noun+verb)

print("Part 1:")
print(aoc(insts))

print("Part 2:")
print(aoc2(insts))
