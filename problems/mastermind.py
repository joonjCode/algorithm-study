'''
Mastermind is a two-player game in which the first player attempts to guess the secret code of the second. In this version, the code may be any six-digit number with all distinct digits.

Each turn the first player guesses some number, and the second player responds by saying how many digits in this number correctly matched their location in the secret code. For example, if the secret code were 123456, then a guess of 175286 would score two, since 1 and 6 were correctly placed.

Write an algorithm which, given a sequence of guesses and their scores, determines whether there exists some secret code that could have produced them.

For example, for the following scores you should return True, since they correspond to the secret code 123456:

{175286: 2, 293416: 3, 654321: 0}
However, it is impossible for any key to result in the following scores, so in this case you should return False:

{123456: 4, 345678: 4, 567890: 4}
We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

'''
def mastermind(guesses:dict):
    # Password is 6 digit and is distinct
    # 0 - 9
    def _corresponds(guess, code, score):
        correct = 0
        for guess_digit, real_digit in zip(guess, code):
            if guess_digit == real_digit:
                correct +=1
    
        return correct == score

    from itertools import permutations
    possible_combination = [''.join(map(str, num)) for num in permutations(range(0,10),6)]
    for code in possible_combination:
        
        if all(_corresponds(str(guess), code, score) for guess, score in guesses.items()):
            return True
        break

    return False
class TestMastermind:
    def test_one(self):
        test_case = {175286: 2, 293416: 3, 654321: 0}
        assert mastermind(test_case) == True
    def test_two(self):
        test_case = {123456: 4, 345678: 4, 567890: 4}
        assert mastermind(test_case) == False