### Algebraic Manipulation and Function Composition with Complex Numbers
Let $p^2(z) = z^2 + 6z +1$ and $\phi(z) = z + 3$. Compute $f = \phi \circ \phi^{-1}$ and use it to calculate $p^2(\sqrt{2i+5}-3)$.

We are using $\phi$ instead of directly calculating $p^2$ to simplify the computation.

### Solution
#### Step 1: Inverse of $\phi$

$$\phi(z) = z + 3$$
$$\phi^{-1}(z) = z - 3$$

#### Step 2: Composite Function $f = \phi \circ p \circ \phi^{-1}$

$$f(z) = \phi(p(\phi^{-1}(z)))$$

Substitute $\phi^{-1}(z)$
$$f(z) = \phi(p(z - 3))$$

Substitute $p(z)$
$$f(z) = \phi((z - 3)^2 + 6(z - 3) + 1)$$
$$= \phi(z^2 - 6z + 9 + 6z - 18 + 1)$$
$$= \phi(z^2 - 8)$$

Substitute $\phi(z)$
$$f(z) = z^2 - 5$$

#### Step 3: Calculating $p^2(\sqrt{2i+5}-3)$

Since $p^n(z) = \phi^{-1} \circ f^n \circ \phi(z)$ we can calculate $p^n(z)$ as $f^n(\phi(z))$.

$$p^2(\sqrt{2i+5}-3) = f^2(\sqrt{2i+5}-3+3)-3$$
$$= f^2(\sqrt{2i+5})-3$$

And $f^2(\sqrt{2i+5})$ is just $f(f(\sqrt{2i+5}))$.
$$f(\sqrt{2i+5}) = (\sqrt{2i+5})^2 - 5$$
$$= 2i + 5 - 5$$
$$= 2i$$

So
$$f^2(\sqrt{2i+5}) = f(2i)$$
$$= (2i)^2 - 5$$
$$= -4 - 5$$
$$= -9$$

And finally
$$p^2(\sqrt{2i+5}-3) = -9 - 3$$
$$= -12$$

### Code
```python
import numpy as np

def phi(z):
    return z + 3

def phi_inv(z):
    return z - 3

def f(z):
    return z**2 - 5

def p(z):
    return phi_inv(f(phi(z)))

def p2(z):
    return p(p(z))

print(p2(np.sqrt(2j + 5) - 3))
```

### Output
```
(-12+0j)
```