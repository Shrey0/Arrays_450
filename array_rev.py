def rev(A, start, end):
    while start<end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
        
A = [1,2,3,4,5,6]
print(A)
rev(A,0,5)
print("Reversed List")
print(A)