pauls_name = 'Paul W. Bredenberg'
pauls_age = 27 # not a lie
pauls_height = 74 # inches
pauls_weight = 160 # lbs
pauls_eyes = 'Blue'
pauls_teeth = 'White'
pauls_hair = 'Brown'
inches = pauls_height
centimeters = pauls_height * 2.54
kilos = pauls_weight / 2.20462262


print "Let's talk about %s." % pauls_name
print "He's %d inches tall." % pauls_height
print "He's %d pounds heavy." % pauls_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (pauls_eyes, pauls_hair)
print "His teeth are usually %s depending on the coffee." % pauls_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    pauls_age, pauls_height, pauls_weight, pauls_age + pauls_height + pauls_weight)

print "In centimeters, Pauls is %d centimeters tall." % centimeters  

print "In kilos, paul weighs %d kilograms." % kilos  
