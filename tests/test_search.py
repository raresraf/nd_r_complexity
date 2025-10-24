import pandas as pd
import pytest
from nd_r_complexity.model_search import find_best_model
from nd_r_complexity.search import NDBasisFunction
import tempfile
import os
from sklearn.metrics import mean_squared_error
import numpy as np


def test_model_search_knapsack(capsys):
    """Tests the find_best_model function with grid search and knapsack data."""
    data = {
        "n": [
            2500,
            2500,
            2500,
            2500,
            2500,
            2500,
            2500,
            2500,
            5000,
            5000,
            5000,
            5000,
            5000,
            5000,
            5000,
            5000,
            7500,
            7500,
            7500,
            7500,
            7500,
            7500,
            7500,
            7500,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            10000,
            12500,
            12500,
            12500,
            12500,
            12500,
            12500,
            12500,
            12500,
            15000,
            15000,
            15000,
            15000,
            15000,
            15000,
            15000,
            15000,
            17500,
            17500,
            17500,
            17500,
            17500,
            17500,
            17500,
            17500,
            20000,
            20000,
            20000,
            20000,
            20000,
            20000,
            20000,
            20000,
        ],
        "W": [
            2500,
            5000,
            7500,
            10000,
            12500,
            15000,
            17500,
            20000,
            2500,
            5000,
            7500,
            10000,
            12500,
            15000,
            17500,
            20000,
            2500,
            5000,
            7500,
            10000,
            12500,
            15000,
            17500,
            20000,
            2500,
            5000,
            7500,
            10000,
            12500,
            15000,
            17500,
            20000,
            2500,
            5000,
            7500,
            10000,
            12500,
            15000,
            17500,
            20000,
            2500,
            5000,
            7500,
            10000,
            12500,
            15000,
            17500,
            20000,
            2500,
            5000,
            7500,
            10000,
            12500,
            15000,
            17500,
            20000,
            2500,
            5000,
            7500,
            10000,
            12500,
            15000,
            17500,
            20000,
        ],
        "time_ms": [
            48.9010,
            92.7970,
            139.9630,
            203.9360,
            221.5770,
            258.6120,
            320.5740,
            328.1810,
            97.2550,
            188.1200,
            279.1970,
            406.1400,
            479.6660,
            577.0370,
            637.3480,
            750.3690,
            142.2620,
            281.9770,
            419.4900,
            576.7760,
            714.5260,
            823.3670,
            988.1020,
            1116.7110,
            189.0950,
            375.1150,
            561.3980,
            781.7830,
            968.0090,
            1119.5780,
            1341.5330,
            1540.0570,
            232.5560,
            466.7170,
            701.5510,
            972.0270,
            1227.8950,
            1452.2500,
            1728.8990,
            1935.0700,
            277.1650,
            570.4730,
            847.5410,
            1172.1750,
            1457.2540,
            1727.3870,
            2010.5060,
            2260.7020,
            322.8220,
            661.3950,
            975.4770,
            1336.8760,
            1694.5290,
            1986.1460,
            2318.9990,
            2639.5560,
            370.0470,
            747.8700,
            1117.0620,
            1506.6010,
            1897.6520,
            2255.8310,
            2743.8880,
            3039.6860,
        ],
    }
    df = pd.DataFrame(data)
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tmp_file:
        df.to_csv(tmp_file.name, index=False)
        temp_file_path = tmp_file.name

    try:
        model, basis_functions = find_best_model(
            temp_file_path, num_terms=1, p_values=[1], q_values=[0], X_values=[]
        )

        assert model is not None
        assert basis_functions is not None
        assert len(basis_functions) == 1
        best_func = basis_functions[0]
        assert isinstance(best_func, NDBasisFunction)
        assert len(best_func.funcs) == 2
        data = pd.read_csv(temp_file_path)
        X_data = data.iloc[:, :-1].values
        y_data = data.iloc[:, -1].values
        X_design = np.zeros((len(X_data), len(basis_functions)))
        for i, basis_func in enumerate(basis_functions):
            X_design[:, i] = basis_func(*X_data.T)
        y_pred = model.predict(X_design)
        error = mean_squared_error(y_data, y_pred)
        assert error < 500

        captured = capsys.readouterr()
        assert "Best combination of basis functions:\nn_1^1 * n_2^1" in captured.out

    finally:
        os.remove(temp_file_path)


def test_model_search_bfs(capsys):
    """Tests the find_best_model function with grid search and BFS data."""
    data = {
        "Vertices (V)": [
            1000000,
            1000000,
            1000000,
            1000000,
            1000000,
            2000000,
            2000000,
            2000000,
            2000000,
            2000000,
            3000000,
            3000000,
            3000000,
            3000000,
            3000000,
            4000000,
            4000000,
            4000000,
            4000000,
            4000000,
            5000000,
            5000000,
            5000000,
            5000000,
            5000000,
        ],
        "Edges (E)": [
            1000000,
            2000000,
            3000000,
            4000000,
            5000000,
            2000000,
            4000000,
            6000000,
            8000000,
            10000000,
            3000000,
            6000000,
            9000000,
            12000000,
            15000000,
            4000000,
            8000000,
            12000000,
            16000000,
            20000000,
            5000000,
            10000000,
            15000000,
            20000000,
            25000000,
        ],
        "Time (seconds)": [
            0.234274,
            0.403702,
            0.552781,
            0.747199,
            0.966431,
            0.006395,
            0.805063,
            1.215489,
            1.605980,
            2.089497,
            0.738303,
            1.338934,
            1.821428,
            2.484839,
            3.312580,
            1.020870,
            1.710339,
            2.522506,
            3.412965,
            4.435482,
            0.009743,
            2.197207,
            3.345080,
            4.339670,
            5.638347,
        ],
    }
    df = pd.DataFrame(data)
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tmp_file:
        df.to_csv(tmp_file.name, index=False)
        temp_file_path = tmp_file.name

    try:
        model, basis_functions = find_best_model(
            temp_file_path, num_terms=2, p_values=[1], q_values=[1, 2], X_values=[]
        )

        assert model is not None
        assert basis_functions is not None
        assert (
            len(basis_functions) == 2
        )
        best_func_1 = basis_functions[0]
        best_func_2 = basis_functions[1]
        assert isinstance(best_func_1, NDBasisFunction)
        assert isinstance(best_func_2, NDBasisFunction)

        # Each NDBasisFunction should have 2 funcs (for V and E)
        assert len(best_func_1.funcs) == 2
        assert len(best_func_2.funcs) == 2

        data = pd.read_csv(temp_file_path)
        X_data = data.iloc[:, :-1].values
        y_data = data.iloc[:, -1].values
        X_design = np.zeros((len(X_data), len(basis_functions)))
        for i, basis_func in enumerate(basis_functions):
            X_design[:, i] = basis_func(*X_data.T)
        y_pred = model.predict(X_design)
        error = mean_squared_error(y_data, y_pred)
        assert error < 10.0

    finally:
        os.remove(temp_file_path)
