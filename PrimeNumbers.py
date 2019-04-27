class PrimeNumbers:

    def prime(self, x):
        print("x is:"+str(x))
        
        if  x<3: 
             return True
        else:
            for i in range(x):
                print(i)
                if i>1 and x%i == 0:
                    return False
                else:
                    if i<2:
                        continue
        return True       

            

y = PrimeNumbers()
print(y.prime(1))
print(y.prime(2))
print(y.prime(5))


