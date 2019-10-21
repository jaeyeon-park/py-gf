# Author : Jaeyeon-park
# Created : 2019-10-21
# Updated : 2019-10-21
# Description : Python implementation of Galois field compatible with numpy
class gf(int):
    __gfnum = None
    __inverse = None

    @classmethod
    def calculateInverses(cls):
        inv = {}
        for i in range(1,cls.__gfnum):
            for j in range(1,cls.__gfnum):
                if (i*j)%cls.__gfnum==1:
                    inv[i] = j
            if inv.get(i) is None:
                raise Exception("Impossible gfnum: {}".format(cls.__gfnum))
        cls.__inverse = inv

    def __checkOperandsType(func):
        def override(self,val):
            if (isinstance(val,gf) and val.gfnum != self.gfnum) or not isinstance(val,int):
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(type(self),type(val)))
            return func(self,val%self.gfnum)
        return override

    @property
    def gfnum(self):
        return type(self).__gfnum
    @property
    def inverse(self):
        cls = type(self)
        if self == 0:
            raise ZeroDivisionError("Zero cannot have inverse")
        else:
            return cls(cls.__inverse[self])

    def __new__(cls,gfnum,val=None):
        if val is not None: val = val%gfnum
        obj = super().__new__(cls,val)
        if not cls.__gfnum: cls.__gfnum = gfnum
        if not cls.__inverse: cls.calculateInverses()
        return obj
    
    @__checkOperandsType
    def __add__(self,val):
        return type(self)(int.__add__(self,val)%self.gfnum)
            
    __iadd__ = __radd__ = __add__

    @__checkOperandsType
    def __sub__(self,val):
        return type(self)(int.__sub__(self,val)%self.gfnum)

    @__checkOperandsType
    def __rsub__(self,val):
        return type(self)(int.__rsub__(self,val)%self.gfnum)

    @__checkOperandsType
    def __mul__(self,val):
        return type(self)(int.__mul__(self,val)%self.gfnum)
    __imul__ = __rmul__ = __mul__

    @__checkOperandsType
    def __truediv__(self,val):
        if val == 0: raise ZeroDivisionError("division by zero")
        return self*type(self)(val).inverse
    @__checkOperandsType
    def __rtruediv__(self,val):
        if self == 0: raise ZeroDivisionError("division by zero")
        return type(val)*self.inverse

    def __repr__(self):
        return "gf{}({})".format(self.gfnum,int(self))
    
    def __str__(self):
        return self.__repr__()

class gf2(gf):
    def __new__(cls,val=None):
        obj = super().__new__(cls,2,val)
        return obj

class gf3(gf):
    def __new__(cls,val=None):
        obj = super().__new__(cls,3,val)
        return obj