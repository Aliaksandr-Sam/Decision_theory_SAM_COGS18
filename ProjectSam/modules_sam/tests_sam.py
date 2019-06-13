from functions_sam import Lottery, choice_maximax, choice_minimax, fosd_lottery, sorted_unique_list, mean_preserving_spread



def test_Lottery():
    """Tests for class Lottery and its methods """

    A = Lottery('daje', {1:0.2, 2:0.4, 10:0.4})
    B = Lottery('baje', {1:1, 5:0.4})
    C = Lottery('asd', {1:-0.2, 2:1.2})

    #testing correctness of attributes of Lottery
    assert 0.2 in A.probs
    assert 0.4 in A.probs
    assert 1 in A.outcomes
    assert 2 in A.outcomes
    assert 10 in A.outcomes
    assert A.lottery == {1:0.2, 2:0.4, 10:0.4}
    assert A.name == 'daje'

    #test for min_outcome() method
    assert A.min_outcome() == 1

    # test for max_outcome() method
    assert A.max_outcome() == 10

    # test for exp_value() method
    assert round(A.exp_value(),1) == 5

    # test for variance() method
    assert round(A.variance(), 1) == 16.8

    # test for check_correctness() method
    assert B.check_correctness() == "WARNING!!! The sum of probabilities is not equal to 1."
    assert C.check_correctness() == "WARNING!!! Probabilities must be non-negative"
    assert A.check_correctness() == "Lottery is correctly specified"

    # test for most_probable_outcome() method
    assert A.most_probable_outcome() == [2, 10]
    assert C.most_probable_outcome() == 2


def test_choice_maximax():
    """Tests for 'choice_maximax' function"""

    A = Lottery("bingo", {1:0.2, 4:0.6, 10:0.2})
    B = Lottery("jango", {1: 0.3, 4: 0.2, 10: 0.5})
    C = Lottery("wongo", {1: 0.4, 4: 0.3, 14: 0.3})

    #test of indifference
    assert choice_maximax(A, B) == "Lotteries bingo and jango are indifferent by maximax criteria"

    #test of preference
    assert choice_maximax(B, C) == "Lottery wongo is preferred to lottery jango by maximax criteria"


def test_choice_minimax():
    """Tests for 'choice_minimax' function"""

    A = Lottery("bingo", {1:0.2, 4:0.6, 10:0.2})
    B = Lottery("jango", {1: 0.3, 4: 0.2, 10: 0.5})
    C = Lottery("wongo", {2: 0.4, 4: 0.3, 14: 0.3})

    # test of indifference
    assert choice_minimax(A, B) == "Lotteries bingo and jango are indifferent by minimax criteria"

    # test of preference
    assert choice_minimax(B, C) == "Lottery wongo is preferred to lottery jango by minimax criteria"


def test_sorted_list_unique():
    """Tests for 'sorted_list_unique' function"""

    list1 = [1,2,3]
    list2 = [3,4,5]

    #test if reverse is default value(False)
    assert sorted_unique_list(list1, list2) == [1, 2, 3, 4, 5]

    #test if reverse is True
    assert sorted_unique_list(list1, list2, reverse = True) == [5, 4, 3, 2, 1]


def test_fosd_lottery():
    """Tests for 'fosd_lottery' function"""

    A = Lottery("bingo", {1: 0.2, 4: 0.6, 10: 0.2})
    B = Lottery("jango", {1: 0.3, 4: 0.2, 10: 0.5})
    C = Lottery("wongo", {1: 0.2, 4: 0.3, 14: 0.5})

    #test for no FOSD relationship
    assert fosd_lottery(A, B) == "There is no fosd relationship"

    #test for presence of FOSD
    assert fosd_lottery(B, C) == "Lottery wongo first order stochastically dominates Lottery jango"


def test_mean_preserving_spread():
    """Tests for 'mean_preserving_spread' function"""

    A = Lottery("bingo", {10: 0.2, 20: 0.6, 100: 0.2})
    B = Lottery("jango", {10: 0.7, 85: 0.2, 200: 0.1})
    C = Lottery("wongo", {10: 0.2, 40: 0.3, 60: 0.5})

    #Test when means are not equal
    assert mean_preserving_spread(A,B) == "The means of the two lotteries are not equal. \n Mean preserving spread method is not applicable"

    # Test when means are  equal
    assert mean_preserving_spread(C,B) == "Lottery wongo is preferred to lottery jango \n by mean preserving spread method"