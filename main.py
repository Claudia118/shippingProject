print("Ground Shipping, small flat charge plus a rate based on the weight of your package (GS).\n"
      "Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight (GSP).\n" 
     "Drone Shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping (DS).\n")

#Get weight of package from user
weight = float(input("Please enter the package weight: "))

#Ground Shipping, small flat charge plus a rate based on the weight of your package
def ground_shipping(weight):
    if weight <= 2:
        cost_ground = weight * 1.50 + 20.00
    elif weight > 2 and weight <= 6:
        cost_ground = weight * 3.00 + 20.00
    elif weight > 6 and weight <= 10:
        cost_ground = weight * 4.00 + 20.00
    else:
        cost_ground = weight * 4.75 + 20.00
    return cost_ground

#Ground Shipping Premium
def premium_shipping():
  cost_ground_premium = 125.00
  return cost_ground_premium


def start(weight):
    userAnswer = input("What shipping options to you choose (GS), (GSP) OR (DS): ").upper()

    if userAnswer == "GS":
        print(ground_shipping(weight))
    elif userAnswer == "GSP":
        print(premium_shipping())



start(weight)
