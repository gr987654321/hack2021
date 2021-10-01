def numConcat(num1, num2):
       
        # Convert both the numbers to
        # strings
        num1 = str(num1)
        num2 = str(num2)
          
        # Concatenate the strings
        num1 += num2
          
        return num1
  
  
# Driver's code
a =58
b =60
print(numConcat(a, b))
