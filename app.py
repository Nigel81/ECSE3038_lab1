
# def parallel(resistors):
#     R_total = 0
#     R_total = ((1/resistors[0]) + (1/resistors[1]) + (1/resistors[2]))
#     R_total = 1/R_total

#     print(str("%.3f" % R_total) + " ohms")

# resistor_list = [330,1000,2200]
# parallel(resistor_list) 


# def potential_divider(voltage,list):
#     resistors_series = 0
#     for u in list:
#         resistors_series = resistors_series + u
#     current = voltage/resistors_series
#     for y in list:
#         voltage_across_resistor = current * y
#         print(str("%.2f" % voltage_across_resistor) + "v")

# resistor_list_potential_divider = [3000, 6000, 2000, 3000]
# potential_divider(9,resistor_list_potential_divider)

def temperature_check(temp, units):
    if(units == "C"):
        if 35 < temp < 40:
            print("The patient's temperature is normal")
        elif temp <= 35:
            print("The patient is hypothermic")
        elif temp >= 40:
            print("The patient is hyperthermic")

    else:
        if 95 < temp < 104:
            print("The patient's temperature is normal")
        elif temp <= 95:
            print("The patient is hypothermic")
        elif temp >= 104:
            print("The patient is hyperthermic")

temperature_check(34, "C")
temperature_check(37, "C")
temperature_check(106, "F")
temperature_check(70, "F")
      