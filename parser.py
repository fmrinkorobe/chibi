from exp import Val, Add

def parse(s: str):
    num = int(s)
    return Val(num)
 e = parse("123")
 print(e)

 s = "123+456"
 pos = s.find('+')
 print('pos', pos)

 s1 = s[Θ:pos]
 s2 = s[pos+1:]
 print(s, s1, s2)