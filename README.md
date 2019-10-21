# py-gf
### Python implementation for the finite field(Galois Field)

## How to use
- How to implement the custom galois field class
```python
from gf import gf
class gf3(gf):
def __new__(cls,val=0):
  return super().__new__(cls,3,val)
```
- How to use galois field 2 (pre-built in gf.py)
```python
from gf import gf2
a = gf2(0) #0
b = gf2(1) #1
c = gf2(3) #1
# automatically casted into the corresponding element of gaolois field 2
# using mod operation
print(a+b) #1
print(b+b) #0
print(a/b) #0
print(b/a) #zeroDivisionError
print(c*b) #1
```
