# load libraries
import numpy as np
import scipy.sparse as sp

import cplex as cp

def mixed_integer_linear_programming(direction, A, senses, b, c, l, u, types, names):
    # create an empty optimization problem
    prob = cp.Cplex()

    # add decision variables to the problem including their coefficients in objective and ranges
    prob.variables.add(obj = c.tolist(), lb = l.tolist(), ub = u.tolist(), types = types.tolist(), names = names.tolist())

    # define problem type
    if direction == "maximize":
        prob.objective.set_sense(prob.objective.sense.maximize)
    else:
        prob.objective.set_sense(prob.objective.sense.minimize)

    # add constraints to the problem including their directions and right-hand side values
    prob.linear_constraints.add(senses = senses.tolist(), rhs = b.tolist())

    # add coefficients for each constraint
    row_indices, col_indices = A.nonzero()
    prob.linear_constraints.set_coefficients(zip(row_indices.tolist(), col_indices.tolist(), A.data.tolist()))

    print(prob.write_as_string())
    # solve the problem
    prob.solve()
    
    # check the solution status
    print(prob.solution.get_status())
    print(prob.solution.status[prob.solution.get_status()])

    # get the solution
    x_star = prob.solution.get_values()
    obj_star = prob.solution.get_objective_value()

    return(x_star, obj_star)

def coin_distribution_problem(coins_file, M):
    # your implementation starts below
    
    coins = np.loadtxt(coins_file)
    N = coins.shape[0]
    
    c = np.ones(N*M)
    b = np.concatenate((np.repeat(1/M*(np.sum(coins)),M),np.repeat(1,N)))
    senses = np.repeat("E",M+N)
    l = np.repeat(0,M*N)
    u = np.repeat(1,M*N)
    names = np.array([f"x_{i}_{j}" for i in range(1,N+1) for j in range(1,M+1)])
    types = np.repeat("B", N*M)
    
    data = np.concatenate((np.tile(coins, M),np.repeat(1,M*N)))
    row = np.concatenate((np.repeat(range(M), N),np.repeat(range(M,M+N), M)))
    col = np.concatenate((np.array(range(N*M)).reshape(N, M).T.flatten(),np.array(range(N*M))))
    A = sp.csr_matrix((data, (row, col)), shape=(M+N, M*N))
    
    X_star, Obj_star = mixed_integer_linear_programming("maximize", A, senses, b, c, l, u, types, names)

    # your implementation ends above
    return(X_star)

X_star = coin_distribution_problem("coins.txt", 2)
print(X_star)