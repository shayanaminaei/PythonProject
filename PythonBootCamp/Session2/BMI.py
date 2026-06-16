# calculate user's BMI
print("BMI calculator:")

def get_height():
    height = float(input("Height(CM): "))

    if height < 100:
        print("Height must be in CM, so try again...")
        return get_height()

    return height / 100


def get_weight():
    weight = float(input("Weight(KG): "))

    if weight <= 0:
        print("Weight must be KG, so try again...")
        return get_weight()

    return weight


height = get_height()
weight = get_weight()

bmi = weight // (height * height)

print("Calculating...")
print("BMI =", bmi)

if bmi < 18.5:
    print("Under weight")
elif 18.5 < bmi <= 25:
    print("Normal")
elif 25< bmi <= 30:
    print("Over weight")
elif 30 < bmi <= 35:
    print("Obese")
elif bmi > 35:
    print("Extreme")

print("Exiting...")