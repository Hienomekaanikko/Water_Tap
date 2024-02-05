import watertap
import waterglass

water_on = watertap.WaterTap()
fill_glass =waterglass.WaterGlass()
tap_on = True

while tap_on:
    water_on.open_tap()
    ask = input("Fill a glass? ")
    if ask == "yes":
        print(fill_glass.fill_glass())
    else:
        water_on.close_tap()
        tap_on = False
        
