# calulate bmi based on height and weight.
import math;
# bmi is calculate as weight in kg divided by height in meters squared.

def ft_m(height):
    meters = height*.3048
    return meters

def lb_kg(weight):
    kgs = weight*0.453592
    return kgs


def bmi_calc_empirical(height, weight):
    weight = lb_kg(weight)
    height= ft_m(height)
    bmi = math.ceil((weight/(math.pow(height,2))))
    return bmi

if __name__ == "__main__":
    h = input("what is th persons height?")
    w = input("what is the persons weight?")
    h = float(h)
    w = float(w)
    print(bmi_calc_empirical(h,w))
              
print(math.pow(2,3))
print(5+(8/12))

print(bmi_calc_empirical((5+(8/12)), 200));
