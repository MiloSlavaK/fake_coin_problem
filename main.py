from strategy import FakeCoinSolver
from visualization import visualize_tree

def main():
    solver = FakeCoinSolver(12)

    result = solver.solve()

    print("Результат:")
    print(result)

    visualize_tree(solver.tree)

if __name__ == "__main__":
    main()