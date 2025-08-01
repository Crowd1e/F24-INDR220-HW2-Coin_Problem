# F24-INDR220-HW2-Coin_Problem

This project solves the Coin Distribution Problem using Integer Linear Programming (ILP) and CPLEX.

A parent tries to distribute N coins to M children such that each child gets coins summing up to the same total value. The goal is to find an optimal assignment using binary decision variables.

## 📄 Input:
	•	coins.txt: A single-row file with coin values.
	•	Number of children (M).

## 🧠 Formulation:
	•	Each coin must be assigned to exactly one child.
	•	Each child must receive coins summing up to the same total value.
	•	Solved via ILP with binary variables xij ∈ {0,1}.

## 🛠 Implementation:
	•	Python function: coin_distribution_problem(coins_file, M)
	•	Solver: IBM CPLEX
	•	Environment: Azure Lab Services

📌 Note: Only partitions with equal total coin value are considered feasible.
