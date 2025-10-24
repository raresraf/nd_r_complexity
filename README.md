# N-Dimensional R-Complexity

A Python package to approximate the big r-Theta complexity based on emphirical results.

## Installation

To install the package, navigate to the root directory of the project (where `pyproject.toml` is located) and run:

```bash
python3 -m pip install .
```

## Usage

### Manual Testing

You can manually test the package with the provided experimental datasets. Navigate to the root directory of the project and run the following commands:

**For `knapsack_data.csv` (Grid Search):**
```bash
python3 -m nd_r_complexity.main src/experimental/knapsack_data.csv
```

**For `bfs_data.csv` (Grid Search with specific parameters):**
```bash
python3 -m nd_r_complexity.main src/experimental/bfs_data.csv --num_terms 2 --p_values 1 --q_values 1 2
```

**For `knapsack_data.csv` (Random Search):**
```bash
python3 -m nd_r_complexity.main src/experimental/knapsack_data.csv --search_strategy random --num_samples 1000
```

### Running Unit Tests

To run the automated unit tests, navigate to the root directory of the project and execute:

```bash
python3 -m pytest
```
