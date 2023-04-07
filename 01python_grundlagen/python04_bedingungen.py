# Bedingungen

# A) Bedingungen sind Ausdrücke, die True oder False ergeben:
print(10 > 5)
#=> True
print(10 > 100)
#=> False

# B) Du kannst Code abhängig von einer Bedingung mit if ausführen:
alter = 12
filmfreigabe = 16
if (alter >= filmfreigabe):
    print("Viel Spaß beim Film!")
else:
    print("Du bist leider noch nicht alt genug, um den Film zu schauen.")
#=> Du bist leider noch nicht alt genug, um den Film zu schauen.
    
# C) Ihr könnt Bedingungen in eine Listenabstraktion einbauen,
# und auf diese Weise Listen filtern:
zahlen = [29, 3, 11, 17, 21, 5]
groesser10 = [zahl for zahl in zahlen if zahl > 10]
print(groesser10)