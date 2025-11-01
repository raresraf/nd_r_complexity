import argparse
from nd_r_complexity.search import (
    generate_basis_function_combinations,
    count_basis_function_combinations,
)
from . import constants

def print_functions(
    num_dimensions, num_terms, p_values, q_values, X_values, total_only=False
):
    """Prints all the possible functions that will be iterated."""
    total_combinations = count_basis_function_combinations(
        num_dimensions, num_terms, p_values, q_values, X_values
    )

    print(f"\nTotal possible combinations: {total_combinations}")

    if total_only:
        return

    basis_combinations = generate_basis_function_combinations(
        num_dimensions, num_terms, p_values, q_values, X_values
    )

    for i, basis_combination in enumerate(basis_combinations):
        if i % 1000000 == 0 or i == 0 or i == total_combinations - 1:
            print(f"\n--- Combination {i} ---")
            print(" + ".join([str(func) for func in basis_combination]))


def main():
    """Main function to print the functions."""
    parser = argparse.ArgumentParser(
        description="Print all the possible functions that will be iterated."
    )
    parser.add_argument(
        "--num_dimensions",
        type=int,
        required=True,
        help="The number of dimensions of the input data.",
    )
    parser.add_argument(
        "--num_terms",
        type=int,
        default=constants.DEFAULT_NUM_TERMS,
        help="The number of terms in the complexity function.",
    )
    parser.add_argument(
        "--p_values",
        type=float,
        nargs="*",
        default=constants.DEFAULT_P_VALUES,
        help="A list of values for the exponents of the polynomial terms.",
    )
    parser.add_argument(
        "--q_values",
        type=float,
        nargs="*",
        default=constants.DEFAULT_Q_VALUES,
        help="A list of values for the exponents of the polylogarithmic terms.",
    )
    parser.add_argument(
        "--X_values",
        type=float,
        nargs="*",
        default=constants.DEFAULT_X_VALUES,
        help="A list of values for the base of the exponential terms.",
    )
    parser.add_argument(
        "--total_only",
        action="store_true",
        help="Only print the total number of combinations.",
    )
    args = parser.parse_args()

    print_functions(
        args.num_dimensions,
        args.num_terms,
        args.p_values,
        args.q_values,
        args.X_values,
        args.total_only,
    )


if __name__ == "__main__":
    main()
