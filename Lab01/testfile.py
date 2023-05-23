from factorial import fact

def test_factorial():
    fact.compute(1)==1
    fact.compute(2)==2
    fact.compute(4)==24
    fact.compute(6)==720