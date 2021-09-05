NAME_TO_HEX = {"aliceblue": "#f0f8ff", "beige": "#f5f5dc", "blueviolet": "#8a2be2", "coral": "#ff7f50",
               "cyan1": "#00ffff", "darkkhaki": "#bdb76b", "darkorchid": "#9932cc", "DarkSalmon": "#e9967a",
               "deeppink1": "#ff1493", "ghostwhite": "#f8f8ff"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in NAME_TO_HEX:
        print(f"{colour_name:8} is {NAME_TO_HEX[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
