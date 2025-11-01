import itertools
import numpy as np
from . import constants
from scipy.special import gamma
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from .loader import load_data
from joblib import Parallel, delayed
from tqdm import tqdm
from .search import (
    generate_basis_function_combinations,
    generate_random_basis_function_combinations,
)


def fit_model(basis_combination, X_data, y_data):
    X_design = np.zeros((len(X_data), len(basis_combination)))
    for i, basis_func in enumerate(basis_combination):
        X_design[:, i] = basis_func(*X_data.T)

    model = LinearRegression()
    try:
        model.fit(X_design, y_data)
        y_pred = model.predict(X_design)
        error = mean_squared_error(y_data, y_pred)
        return error, model, basis_combination
    except ValueError as e:
        if "Input X contains infinity or a value too large" in str(
            e
        ) or "Input X contains NaN" in str(e):
            return float("inf"), None, None
        else:
            raise e


def find_best_model(
    data_path,
    num_terms,
    p_values,
    q_values,
    X_values,
    num_threads=4,
    search_strategy="grid",
    num_samples=100,
):
    """Performs a search to find the best model."""
    data = load_data(data_path)
    X_data = data.iloc[:, :-1].values
    y_data = data.iloc[:, -1].values
    num_dimensions = X_data.shape[1]

    if search_strategy == "grid":
        basis_combinations = generate_basis_function_combinations(
            num_dimensions, num_terms, p_values, q_values, X_values
        )
    elif search_strategy == "random":
        basis_combinations = generate_random_basis_function_combinations(
            num_dimensions, num_terms, p_values, q_values, X_values, num_samples
        )
    else:
        raise ValueError("Invalid search strategy. Choose 'grid' or 'random'.")

    results = Parallel(n_jobs=num_threads)(
        delayed(fit_model)(basis_combination, X_data, y_data)
        for basis_combination in tqdm(basis_combinations)
    )

    best_error = float("inf")
    best_model = None
    best_basis_functions = None

    for error, model, basis_functions in results:
        if error < best_error:
            best_error = error
            best_model = model
            best_basis_functions = basis_functions

    print("Best combination of basis functions:")
    print(" + ".join([str(func) for func in best_basis_functions]))
    print(f"Best model coefficients: {best_model.coef_}")
    print(f"Best model intercept: {best_model.intercept_}")
    print(f"Mean squared error: {best_error}")

    return best_model, best_basis_functions
