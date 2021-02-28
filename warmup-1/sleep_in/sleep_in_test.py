'''
Unit tests for the sleep_in function for [this Coding Bat problem](https://codingbat.com/prob/p173401)
'''

# import the code to be tested
from sleep_in import sleep_in

# begin writing tests (top-level test suite)
def describe_a_sleep_in_function():

    def that_determines_whether_or_not_we_should_sleep_in():
        '''
        The two things we care about are if it's a weekend/weekday,
        and if we're on vacation or not. 2 variables that can have
        2 values each, means we have a total of (2 x 2 = 4) 4 possibles
        outcomes to be concerned about.
        '''
        assert sleep_in(True, True) == True # weekday but on vacation -> sleep in 
        assert sleep_in(True, False) == False # weekday but NOT on vacation -> do NOTsleep in 
        assert sleep_in(False, True) == True # weekday and on vacation -> sleep in 
        assert sleep_in(False, False) == True # weekday but NOT on vacation -> sleep in 