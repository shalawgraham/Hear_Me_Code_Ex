bread_slices = 9
peanut_butter = 8
jelly = 2

if bread_slices >= 2 and peanut_butter > 0 and jelly > 0:
	print "You have all the ingredients to make a PBJ sandwich."
else:
	print "You don't have enough of all of the ingredients."

if bread_slices >= 2 and peanut_butter > 0 and jelly > 0:
	print "You can make a PBJ sandwich. You have enough bread for {0} regular sandwiches and {1} open-faced sandwich.".format(bread_slices/2, bread_slices%2)

if peanut_butter > jelly and jelly > 0:
	print "You have enough peanut butter and jelly for {0} sandwiches.".format(jelly)
elif jelly > peanut_butter and peanut_butter > 0:
	print "You have enough peanut butter and jelly for {0} sandwiches.".format(peanut_butter)
else:
	print "You're a bit short on ingredients."
