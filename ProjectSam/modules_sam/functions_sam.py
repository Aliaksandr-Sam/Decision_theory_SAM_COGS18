class Lottery():

    """
    Create an instance for any lottery

    Parameters
    ----------
    name : str
        Name of the lottery
    lottery : dictionary
        outcomes of a lottery with corresponding probabilities
    """
    
    def __init__(self, name, lottery):
        self.name = name
        self.lottery = lottery
        self.outcomes = [*lottery.keys()]
        self.probs = [*lottery.values()]

    def max_outcome(self):
        """Returns the largest possible outcome of the lottery"""

        return max(self.outcomes)

    def min_outcome(self):
        """Returns the lowest possible outcome of the lottery"""

        return min(self.outcomes)

    def exp_value(self):
        """
        Returns expected value of the lottery

        """

        output = 0

        for el1, el2 in zip(self.outcomes,self.probs):
            output += el1*el2

        return output

    def variance(self):
        """Returns variance of the lottery"""

        output = 0

        #sums squared outcomes multiplied by corresponding probabilities
        for el1, el2 in zip(self.outcomes, self.probs):
            output += el2*el1**2

        output = output - self.exp_value()**2
        return output

    def most_probable_outcome(self):
        """Returns the outcome(or outcomes) with the largest probability"""

        output_list = []

        for outcome in self.lottery:
            if self.lottery[outcome] == max(self.probs):
                output = outcome
                output_list.append(outcome)

        if len(output_list) == 1:
            return output
        else:
            return output_list

    def check_correctness(self):
        """Checks if the lottery is correctly defined"""

        if round(sum(self.probs), 5) != 1:
            return "WARNING!!! The sum of probabilities is not equal to 1."

        for el in self.probs:
            if el < 0:
                return "WARNING!!! Probabilities must be non-negative"
                break

        return "Lottery is correctly specified"


def choice_maximax(lottery_a, lottery_b):
    """
    Returns preference between two lotteries based on maximax criteria

    Parameters
    ----------
    lottery_a : Lottery Object
        Object of class Lottery
    lottery_b : Lottery Object
        Object of class Lottery

    Returns
    -------
    str
        lottery_a is preferred to lottery_b or vice versa or no preference
        depending on the comparison of maximum outcomes
    """

    if lottery_a.max_outcome() > lottery_b.max_outcome():
        return f"Lottery {lottery_a.name} is preferred to lottery {lottery_b.name} by maximax criteria"

    elif lottery_b.max_outcome() > lottery_a.max_outcome():
        return f"Lottery {lottery_b.name} is preferred to lottery {lottery_a.name} by maximax criteria"

    else:
        return f"Lotteries {lottery_a.name} and {lottery_b.name} are indifferent by maximax criteria"


def choice_minimax(lottery_a, lottery_b):
    """
    Returns preference between two lotteries based on minimax criteria

    Parameters
    ----------
    lottery_a : Lottery Object
        Object of class Lottery
    lottery_b : Lottery Object
        Object of class Lottery


    Returns
    -------
    str
        lottery_a is preferred to lottery_b or vice versa or no preference
        depending on the comparison of minimum outcomes
    """

    if lottery_a.min_outcome() > lottery_b.min_outcome():
        return f"Lottery {lottery_a.name} is preferred to lottery {lottery_b.name} by minimax criteria"

    elif lottery_b.min_outcome() > lottery_a.min_outcome():
        return f"Lottery {lottery_b.name} is preferred to lottery {lottery_a.name} by minimax criteria"

    else:
        return f"Lotteries {lottery_a.name} and {lottery_b.name} are indifferent by minimax criteria"


def sorted_unique_list(list1, list2, reverse = False):
    """
    Creates a sorted list of unique elements of two input lists

    Parameters
    ----------
    list1 : list
        first input list
    list2 : list
        second input list
    reverse : bool
        sorting in descending order if True; in ascending if False(False is set by default)

    Returns
    -------
    output : list
        sorted list of all unique elements of two lists

    """
    output = list(set(list1 + list2))
    output.sort(reverse=reverse)

    return output


def fosd_lottery(lottery_A, lottery_B):
    """
    Returns preference between two lotteries based on FOSD criteria

    Parameters
    ----------
    lottery_A : Lottery Object
        Object of class Lottery
    lottery_B : Lottery Object
        Object of class Lottery


    Returns
    -------
    str
        lottery_A first order stochastically dominates lottery_B or vice versa
        or there is no FOSD relationship between the two lotteries
        depending on the comparison of cumulative probabilities of the lotteries
        at all possible outcomes
    """

    outcomes_list = sorted_unique_list(lottery_A.outcomes, lottery_B.outcomes)


    #initializing starting cumulative probabilities of lotteries
    cum_prob_A = 0
    cum_prob_B = 0
    A_fosd_B = True
    B_fosd_A = True

    for el in outcomes_list:

        #checking the condition of B FOSD A
        if cum_prob_B > cum_prob_A and B_fosd_A:
            B_fosd_A = False

        # checking the condition of A FOSD B
        if cum_prob_A > cum_prob_B and A_fosd_B:
            A_fosd_B = False

        # updating cumulative probability of lottery A
        if el in lottery_A.outcomes:
            cum_prob_A += lottery_A.lottery[el]

        # updating cumulative probability of lottery B
        if el in lottery_B.outcomes:
            cum_prob_B += lottery_B.lottery[el]

    if B_fosd_A:
        return f"Lottery {lottery_B.name} first order stochastically dominates Lottery {lottery_A.name}"

    elif A_fosd_B:
        return f"Lottery {lottery_A.name} first order stochastically dominates Lottery {lottery_B.name}"

    else:
        return "There is no fosd relationship"


def mean_preserving_spread(lottery_a, lottery_b):
    """
    Returns preference between two lotteries based on mean preserving spread criteria

    Parameters
    ----------
    lottery_a : Lottery Object
        Object of class Lottery
    lottery_b : Lottery Object
        Object of class Lottery

    Returns
    -------
    str
        lottery_A is a mean preserving spread of lottery_B or vice versa
        or they are indifferent by this criteria
        depending on the comparison of cumulative probabilities of the lotteries
        at all possible outcomes
        if means of two lotteries are not equal the method is not applicable
    """
    if lottery_a.exp_value() != lottery_b.exp_value():
        return "The means of the two lotteries are not equal. \n Mean preserving spread method is not applicable"

    else:

        if lottery_a.variance() == lottery_b.variance():
            return f"Lotteries {lottery_a.name} and {lottery_b.name} are indifferent \n by mean preserving spread method"

        elif lottery_a.variance() > lottery_b.variance():
            return f"Lottery {lottery_b.name} is preferred to lottery {lottery_a.name} \n by mean preserving spread method"

        elif lottery_a.variance() < lottery_b.variance():
            return f"Lottery {lottery_a.name} is preferred to lottery {lottery_b.name} \n by mean preserving spread method"