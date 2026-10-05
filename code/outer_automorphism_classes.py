"""
Class action of the outer automorphism of 2I = SL(2,5) and of the central lift g -> -g.

Written for AOG 1.8 (not vendored from another repository).  Standard library only.

Question answered (exactly, by enumeration of the 120 matrices over F_5):
  (1) which permutation of the nine conjugacy classes is induced by the outer automorphism
      of SL(2,5), realised as conjugation by diag(2,1) in GL(2,5)?
  (2) does it fix the order-4 class, and does it map the order-5 locus (5a u 5b) and the
      order-10 locus (10a u 10b) to themselves?
  (3) which permutation of the classes is induced by g -> -g (the central lift)?

What this does and does not show: it determines the class permutations only.  It says nothing
about which locus a selection principle "should" pick; in particular, since both candidate loci
(order-4 versus order-5/10) are invariant under the outer automorphism, a map of that type is not
needed to choose between loci, only to tell the two classes within a locus (5a from 5b, 2 from 2').
"""

from itertools import product

P = 5
I2 = (1, 0, 0, 1)


def mul(a, b):
    return ((a[0] * b[0] + a[1] * b[2]) % P, (a[0] * b[1] + a[1] * b[3]) % P,
            (a[2] * b[0] + a[3] * b[2]) % P, (a[2] * b[1] + a[3] * b[3]) % P)


def det(a):
    return (a[0] * a[3] - a[1] * a[2]) % P


def inv(a):
    d = pow(det(a), -1, P)
    return ((a[3] * d) % P, (-a[1] * d) % P, (-a[2] * d) % P, (a[0] * d) % P)


def order(g):
    x, k = g, 1
    while x != I2:
        x, k = mul(x, g), k + 1
    return k


G = [m for m in product(range(P), repeat=4) if det(m) == 1]
assert len(G) == 120

# conjugacy classes inside SL(2,5)
cls_of = {}
classes = []
for g in G:
    if g in cls_of:
        continue
    orb = {mul(mul(h, g), inv(h)) for h in G}
    for x in orb:
        cls_of[x] = len(classes)
    classes.append(sorted(orb))

# name classes by (order, index among classes of equal order); 5a/5b are the two classes of order 5
# (the labelling of a versus b is a convention); the order-10 classes are then named by 10x := -(5x), below
names = {}
count = {}
for c in classes:
    count[order(c[0])] = count.get(order(c[0]), 0) + 1
tmp = {}
for c in sorted(classes, key=lambda c: (order(c[0]), c)):
    o = order(c[0])
    tmp[o] = tmp.get(o, 0) + 1
    names[cls_of[c[0]]] = f"{o}" if count[o] == 1 else f"{o}{'ab'[tmp[o] - 1]}"

# convention (fixed once, as in the note's appendix table): 10a := -(5a) and 10b := -(5b), so that the
# central lift g -> -g exchanges 5a <-> 10a and 5b <-> 10b by definition of the labels.
neg0 = lambda g: tuple((-x) % P for x in g)
for c in classes:
    if order(c[0]) == 10:
        src = cls_of[neg0(c[0])]
        assert order(classes[src][0]) == 5
        names[cls_of[c[0]]] = "10" + names[src][-1]

print("classes (name: size):", {names[i]: len(classes[i]) for i in sorted(names, key=lambda i: (order(classes[i][0]), names[i]))})

# outer automorphism: conjugation by diag(2,1) in GL(2,5) (det 2 is a non-square mod 5)
D = (2, 0, 0, 1)
phi = lambda g: mul(mul(D, g), inv(D))
assert all(det(phi(g)) == 1 for g in G)
assert all(phi(mul(a, b)) == mul(phi(a), phi(b)) for a in G[:20] for b in G)
assert sorted(phi(g) for g in G) == sorted(G)
assert any(phi(g) != g for g in G)

perm_out = {}
for ci, c in enumerate(classes):
    imgs = {cls_of[phi(g)] for g in c}
    assert len(imgs) == 1
    perm_out[ci] = imgs.pop()
print("\nouter automorphism (conjugation by diag(2,1)) on classes:")
for ci in sorted(perm_out, key=lambda i: (order(classes[i][0]), names[i])):
    print(f"  {names[ci]:>4} -> {names[perm_out[ci]]}")

# is it inner?  (inner <=> trivial on classes is necessary; check it is not trivial)
inner_on_classes = all(perm_out[c] == c for c in perm_out)
print("trivial on classes (necessary for inner):", inner_on_classes)

order4 = [c for c in classes if order(c[0]) == 4]
assert len(order4) == 1
c4 = cls_of[order4[0][0]]
loc5 = {c for c in perm_out if order(classes[c][0]) == 5}
loc10 = {c for c in perm_out if order(classes[c][0]) == 10}
print("order-4 class fixed:", perm_out[c4] == c4)
print("order-5 locus {5a,5b} mapped onto itself:", {perm_out[c] for c in loc5} == loc5,
      "; swaps 5a <-> 5b:", all(perm_out[c] != c for c in loc5))
print("order-10 locus {10a,10b} mapped onto itself:", {perm_out[c] for c in loc10} == loc10,
      "; swaps 10a <-> 10b:", all(perm_out[c] != c for c in loc10))

# central lift g -> -g
neg = lambda g: tuple((-x) % P for x in g)
perm_neg = {}
for ci, c in enumerate(classes):
    imgs = {cls_of[neg(g)] for g in c}
    assert len(imgs) == 1
    perm_neg[ci] = imgs.pop()
print("\ncentral lift g -> -g on classes:")
for ci in sorted(perm_neg, key=lambda i: (order(classes[i][0]), names[i])):
    print(f"  {names[ci]:>4} -> {names[perm_neg[ci]]}")
print("order-4 class fixed by g -> -g:", perm_neg[c4] == c4)

print("\nSUMMARY")
print("- the outer automorphism fixes the order-4 class and preserves each of the order-5 and order-10 loci,")
print("  exchanging the two classes inside each (5a<->5b, 10a<->10b);")
print("- hence both candidate loci are invariant under it: the Galois action is not, by itself, a map")
print("  between the order-4 locus and the order-5/10 locus; no link between the gate and this action is shown here.")
