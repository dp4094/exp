from charm.toolbox.pairinggroup import PairingGroup, G1, G2, GT, ZR, pair
import time
import random
import math

# 自定义整数模 n 的环 Zn
class Zn:
    def __init__(self, value, n):
        self.n = n
        self.value = value % n

    def __add__(self, other):
        return Zn((self.value + other.value) % self.n, self.n)

    def __mul__(self, other):
        return Zn((self.value * other.value) % self.n, self.n)

    def __pow__(self, exponent):
        e = exponent.value if isinstance(exponent, Zn) else exponent
        return Zn(pow(self.value, e, self.n), self.n)

    def inverse(self):
        def egcd(a, b):
            if a == 0:
                return b, 0, 1
            g, y, x = egcd(b % a, a)
            return g, x - (b // a) * y, y
        g, x, _ = egcd(self.value, self.n)
        if g != 1:
            raise ValueError("No inverse exists.")
        return Zn(x % self.n, self.n)


# 初始化 pairing group
group = PairingGroup('MNT224')

zR = group.random(ZR)
P = group.random(G1)
Q = group.random(G2)
T = group.random(G1)

p = group.serialize(P)
sp = str(p)

n = 100  # 外部迭代轮数（统计用）
bulk = 100  # 每轮模运算执行次数

# 初始化计时器
pa = sm = bp = ge = gm = hG = hZR = ra = rm = re = 0
mod_add = mod_mul = mod_pow = mod_inv = 0
pair_add = pair_mul = 0

mod_n = 104729  # 一个大素数

for i in range(n):
    # 椭圆曲线与配对操作
    t1 = time.perf_counter()
    P * T
    t2 = time.perf_counter()
    P ** zR
    t3 = time.perf_counter()
    gtt = pair(P, Q)
    t4 = time.perf_counter()
    gtt ** zR
    t5 = time.perf_counter()
    gtt * gtt
    t6 = time.perf_counter()
    group.hash(zR, G1)
    t7 = time.perf_counter()
    group.hash(sp, ZR)
    t8 = time.perf_counter()
    zR + zR
    t9 = time.perf_counter()
    zR * zR
    t10 = time.perf_counter()
    zR ** zR
    t11 = time.perf_counter()

    # 模环运算（Zn）
    a = Zn(random.randint(1, mod_n - 1), mod_n)
    b = Zn(random.randint(1, mod_n - 1), mod_n)
    exp = random.randint(1, 1000)

    # 模加法（批量）
    start = ti