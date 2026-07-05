from fontTools import ttLib

# For the Roman variable font
font = ttLib.TTFont("../fonts/variable/Nevermind[wght].ttf")
name_table = font['name']

# Add Name ID 16 and 17
name_table.setName("Nevermind", 16, 3, 1, 0x409)
name_table.setName("Regular", 17, 3, 1, 0x409)

font.save("../fonts/variable/Nevermind[wght].ttf")
print("✅ Name IDs 16 and 17 added to Nevermind[wght].ttf")

# For the Italic variable font if it exists
try:
    font_italic = ttLib.TTFont("../fonts/variable/Nevermind-Italic[wght].ttf")
    name_table_italic = font_italic['name']
    
    name_table_italic.setName("Nevermind", 16, 3, 1, 0x409)
    name_table_italic.setName("Italic", 17, 3, 1, 0x409)
    
    font_italic.save("../fonts/variable/Nevermind-Italic[wght].ttf")
    print("✅ Name IDs 16 and 17 added to Nevermind-Italic[wght].ttf")
except:
    print("ℹ️  No Italic file found (normal if you only have one axis)")