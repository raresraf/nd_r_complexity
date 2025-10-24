import argparse
from nd_r_complexity.model_search import find_best_model
from nd_r_complexity import constants


def main():
    """Main function to run the grid search."""
    parser = argparse.ArgumentParser(
        description="Find the best complexity model for a given dataset."
    )
    parser.add_argument("data_path", help="Path to the CSV data file.")
    parser.add_argument(
        "--num_threads",
        type=int,
        default=4,
        help="Number of threads to use for parallel processing.",
    )
    parser.add_argument(
        "--search_strategy",
        type=str,
        default="grid",
        help="Search strategy to use ('grid' or 'random').",
    )
    parser.add_argument(
        "--num_samples",
        type=int,
        default=100,
        help="Number of samples to use for random search.",
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
        help="A list of values for the exponents of the polynomial terms (e.g., 1 2 3).",
    )
    parser.add_argument(
        "--q_values",
        type=float,
        nargs="*",
        default=constants.DEFAULT_Q_VALUES,
        help="A list of values for the exponents of the polylogarithmic terms (e.g., 1 2).",
    )
    parser.add_argument(
        "--X_values",
        type=float,
        nargs="*",
        default=constants.DEFAULT_X_VALUES,
        help="A list of values for the base of the exponential terms (e.g., 2 10).",
    )
    args = parser.parse_args()
    find_best_model(
        args.data_path,
        num_threads=args.num_threads,
        search_strategy=args.search_strategy,
        num_samples=args.num_samples,
        num_terms=args.num_terms,
        p_values=args.p_values,
        q_values=args.q_values,
        X_values=args.X_values,
    )


if __name__ == "__main__":
    main()
