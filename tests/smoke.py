import sys, math
task=sys.argv[1]
if task=='invsqrt':
    for x in range(1,10000):
        s=(22-x.bit_length())//2
        m=x<<(2*s)
        assert 2**20<=m<2**22
        assert math.isclose(1/math.sqrt(x),2**(s-10)/math.sqrt(m/2**20),rel_tol=1e-15)
elif task=='dqi':
    for q in [2,4,8,16,32]:
        for a in range(q):
            for b in range(q):
                assert (a^b)^b==a
else:
    for n in range(2,77):
        assert len([(i-1,i) for i in range(1,n)])==n-1
print(task, 'synthetic infrastructure smoke test passed; NOT official verification')
