# Coins changer

money = [1, 2, 3, 5, 10, 20, 50]

def change(sum):
    exchange = dict([c, float(sum)] for c in range(0,sum+1))
    exchange[0]=0
    # print exchange
    for i in range(1, sum+1):
        for j in [c for c in money if c<=i]:
            print 'i:',i,'j:',j,'ex:',exchange
            if exchange[i-j]+1<exchange[i]:
               exchange[i]=exchange[i-j]+1
               print 'ex:',i, 'ex[i]',exchange[i]
    return exchange[sum]

if __name__=="__main__":
    print change(int(raw_input("Give me money you want to exchange:")))
  
    
