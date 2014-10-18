# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

bread = 20 
#how many individual slices of bread you have

peanut_butter = 5 
#how many servings of peanut butter you have

jelly = 10 
#how many servings of jelly you have

sandwich=1 
#sandwich start count number

two_slices = bread/2 - sandwich 
#how many sandwiches you can make with the bread you have; two slices fo bread per sandwich, minus sandwich count number to count down for leftovers

if bread >=2 and peanut_butter >=1 and jelly >=1:
	print "Let's make a sandwich" #checks to make sure you have enough ingredients to make at least one sandwich
elif bread <2 or jelly <1 or peanut_butter <1:
	print "I can't make any sandwiches."

while bread >=2 and peanut_butter >=1 and jelly >=1:
	print "Making sandwich #{0}. \nI have enough bread for {1} more sandwiches, enough peanut butter for {2} more, and enough jelly for {3} more.\n".format(sandwich, two_slices, peanut_butter-1, jelly-1)
	bread = bread-2 #reducing the amount of bread by 2 slices at a time
	peanut_butter = peanut_butter-1 #reducing the serving of peanut butter
	jelly = jelly-1 #reducing the serving of jelly
	sandwich = sandwich+1 #counting the sandwich number
	two_slices = two_slices-1 #reducing the bread serving (2 slices) count

if jelly==0:
	print "All done! I ran out of jelly." 

if bread<=1:
	print "All done! I ran out of bread." 

if peanut_butter==0:
	print "All done! I ran out of peanut butter." 

