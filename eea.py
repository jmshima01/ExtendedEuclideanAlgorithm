from sys import argv

def eea(a,b):
    x = [1,0]
    y = [0,1]
    r = [a,b]
    a_l = [a]
    b_l = [b]
    q = [None,None]
    while (r[-1] > 1):
        q.append(a // b)
        r.append(a % b)
        x.append(x[-2] - q[-1]*x[-1])
        y.append(y[-2] - q[-1]*y[-1])
        a_l.append(b)
        b_l.append(r[-1])
        a,b = b,r[-1]
        
    print(f"a: {a_l}")
    print(f"b: {b_l}\n")
    print(f"q: {q}")
    print(f"r: {r}")
    print(f"x: {x}")
    print(f"y: {y}")
    return x[-1]

def gcd_(a,b):
    if(b==0):
        return a
    else:
        return gcd_(b,a%b)

if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: python3 eea.py a b")
        exit(1)
    
    a = int(argv[1])
    b = int(argv[2])
    print(f"gcd({a},{b}) =",gcd_(a,b))
    if gcd_(a,b) != 1:
        print("NO INVERSE\n")
        exit(0)
    print("============")
    result = eea(a,b)
    while result < 0:
        result+=b
    print("============")
    print("result: ",result)
    print()