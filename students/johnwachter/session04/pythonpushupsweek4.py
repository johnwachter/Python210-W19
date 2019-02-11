#Python Pushups - warmup 2 'array_font9'
def array_front9(nums):
  checklist = nums[0:4]
  if 9 in checklist:
      return True
  return False
print(array_front9([1, 9, 3, 4, 9]))

def tempconverter(temp):
    if temp[-1] == 'C':
        celtemp = float(temp[:-1])
        tempinfar = ((celtemp)*(9/5) + 32)
        return ("{} Farenheit".format(tempinfar))
    elif temp[-1] == 'F':
        fartemp = float(temp[:-1])
        tempincel = (fartemp - 32)*(5/9)
        return ("{} Celcius".format(tempincel))

tempinput = input("Enter a temperature, followed by 'F' or 'C'")
print(tempconverter(tempinput))
