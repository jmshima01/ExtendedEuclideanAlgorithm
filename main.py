from sys import argv


def eea(a,b):

    x = [1,0]
    y = [0,1]
    r = [a,b]
    a_l = [a]
    b_l = [b]
    q = [None,None]
    while (r[-1] >= 1):
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

    
def gcd_(a,b):
    # if(a<b):
    #     a,b=b,a
    if(b==0):
        return a
    else:
        return gcd_(b,a%b)


if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: python3 main.py a b")
        exit(1)
    
    a = int(argv[1])
    b = int(argv[2])

    eea(a,b)
    
    
    print("============")
    print(gcd_(a,b))
    if gcd_(a,b) != 1:
        print(f"NO INVERSE: gcd = {gcd_(a,b)}")
        exit(1)
