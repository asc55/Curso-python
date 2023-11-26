def notas(* n, situacao=False):
    r = {}
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["média"] = (sum(n)/len(n))
    media = sum(n)/len(n)
    if situacao:
        if media >= 7:
            r["situacao"] = 'BOA'
        elif 5 <= media <= 6.9:
            r["situacao"] = 'RAZOAVEL'
        else:
            r["situacao"] = 'RUIM'
    return r


r = notas(5.5, 9.5, 10, 6.5, situacao=True)
print(r)