#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0
    # O(n) * O(1) = O(n)
    while (a < n * n * n):  # O(n)
        a = a + n * n       # O(1)
```

The time complexity of this snippet is linear O(n), because the statement inside the while loop is constant O(1), it doesn't depend on how big n input is. However while loop depends on how big n is, the bigger n will be the more iterations will be in a loop that makes time complexity linear O(n).


```python
b)  sum = 0
    # O(n)*O(lon(n)) = O(n log(n))
    for i in range(n):  # O(n)
      j = 1             # O(1)
      while j < n:      # O(n)
        j *= 2          # O(1)
        sum += 1        # O(1)
```

The time complexity of this snippet is quadratic O(n^2), there are two nested loops (for and while) which depend on input n. the larger n will be iterations will be doubled, therefore time complexity is quadratic O(n^2).


```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) # 
```

This function is being called recursively n-1 each time before reaching the base case. Since it is n-1, we deduct 1 from n before calling the function, so the time complexity is O(n-1), and it's the same as O(n), therefore it's linear. 


## Exercise II


In my opinion, the effective way to determine the floor number is by applying binary search, find the middle and throw the egg, ckeck if the thrown egg breaks, if it does,then there is no need to consider higher floors than the middle one, otherwise there is no need to consider lower floors than the middle one. And repeat all the steps.  

Pseudo code: 

determine an array of floors
get the lowest floor
get the highest floor
repeat steps below until the highest floor less than or equal to lowest floor
    find the middle floor
    throw an egg from the middle floor
    if egg broke
        set the middle floor's value as a new hightest floor
    else
        set the middle floor's value as a new lowest floor 
return the floor value

Time Complexity:

The time complexity of this algorithm is logarithmic becase at each checking (iteration) we divide array in half, even if there is a loop of O(n), meaning that it depends on what number is n, since we dividing n/2 each iteration, the time complexity is O(log(n))

Code Example:

```python
def find_floor(floors_num):
    eggs = 999 # plenty of eggs
    dropped = 0 # drop count
    broken = 0  # broken count
    lower = 0   # lower floor
    higher = len(n) # higher floor

    # make an assumption that the floor value is 3 
    f = 3; 
    
    while higher >= lower:
    # find middle floor
        middle_floor = (lower+higher)//2
        # throw the egg
        eggs -= 1
        # base case assume f is 3rd floor that egg 
        if n[middle_floor] == f:
            dropped += 1
            broken += 1
            return n[middle_floor], dropped, broken
        # search the floor
        else:
            # if 
            if n[middle_floor] > f:
                dropped +=1
                broken +=1
                higher = middle_floor
            else:
                dropped +=1
                lower = middle_floor+1
    return n[middle_floor], dropped, broken

n = [1,2,3,4,5,6,7]  
find_floor(n) 
```

    
    
    
