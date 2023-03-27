"""
************************************************************************
BINARY SEARCH ALGORITHM IN PYTHON
CODE BY ALLAN CHIZANGA
ZOMAC DIGITAL FOUNDER
+263 719 203 127
allanofhcrist@gmail.com
*********************************************************************
"""
"""
VARIABLES:
      toSearchArray: represents our list of keys that contains a search key
      target : is the key the user is searching
      start: the starting index
      end : ending index
      binaryCounter : to record number of iterations made 
      response: contains a response whether the algorithm was a 
      success or not
TIME COMPLEXITY
O(logn) = log8 = 0.9

"""
toSearchArray = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 11  # initializer
start = 0
end = len(toSearchArray)-1
binaryCounter = 0  # to count number of binaries made
response = False  # whether the search was  successful or not
# take the target from the user
while True:
    try:
        target = int(input("which key are you searching ?"))
        break
    except ValueError:
        print("Please enter a value")
print(f"TARGET : {target}")
while start <= end:
    print(f"***********Binary '{binaryCounter+1}'*********************")
 # find the mid value
    mid = (start + end
           )//2  # mid term
    print(f"{mid} : mid")
    # find the target at the mid
    if target == toSearchArray[mid]:
        print(f"target {target} is at index {mid}")
        response = True
        break
    # find the target at the left side of the list
    elif target < toSearchArray[mid]:
        end = mid - 1
        binaryCounter += 1
    else:
        start = mid+1
        binaryCounter += 1
if response == True:
    print("**********Loop finished successfully************")
else:
    print("*********Loop finished unsuccessfully***********")
