## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence

#this will be recursive, so start with the first element?
#fib[0]: #1

#while loop
fib=[1]
while len(fib)<11:
   if len(fib)<2:
      fib.append(1)
   else:
      fib.append(fib[-1]+fib[-2]) #append the next element
      print fib

# for loop
#does not work
fib_loop = [i+(i-1) for i-1 in range(1,10)]

