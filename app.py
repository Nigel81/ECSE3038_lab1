
def parallel(resistors):
    R_total = 0
    R_total = ((1/resistors[0]) + (1/resistors[1]) + (1/resistors[2]))
    R_total = 1/R_total

    print(str("%.3f" % R_total) + " ohms")

resistor_list = [330,1000,2200]
parallel(resistor_list) 


      