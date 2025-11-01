import itertools
import random
import numpy as np
from scipy.special import gamma


# 1-D Basis Functions
class BasisFunction:
    def __init__(self, name_template):
        self.name_template = name_template

    def __call__(self, n):
        raise NotImplementedError

    def __str__(self, dimension_index=None):
        if dimension_index is not None:
            return self.name_template.replace("n", f"n_{dimension_index+1}")
        return self.name_template


class Polynomial(BasisFunction):
    def __init__(self, p):
        super().__init__(f"n^{p}")
        self.p = p

    def __call__(self, n):
        return n**self.p


class Polylog(BasisFunction):
    def __init__(self, q):
        super().__init__(f"log(n)^{q}")
        self.q = q

    def __call__(self, n):
        # Avoid log(0)
        return np.log(n + 1e-9) ** self.q


class Exponential(BasisFunction):
    def __init__(self, X):
        super().__init__(f"{X}^n")
        self.X = X

    def __call__(self, n):
        return self.X**n


class Factorial(BasisFunction):
    def __init__(self):
        super().__init__("Gamma(n)")

    def __call__(self, n):
        return gamma(n + 1)


class MixedBasisFunction(BasisFunction):
    def __init__(self, funcs):
        self.funcs = funcs
        name_template = " * ".join([str(f) for f in funcs])
        super().__init__(name_template)

    def __call__(self, n):
        res = np.ones_like(n, dtype=np.float64)
        for f in self.funcs:
            term = f(n)
            if np.any(np.isnan(term)) or np.any(np.isinf(term)):
                return np.full_like(res, np.nan)
            res *= term
            if np.any(np.isnan(res)) or np.any(np.isinf(res)):
                return np.full_like(res, np.nan)
        return res


# N-Dimensional Basis Functions
class NDBasisFunction:
    def __init__(self, funcs):
        self.funcs = funcs

    def __call__(self, *args):
        res = np.ones_like(args[0], dtype=np.float64)
        for i, arg in enumerate(args):
            term = self.funcs[i](arg)
            if np.any(np.isnan(term)) or np.any(np.isinf(term)):
                return np.full_like(res, np.nan)
            res *= term
            if np.any(np.isnan(res)) or np.any(np.isinf(res)):
                return np.full_like(res, np.nan)
        return res

    def __str__(self):

        return " * ".join(
            [self.funcs[i].__str__(dimension_index=i) for i in range(len(self.funcs))]
        )


def generate_1d_basis_functions(p_values, q_values, X_values):
    """Generates a list of 1D basis functions, including mixed terms."""
    elementary_functions = []
    for p in p_values:
        elementary_functions.append(Polynomial(p))
    for q in q_values:
        elementary_functions.append(Polylog(q))
    for X in X_values:
        elementary_functions.append(Exponential(X))
    elementary_functions.append(Factorial())

    # Start with elementary functions
    for f in elementary_functions:
        yield f

    # Add mixed functions (combinations of two distinct elementary functions)
    for f1, f2 in itertools.combinations(elementary_functions, 2):
        yield MixedBasisFunction([f1, f2])


def generate_nd_basis_functions(num_dimensions, p_values, q_values, X_values):
    """Generates all combinations of n-dimensional basis functions."""
    one_d_funcs = list(generate_1d_basis_functions(p_values, q_values, X_values))
    nd_combinations = itertools.product(one_d_funcs, repeat=num_dimensions)
    for combo in nd_combinations:
        yield NDBasisFunction(list(combo))



def n_choose_k(n, k):
    """Calculates the number of combinations (n choose k)."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k

    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


def count_1d_basis_functions(p_values, q_values, X_values):
    """Calculates the number of 1D basis functions."""
    num_elementary = len(p_values) + len(q_values) + len(X_values) + 1
    return num_elementary + n_choose_k(num_elementary, 2)


def count_nd_basis_functions(num_dimensions, p_values, q_values, X_values):
    """Calculates the number of n-dimensional basis funcpythtions."""
    return count_1d_basis_functions(p_values, q_values, X_values) ** num_dimensions


def count_basis_function_combinations(
    num_dimensions, num_terms, p_values, q_values, X_values
):
    """Calculates the number of combinations of basis functions."""
    return n_choose_k(
        count_nd_basis_functions(num_dimensions, p_values, q_values, X_values),
        num_terms,
    )


def generate_basis_function_combinations(
    num_dimensions, num_terms, p_values, q_values, X_values
):
    """Generates all combinations of basis functions."""
    nd_basis_functions = generate_nd_basis_functions(
        num_dimensions, p_values, q_values, X_values
    )
    return itertools.combinations(nd_basis_functions, num_terms)


def generate_random_basis_function_combinations(
    num_dimensions, num_terms, p_values, q_values, X_values, num_samples
):
    basis_functions = generate_nd_basis_functions(
        num_dimensions, p_values, q_values, X_values
    )

    basis_function_combinations = []
    for _ in range(num_samples):
        num_selected_terms = random.randint(1, num_terms)
        basis_function_combinations.append(
            tuple(random.sample(basis_functions, num_selected_terms))
        )

    return basis_function_combinations
