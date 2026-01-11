import argparse
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
sys.path.append(os.path.join(ROOT, "src"))
from src.core.reasoning_engine import ReasoningEngine
from src.test_reasoning import run_all_benchmarks

def main():
    parser = argparse.ArgumentParser(description="Physics Reasoning Engine CLI")

    parser.add_argument(
        "--scenario",
        type=str,
        help="Run a custom physics scenario and return only the answer."
    )

    parser.add_argument(
        "--benchmarks",
        action="store_true",
        help="Run the full benchmark evaluation suite."
    )

    args = parser.parse_args()

    # --- Mode 1: Custom scenario ---
    if args.scenario:
        engine = ReasoningEngine()
        result = engine.run(args.scenario)

        print("\n=== Answer ===")
        print(result.get("final_answer") or result.get("sympy_solution"))
        return

    # --- Mode 2: Benchmark evaluation ---
    if args.benchmarks:
        run_all_benchmarks()
        return

    # --- No mode selected ---
    parser.print_help()


if __name__ == "__main__":
    main()