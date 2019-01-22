#Title: pythonpushups2.py
#Change Log: (Who, When, What)
#JWachter, 1/21/2019, continuing python pushups exercises

"""Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10."""

def makes10(a, b):
  if a + b == 10:
    return True
  elif a == 10 or b == 10:
    return True
  else:
    return False


"""Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number."""
def near_hundred(n):
  if abs(100 - n) <= 10:
    return True
  elif abs(200 - n) <=10:
    return True
  else:
    return False

"""Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative."""
def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b <  0:
      return True
    else:
      return False
  elif a > 0 and b < 0:
    return True
  elif a < 0 and b > 0:
    return True
  else:
    return False

"""Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged."""

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  else:
    return "not " + str
