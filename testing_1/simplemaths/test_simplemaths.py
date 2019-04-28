import pytest
from pytest import raises
from simplemaths.simplemaths import SimpleMaths as sm

class TestSimpleMaths():
    
    def test_constructor_float(self):
        with raises(TypeError):
            sm(2.0)
      
    def test_constructor_neg(self):
        sm(-2)
    
            
    def test_constructor_string(self):
        with raises(TypeError):
            sm('bollocks')
            
            
    def test_square_neg(self):
        assert sm(-2).square() == sm(2).square()
        
    def test_square_positivity(self):
        assert sm(-3).square() >= 0
        
    def test_factorial_monotony(self):
        assert sm(3).factorial() > 3
        
    def test_factorial_1(self):
        assert sm(1).factorial() == 1
        
    def test_factorial_0(self):
        assert sm(0).factorial() == 1
        
    def test_power_monotony(self):
        with raises(AssertionError):
            assert sm(5).power() < 5
            
    def test_odd_or_even_evens(self):
        assert sm(2).odd_or_even() == 'Even'
        
    def test_odd_or_even_odds(self):
        assert sm(3).odd_or_even() == 'Odd'
        
    def test_odd_or_even_zero(self):
        assert sm(0).odd_or_even() == 'Even'
        
    def test_square_root_positivity(self):
        for x in range(1,10):
            assert sm(x).square_root() >= 0
            
    def test_square_root_monotony(self):
        for x in range(1,10):
            assert sm(x).square_root() <= x
            
    
        
        
        

        
    
        
    
        
    
    
    
    