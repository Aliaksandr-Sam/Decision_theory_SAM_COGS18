import sys
sys.path.append('../')


from modules_sam.functions_sam import Lottery, choice_maximax, choice_minimax, fosd_lottery, sorted_unique_list, mean_preserving_spread

""" ALLAIS Paradox"""

a1 = Lottery('a1', {1000000:1})
a2 = Lottery('a2', {0:0.01, 1000000:0.89, 5000000:0.1})
b1 = Lottery('b1', {0:0.89, 1000000:0.11})
b2 = Lottery('b2', {0:0.9, 5000000:0.1})

##In reality majority of people have the following preferences:
## a1 is preferred to a2
## b2 is preferred to b1

##Here I show that such preferences do not obey neither
## maximax criteria nor minimax criteria

print(choice_maximax(a1,a2))
print(choice_maximax(b1,b2))
print(choice_minimax(a1,a2))
print(choice_minimax(b1,b2))

##The outputs of above code suggest that the individual following minimax criteria
##when making a choice between lotteries should be indifferent between b1 and b2
## This does not correspond to choice of majority of people in real life
##thus, minimax is a poor method explaining ALLAIS Paradox

##Also ,the outputs above suggest that the individual following maximax criteria
##should choose a2 when making a choice between lotteries should prefer a2 to a1
## This does not correspond to choice of majority of people in real life
##thus, maximax is a poor method explaining ALLAIS Paradox


"""FOSD"""

lot1 = Lottery('lot1', {95:1})
lot2 = Lottery('lot2', {90:0.5, 110:0.5})
lot3 = Lottery('lot3', {95:0.3, 100:0.1, 120:0.6})

##In reality any rational individual prefers such a lottery that
##first order stochastically dominates the other

##Here I show the presence/absence of FOSD condition
## when comparing lotteries lot1, lot2, lot3

print(fosd_lottery(lot1, lot2))
print(fosd_lottery(lot1, lot3))
print(fosd_lottery(lot2, lot3))

##The outputs of above code suggest that any rational individual
##should choose lottery lot3 in any case when comparing the above
##three lotteries because it first order stochastically
##dominates both lotteries lot1 and lot2.

##At the same time, there is no FOSD relationship between
##lotteries lot1 and lot2, and it is only due to each individual
##level of risk aversion(or risk loving) which one to choose


"""Mean Preserving Spread"""

lot_a = Lottery('lot_a', {60:0.75, 420:0.25})
lot_b = Lottery('lot_b', {120:0.75, 240:0.25})
lot_c = Lottery('lot_c', {100:0.2, 200:0.8})

##In reality any rational risk averse individual does not prefer such a
##lottery that is a mean preserving spread of another
##(Given the choice between two lotteries with equal means)

##Here I show the presence/absence of this condition
## when comparing lotteries lot_a, lot_b, lot_c

print(mean_preserving_spread(lot_a, lot_b))
print(mean_preserving_spread(lot_a, lot_c))
print(mean_preserving_spread(lot_b, lot_c))

##The outputs of above code suggest that any rational risk averse individual
##should choose lot_b when comparing with lot_a by mean preserving
##spread criteria(means of these two lotteries are equal, but lot_a
##is more spread).

##At the same time, we are not able to say anything about preferences
##of a risk averse individual when comparing lot_c with either lot_a
##or lot_b because expected value of lot_c is different from expected
##value of lotteries lot_a and lot_b

