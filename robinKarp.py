import  random
class robin:
    def __init__(self,x,m,prime):
        self.x=x
        self.m=m
        self.prime=prime
        self.map=[0]*(m)
    def hash_number(self,word):
        words=list(word)
        if(isinstance(word,str)):
            words=[ord(x) for x in words]
        #print(words)
        sum=0
        j=0
        for i in words:
            sum=sum + i*(self.x**j)
            j+=1
        #print(sum)
        sum=sum%self.prime
        sum=sum%self.m
        return sum

    def hash_array(self,text,pattern):
        H=[]
        j=len(pattern)
        for i in range(0, (len(text) - len(pattern)) + 1):
            H.append(self.hash_number(text[i:j]))
            j+=1
        return H

    def PrecomputeHashes(self,text,pattern):
        text=[ord(x) for x in text]
        pattern=[ord(x) for x in pattern]
        H=[0] *((len(text)-len(pattern))+1)
        last_substring=text[len(pattern)-len(text)+1:len(text)]
        print('last',last_substring)
        H[len(H)-1]=self.hash_number(last_substring)
        #y=1
        print('last hash',H[len(H)-1])
        print(H)
        #for i in range(1,len(pattern)):
         #   y=(y*self.x)%self.prime
        y=self.x**(len(pattern))
        print('y',y)
        for i in range(len(text)-len(pattern)-1,-1,-1):
            #print('substrings',text[i+len(pattern)])
            H[i]=((self.x * H[i+1] + text[i] - y * text[i+len(pattern)]) % self.prime)%100
            print('hash  as',H[i])
        return H
    def compare_hash(self,text_hash,pattern_hash):
        pos=[]
        for i in range(len(text_hash)):
            if(text_hash[i]==pattern_hash):
                pos.append(i)
        return pos

if __name__ == '__main__':
    text = 'baaaaaaab'
    pattern = 'aaaaa'
    prime=1000000007
    m=100
    x=3

    print(text)
    print(pattern)
    r = robin(x,m,prime)
    pattern_hash=r.hash_number(pattern)
    text_hash=r.PrecomputeHashes(text,pattern)

    #text_hash_n=r.hash_array(text,pattern)
    #print(text_hash)
    print(text_hash)
    print(r.compare_hash(text_hash,pattern_hash))

