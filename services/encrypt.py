def encrypt(content):
        a=content
        b=[]
        for i in a:
                l=ord(i)
                l+=4
                i=chr(l)
                b.append(i)
        s=''
        s=s.join(b)
        return s