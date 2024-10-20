import sympy as sp
from sympy.solvers import solve
from sympy import Eq

class EquationSolver:
    def __init__(self):
        pass

    def solve_linear(self, equation):
        """Solve a single linear equation."""
        x = sp.symbols('x')
        solution = solve(equation, x)
        return solution

    def solve_quadratic(self, a, b, c):
        """Solve a quadratic equation of the form ax^2 + bx + c = 0."""
        x = sp.symbols('x')
        equation = Eq(a*x**2 + b*x + c, 0)
        solution = solve(equation, x)
        return solution

    def solve_system(self, equations, variables):
        """Solve a system of equations with given variables."""
        solution = solve(equations, variables)
        return solution

    def solve_symbolic(self, equation, variable):
        """Solve any symbolic equation."""
        solution = solve(equation, variable)
        return solution

def main():
    solver = EquationSolver()

    print("=== Equation Solver ===")
    while True:
        print("\n1. Solve Linear Equation")
        print("2. Solve Quadratic Equation")
        print("3. Solve System of Equations")
        print("4. Solve Symbolic Equation")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            # Solving linear equations
            try:
                equation = input("Enter the linear equation (e.g., '2*x + 3 = 7'): ")
                x = sp.symbols('x')
                solution = solver.solve_linear(sp.sympify(equation))
                print(f"Solution: {solution}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            # Solving quadratic equations
            try:
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter coefficient c: "))
                solution = solver.solve_quadratic(a, b, c)
                print(f"Solutions: {solution}")
            except ValueError:
                print("Please enter valid numbers.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            # Solving a system of equations
            try:
                num_equations = int(input("Enter number of equations: "))
                equations = []
                variables = []

                for i in range(num_equations):
                    equation = input(f"Enter equation {i + 1} (e.g., '2*x + y = 5'): ")
                    equations.append(sp.sympify(equation))

                num_variables = int(input("Enter number of variables: "))
                for i in range(num_variables):
                    variable = input(f"Enter variable {i + 1} (e.g., 'x', 'y'): ")
                    variables.append(sp.symbols(variable))

                solution = solver.solve_system(equations, variables)
                print(f"Solution: {solution}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "4":
            # Solving symbolic equations
            try:
                equation = input("Enter the symbolic equation (e.g., 'x**2 - 4 = 0'): ")
                variable = input("Enter the variable to solve for (e.g., 'x'): ")
                solution = solver.solve_symbolic(sp.sympify(equation), sp.symbols(variable))
                print(f"Solution: {solution}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
