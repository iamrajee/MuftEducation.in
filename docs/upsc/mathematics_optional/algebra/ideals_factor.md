---
id: ideals_factor
title: Ideals and Factor Rings
sidebar_label: Ideals and Factor Rings
---

## Ideal

A subring $A$ of a ring $R$ is called a (two-sided) ideal of $R$ if for every $r \in R$ and every $a \in A$ both $ra$ and $ar$ are in $A$.

---

* So, a subring $A$ of a ring $R$ is an ideal of $R$ if $A$ "absorbs" elements from $R$—that is, if $rA \subseteq A$ and $Ar \subseteq A$ for all $r \in R$.

* An ideal $A$ of $R$ is called a proper ideal of $R$ if $A$ is a proper subset of $R$. 

*  If $A$ is an ideal of a ring $R$ and 1 belongs to $A$, then $A = R$.

## Theorem 13.1

A nonempty subset $A$ of a ring $R$ is an ideal of $R$ if

1. $a - b \in A$ whenever $a, b \in A$.
2. $ra$ and $ar$ are in $A$ whenever $a \in A$ and $r \in R$.

**Examples:**

*  For any ring $R, \\{0\\}$ and $R$ are ideals of $R$. The ideal $\\{0\\}$ is called the trivial ideal.

* For any positive integer $n$, the set $nZ = \\{0, \pm n, \pm 2n, . . .\\}$ is an ideal of $Z$.

* Let $R$ be a commutative ring with unity and let $a \in R$. The set $\langle a \rangle = \\{ra \mid r \in R\\}$ is an ideal of $R$ called the principal ideal generated by $a$. 

* Let $R[x]$ denote the set of all polynomials with real coefficients and let $A$ denote the subset of all polynomials with constant term 0. Then $A$ is an ideal of $R[x]$ and $A = \langle x \rangle$.

* Let $R$ be a commutative ring with unity and let $a_1, a_2, . . . , a_n$ belong to $R$. Then $I = \langle a_1, a_2, . . . , a_n \rangle = \\{r_1a_1 + r_2a_2 + \cdots + r_na_n \mid r_i \in R\\}$ is an ideal of $R$ called the ideal generated by $a_1, a_2, . . . , a_n$. 

* Let $Z[x]$ denote the ring of all polynomials with integer coefficients and let $I$ be the subset of $Z[x]$ of all polynomials with even constant terms. Then $I$ is an ideal of $Z[x]$ and $I = \langle x, 2 \rangle$.

## Theorem 13.2 (Existence of Factor Rings)

Let $R$ be a ring and let $A$ be a subring of $R$. The set of cosets $\\{r + A \mid r \in R\\}$ is a ring under the operations $(s + A) + (t + A) = s + t + A$ and $(s + A)(t + A) = st + A$ if and only if $A$ is an ideal of $R$.

**Proof:** We know that the set of cosets forms a group under addition.
Once we know that multiplication is indeed a binary operation on the
cosets, it is trivial to check that the multiplication is associative and
that multiplication is distributive over addition. Hence, the proof boils
down to showing that multiplication is well-defined if and only if $A$ is
an ideal of $R$. To do this, let us suppose that $A$ is an ideal and let $s + A = s' + A$ and $t + A = t' + A$. Then we must show that $st + A = s't' + A$.
Well, by definition, $s = s' + a$ and $t = t' + b$, where $a$ and $b$ belong
to $A$. Then and so $st = (s' + a)(t' + b) = s't' + at' + s'b + ab$ (thus $st \in s't' + A$, alternatively),

$st + A = s't' + at' + s'b + ab + A = s't' + A$, since $A$ absorbs $at' + s'b + ab$. Thus, multiplication is well-defined when $A$ is an ideal.

On the other hand, suppose that $A$ is a subring of $R$ that is not an
ideal of $R$. Then there exist elements $a \in A$ and $r \in R$ such that $ar \not \in A$ or $ra \not \in A$. For convenience, say $ar \not \in A$. Consider the elements $a + A = 0 + A$ and $r + A$. Clearly, $(a + A)(r + A) = ar + A$ but $(0 + A)(r + A) = 0r + A = A.$ Since $ar + A \neq A$, the multiplication is not
well-defined and the set of cosets is not a ring.

**Examples:**

* $2Z/6Z = \\{0 + 6Z, 2 + 6Z, 4 + 6Z\\}$. Here the operations are essentially modulo 6 arithmetic. For example, $(4 + 6Z) + (4 + 6Z) = 2 + 6Z$ and $(4 + 6Z)(4 + 6Z) = 4 + 6Z$.

* Let $R = \\{\begin{bmatrix} a_1 & a_2 \\\ a_3 & a_4 \end{bmatrix} \mid a_i \in Z \\}$  and let $I$ be the subset of $R$ consisting of matrices with even entries. It is easy to show that $I$ is indeed an ideal of $R$. Consider the factor ring $R/I.$ The interesting question about this ring is: What is its size? We claim $R/I$ has 16 elements; in fact, $R/I = \\{ \begin{bmatrix} r_1 & r_2 \\\ r_3 & r_4 \end{bmatrix} + I \mid r_i \in \\{0, 1\\} \\}$ 

* Consider the factor ring of the Gaussian integers $R = Z[i]/\langle 2 - i \rangle.$ (*Note:* $(a + bi)(2 - i)$ doesn't cover the complete $Z[i]$ as $a, b$ have to be integers) What does this ring look like? Of course, the elements of $R$ have the form $a + bi + \langle 2 - i \rangle$, where $a$ and $b$ are integers, but the important question is: What do the distinct cosets look like? The fact that $2 - i + \langle 2 - i \rangle = 0 + \langle 2 - i \rangle$ means that when dealing with coset representatives, we may treat $2 - i$ as equivalent to 0, so that $2 = i$. For example, the coset $3 + 4i + \langle 2 - i \rangle = 3 + 8 + \langle 2 - i \rangle = 11 + \langle 2 - i \rangle.$ (or $4i = 4i - 8 + 8$) Similarly, all the elements of $R$ can be written in the form $a + \langle 2 - i \rangle$, where $a$ is an integer. But we can further reduce the set of distinct coset representatives by observing that when dealing with coset representatives, $2 = i$ implies (by squaring both sides) that $4 = -1$ or $5 = 0$ (actually $(2 + i)(2 - i) = 5$). Thus, the coset $3 + 4i + \langle 2 - i \rangle =$ $11 + \langle 2 - i \rangle = 1 + 5 + 5 + \langle 2 - i \rangle$ $= 1 + \langle 2 - i \rangle$. In this way, we can show that every element of $R$ is equal to one of the following cosets: $0 + \langle 2 - i \rangle, 1 + \langle 2 - i \rangle, 2 + \langle 2 - i \rangle, 3 + \langle 2 - i\rangle, 4 + \langle 2 - i \rangle$. Is any further reduction possible? To demonstrate that there is not, we will show that these five cosets are distinct. It suffices to show that $1 + \langle 2 - i \rangle$ has additive order 5. Since $5(1 + \langle 2 - i \rangle) = 5 + \langle 2 - i\rangle = 0 + \langle 2 - i \rangle, 1 + \langle 2 - i \rangle$ has order 1 or 5. If the order is actually 1, then $1 + \langle 2 - i \rangle = 0 + \langle 2 - i \rangle$, so $1 \in \langle 2 - i \rangle$ (which can be verified to be impossible). It should be clear that the ring $R$ is essentially the same as the field $Z_5$.

*  Let $R[x]$ denote the ring of polynomials with real coefficients. Since, $\langle x^2 + 1\rangle = \\{f(x)(x^2 + 1) \mid f(x) \in R[x]\\}$. Then $R[x]/\langle x^2 + 1\rangle$ = $\\{g(x) + \langle x^2 + 1\rangle \mid g(x) \in R[x]\\}$ = $\\{ax + b + \langle x^2 + 1 \rangle \mid a, b \in R\\}$. To see this last equality, note that if $g(x)$ is any member of $R[x]$, then we may write $g(x)$ in the form $q(x)(x^2 + 1) + r(x)$ 

How is multiplication done? Since $x^2 + 1 + \langle x^2 + 1\rangle = 0 + \langle x^2 + 1\rangle$, one should think of $x^2 + 1$ as 0 or, equivalently, as $x^2 = -1$. So, for example, $(x + 3 + \langle x^2 + 1\rangle)(2x + 5 + \langle x^2 + 1 \rangle)$ = $2x^2 + 11x + 15 + \langle x^2 + 1\rangle$ = $11x + 13 + \langle x^2 + 1\rangle$ . In view of the fact that the elements of this ring have the form $ax + b + \langle x^2 + 1\rangle$, where $x^2 + \langle x^2 + 1\rangle = -1 + \langle x^2 + 1\rangle$, it is perhaps not surprising that this ring turns out to be algebraically the same ring as the ring of complex numbers.

## Prime Ideals and Maximal Ideals

A prime ideal $A$ of a commutative ring $R$ is a proper ideal of $R$ such
that $a, b \in R$ and $ab \in A$ imply $a \in A$ or $b \in A$. A maximal ideal of a commutative ring $R$ is a proper ideal $A$ of $R$ such that, whenever $B$ is an
ideal of $R$ and $A \subseteq B \subseteq R$, then $B = A$ or $B = R$.

**Examples:**

* Let $n$ be an integer greater than 1. Then, in the ring of integers, the ideal $nZ$ is prime if and only if $n$ is prime. ($\\{0\\}$ is also a prime ideal of $Z$.)

* The ideal $\langle x^2 + 1\rangle$ is maximal in $R[x]$. To see this, assume that $A$ is an ideal of $R[x]$ that properly contains $\langle x^2 + 1\rangle$. We will prove that $A = R[x]$ by showing that $A$ contains some nonzero real number $c$. Then $1 = (1/c)c \in A$ and therefore, $A = R[x]$. To this end, let $f(x) \in A,$ but $f(x) \not \in \langle x^2 + 1\rangle.$ Then $f(x) = q(x)(x^2 + 1) + r(x),$ where $r(x) \neq 0$ and the degree of $r(x)$ is less than 2. It follows that $r(x) = ax + b,$ where $a$ and $b$ are not both 0, and $ax + b = r(x) = f(x) - q(x)(x^2 + 1) \in A$. Thus, $a^2x^2 - b^2 = (ax + b)(ax - b) \in A$  and  $a^2(x^2 + 1) \in A.$ So, $0 \neq a^2 + b^2 = (a^2x^2 + a^2) - (a^2x^2 - b^2) \in A$.

* The ideal $\langle x^2 + 1\rangle$ is not prime in $Z_2[x]$, since it contains $(x + 1)^2 = x^2 + 2x + 1 = x^2 + 1$ but does not contain $x + 1$.

### Theorem 13.3

Let $R$ be a commutative ring with unity and let $A$ be an ideal of $R$.
Then $R/A$ is an integral domain if and only if $A$ is prime. (easy to prove)

**Proof:** 

Suppose that $R/A$ is an integral domain and $ab \in A$. Then
$(a + A)(b + A) = ab + A = A$, the zero element of the ring $R/A$. So,
either $a + A = A$ or $b + A = A$; that is, either $a \in A$ or $b \in A$. Hence,
$A$ is prime.

To prove the other half of the theorem, we first observe that $R/A$ is a
commutative ring with unity for any proper ideal $A$. Thus, our task is
simply to show that when $A$ is prime, $R/A$ has no zero-divisors. So, suppose that $A$ is prime and $(a + A)(b + A) = 0 + A = A$. Then $ab \in A$ and, therefore, $a \in A$ or $b \in A$. Thus, one of $a + A$ or $b + A$ is the zero coset in $R/A$.

### Theorem 13.4

Let $R$ be a commutative ring with unity and let $A$ be an ideal of $R$.
Then $R/A$ is a field if and only if $A$ is maximal.

**Proof:** 

Suppose that $R/A$ is a field and $B$ is an ideal of $R$ that properly
contains $A$. Let $b \in B$ but $b \not \in A$. Then $b + A$ is a nonzero element
of $R/A$ and, therefore, there exists an element $c + A$ such that
$(b + A)(c + A) = 1 + A$, the multiplicative identity of $R/A$. Since
$b \in B$, we have $bc \in B$. Because $1 + A = (b + A)(c + A) = bc + A$,

we have $1 - bc \in A \subset B$. So, $1 = (1 - bc) + bc \in B$. Thus,
$B = R$. This proves that $A$ is maximal.

Now suppose that $A$ is maximal and let $b \in R$ but $b \not \in A$. It suffices
to show that $b + A$ has a multiplicative inverse. (All other properties
for a field follow trivially.) Consider $B = \\{br + a \mid r \in R, a \in A\\}$. This
is an ideal of $R$ that properly contains $A$ (easy to see). Since $A$ is maximal, we must have $B = R$. Thus, $1 \in B$, say, $1 = bc + a'$, where $a' \in A$. Then $1 + A = bc + a' + A = bc + A = (b + A)(c + A)$.

---

When a commutative ring has a unity, it follows from Theorems
13.3 and 13.4 that a maximal ideal is a prime ideal. The next example
shows that a prime ideal need not be maximal.

**Examples:** 

* The ideal $\langle x \rangle$ is a prime ideal in $Z[x]$ but not a maximal ideal in $Z[x]$. To verify this, we begin with the observation that $\langle x\rangle = \\{f(x) \in Z[x] \mid f(0) = 0\\}$ . Thus, if $g(x)h(x) \in \langle x\rangle$, then $g(0)h(0) = 0.$ And since $g(0)$ and $h(0)$ are integers, we have $g(0) = 0$ or $h(0) = 0$. To see that $\langle x\rangle$ is not maximal, we simply note that $\langle x\rangle \subset \langle x, 2\rangle \subset Z[x]$ 











