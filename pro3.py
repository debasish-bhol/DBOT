def firstMissingPositive(self, A):
        n = len(A)
        l =[]
        for i in range(n):
            if A[i]>=0:
                l.append(A[i])
        if len(l) <= 0:
            return "1"
        else:
            
            suma = sum(l)
            form = (n*(n+1))//2
            return form - suma
            
