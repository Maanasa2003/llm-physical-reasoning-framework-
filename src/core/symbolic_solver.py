import sympy as sp

def solve_equation(equation_str: str, solve_for: str, known_values: dict):
    """
    General-purpose symbolic equation solver.

    equation_str: "20 - 0.5*g*t**2"
    solve_for: "t"
    known_values: {"g": 9.8}
    """
    # Create symbols for all variables
    symbols = {var: sp.symbols(var, real=True) for var in known_values.keys() | {solve_for}}

    # Parse equation
    expr = sp.sympify(equation_str, locals=symbols)

    # Substitute known values
    substituted = expr.subs(known_values)

    # Solve for the target variable
    solutions = sp.solve(substituted, symbols[solve_for])

    # Filter real, positive solutions
    real_solutions = [sol for sol in solutions if sol.is_real]

    return real_solutions