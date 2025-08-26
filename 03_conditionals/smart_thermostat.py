device_status = "Active"
temperature = 11  # in Celsius

if device_status == "Active":
    if temperature > 30:
        print("It's hot! Turning on the AC.")
    elif temperature < 20:
        print("It's cold! Turning on the heater.")
    else:
        print("Temperature is comfortable.")
else:
    print("Device is inactive.")
