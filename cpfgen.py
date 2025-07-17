cpf = input()

def cpfCheck(dig):
    lcpf = list(map(int, cpf))
    lcpf[0:0] = dig

    r = sum(d*(10-i) for i,d in enumerate(lcpf))%11

    if r == 0 or r == 1: lcpf.append(0)
    else: lcpf.append(11-r)
    
    r = sum(d*(10-i) for i,d in enumerate(lcpf[1:]))%11

    if r == 0 or r == 1: lcpf.append(0)
    else: lcpf.append(11-r)

    lcpf = map(str, lcpf)

    return lcpf

res = []
for i in range(1000):
    dig = str(i)
    dig = list(map(int, dig))

    dig = [0]*(3-len(dig)) + dig

    res.append(''.join(cpfCheck(dig)))

with open(f'gens/{cpf} cpfgen', 'w') as f: f.write('\n'.join(res))
