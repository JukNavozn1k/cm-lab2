import math
from tabulate import tabulate

def solve_system_newton(x0, y0, e):
    # Initialize x and y with the initial values
    x = x0
    y = y0
    
    # Initialize the iteration counter
    it = 0
    
    # Initialize the table with the initial values of x and y
    table = [[it, x, y]]
    
    while True:
        # Calculate the functions and their derivatives
        f1 = math.sin(x + 2.1) - 3 * y + 0.4
        f1_der_x = math.cos(x + 2.1)
        f1_der_y = -3
        f2 = math.cos(y + 1.8) + 1.2 * x
        f2_der_x = 1.2
        f2_der_y = -math.sin(y + 1.8)
        
        # Calculate the Jacobian matrix
        jacobian = [[f1_der_x, f1_der_y], [f2_der_x, f2_der_y]]
        
        # Calculate the inverse of the Jacobian matrix
        det = jacobian[0][0] * jacobian[1][1] - jacobian[0][1] * jacobian[1][0]
        jacobian_inv = [[jacobian[1][1] / det, -jacobian[0][1] / det], [-jacobian[1][0] / det, jacobian[0][0] / det]]
        
        # Calculate the function values vector
        f = [f1, f2]
        
        # Calculate the update vector
        update = [jacobian_inv[0][0] * f[0] + jacobian_inv[0][1] * f[1], jacobian_inv[1][0] * f[0] + jacobian_inv[1][1] * f[1]]
        
        # Update x and y
        x -= update[0]
        y -= update[1]
        
        # Increment the iteration counter
        it += 1
        
        # Add the current values of x and y to the table
        table.append([it, x, y])
        
        # Calculate the maximum update
        max_update = max(abs(update[0]), abs(update[1]))
        
        # Check if the maximum update is smaller than the required accuracy
        if max_update < e:
            break
    
    # Print the table
    print(tabulate(table, headers=['Iteration', 'x', 'y']))

# Test the function
solve_system_newton(0, 0, 0.0001)
