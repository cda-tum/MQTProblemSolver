[![Lint](https://github.com/nquetschlich/MQTProblemSolver/actions/workflows/linter.yml/badge.svg)](https://github.com/nquetschlich/MQTProblemSolver/actions/workflows/linter.yml)
[![CodeCov](https://github.com/nquetschlich/MQTProblemSolver/actions/workflows/coverage.yml/badge.svg)](https://github.com/nquetschlich/MQTProblemSolver/actions/workflows/coverage.yml)

# MQT ProblemSolver

MQT ProblemSolver is a framework to utilize quantum computing as a technology for users with little to no
quantum computing knowledge.
All necessary quantum parts are embedded by domain experts while the interface provided are similar to the ones
classical solver provide:

<p align="center">
<img src="img/framework.png" height=300px>
</p>

When provided with a problem description, MQT ProblemSolver offers a selection of implemented quantum algorithms.
The user just has to chose one and all further (quantum) calculation steps are encapsulated within MQT ProblemSolver.
After the calculation finished, the respective solution is returned - again in the same format as classical
solvers use.

In the current implementation, two case studies are conducted:

1. A SAT Problem: Constraint Satisfaction Problem
2. A Graph-based Optimization Problem: Travelling Salesman Problem

# A SAT Problem: Constraint Satisfaction Problem

This exemplary implementation can be found in the [CSP_example.ipynb](src/mqt/problemsolver/CSP_example.ipynb).
Here, the solution to a Kakuro riddle with a 2x2 can be solved for arbitrary sums `s0` to `s3`:

<p align="center">
<img src="img/kakuro.png" height=200px>
</p>

MQT ProblemSolver will return valid values to `a`, `b`, `c`, and `d` if a solution exists.

# A Graph-based Optimization Problem: Travelling Salesman Problem

This exemplary implementation can be found in the [TSP_example.ipynb](src/mqt/problemsolver/TSP_example.ipynb).
Here, the solution to a Travelling Salesman Problem with 4 cities can be solved for arbitrary distances `dist_1_2` to `dist_3_4`between the cities.

<p align="center">
<img src="img/tsp.png" height=200px>
</p>

MQT ProblemSolver will return the shortest path visiting all cities.

# Repository Structure

```
.
├── src
│ └── mqt
│     └── problemsolver
│        └── sat.py
│        └── sat_example.ipynb
│        └── graph.py
│        └── graph.ipynb
└── tests
    └── ...
```

# Reference

In case you are using MQT ProblemSolver in your work, we would be thankful if you referred to it by citing the following publication:

```bibtex
@misc{xxx,
  title={xxx},
  author={Quetschlich, Nils and Burgholzer, Lukas and Wille, Robert},
  year={2022},
}
```
