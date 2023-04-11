  Task 1

from prime_num_generator import prime_num_generator

def test_prime_num_generator():
     expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i in range(12):
        assert prime_num_generator().__next__() == expected_result[i]

    assert prime_num_generator(101).__next__() == 547
 


  Task 2 
  
  from palindrom import palindrom

def test_palindrom():
    assert palindrom("") == False

    assert palindrom(123) == False

    assert palindrom("This is a test string") == False

    assert palindrom("racecar") == True

    assert palindrom("radar") == True
    
    
    
   Task 3
  
  from validate_ip import validate_ip

def test_validate_ip():
    
    assert validate_ip("") == False

    assert validate_ip(123) == False

    assert validate_ip("10.0.0") == False
    assert validate_ip("10.0.0.256") == False
    assert validate_ip("10.0.0.-1") == False
    assert validate_ip("10.0.0.0.0") == False

    assert validate_ip("192.168.0.1") == True
    assert validate_ip("10.10.0.0") == True
    assert validate_ip("172.16.0.0") == True
    
    
    Task 4
    
    from get_os import get_os

def test_get_os():

    assert get_os("") == False

    assert get_os(123) == False

    assert get_os("192.168.0.1") == "Linux"
    assert get_os("10.10.0.0") == "Windows"
    assert get_os("172.16.0.0") == "MacOS"
    assert get_os("8.8.8.8") == "Unknown"
