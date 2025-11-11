#!/usr/bin/env python3
"""
Create 10 test suites from HumanEval benchmark
Each test suite will be used to test all 4 solution variants
"""
from human_eval.data import read_problems
from pathlib import Path
import sys

def create_test_suite(problem_num, problem_data, output_dir):
    """Create a single test suite file for a problem"""
    
    task_id = f"HumanEval/{problem_num}"
    entry_point = problem_data['entry_point']
    test_code = problem_data['test']
    prompt = problem_data['prompt']
    
    output_file = Path(output_dir) / f"test_humaneval_{problem_num}.py"
    
    with open(output_file, 'w') as f:
        f.write(f'"""\n')
        f.write(f'Test suite for {task_id} - {entry_point}\n')
        f.write(f'This test suite is used to test all 4 solution variants\n')
        f.write(f'"""\n')
        f.write(f'import pytest\n')
        f.write(f'import sys\n')
        f.write(f'from pathlib import Path\n\n')
        
        f.write(f'def test_{entry_point}(solution_module):\n')
        f.write(f'    """\n')
        f.write(f'    Test {entry_point} from HumanEval benchmark\n')
        f.write(f'    solution_module: The module containing the solution to test\n')
        f.write(f'    """\n')
        f.write(f'    # Import the function from the solution module\n')
        f.write(f'    {entry_point} = getattr(solution_module, "{entry_point}")\n\n')
        
        # Extract assertions from test code
        f.write(f'    # Test cases from HumanEval benchmark\n')
        lines = test_code.split('\n')
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('assert'):
                # Replace 'candidate' with the function name
                test_line = stripped.replace('candidate', entry_point)
                f.write(f'    {test_line}\n')
    
    print(f"✓ Created {output_file.name} for {entry_point}")
    return True

def create_conftest(output_dir):
    """Create conftest.py for pytest configuration"""
    
    conftest_file = Path(output_dir) / 'conftest.py'
    
    with open(conftest_file, 'w') as f:
        f.write('''"""
Pytest configuration for testing multiple solution variants
"""
import pytest
import importlib.util
from pathlib import Path
import sys

def pytest_addoption(parser):
    """Add command line option to specify which solution variant to test"""
    parser.addoption(
        "--solution-dir",
        action="store",
        default="solutions/deepseek_coder_6.7b_planning",
        help="Directory containing solutions to test"
    )

@pytest.fixture
def solution_module(request):
    """
    Fixture that imports the solution module for the current test
    Allows same test suite to run against different solution variants
    """
    # Get the test file name to determine which problem we're testing
    test_file = Path(request.fspath)
    # Extract problem number from test file name (e.g., test_humaneval_0.py -> 0)
    problem_num = test_file.stem.split('_')[-1]
    
    # Get solution directory from command line option
    solution_dir = request.config.getoption("--solution-dir")
    
    # Import the solution module
    solution_file = Path(solution_dir) / f"humaneval_{problem_num}.py"
    
    if not solution_file.exists():
        pytest.skip(f"Solution file not found: {solution_file}")
    
    try:
        spec = importlib.util.spec_from_file_location(
            f"solution_{problem_num}", 
            solution_file
        )
        module = importlib.util.module_from_spec(spec)
        
        # Add parent directory to sys.path for imports
        sys.path.insert(0, str(solution_file.parent))
        
        spec.loader.exec_module(module)
        
        return module
    except Exception as e:
        pytest.skip(f"Error loading solution: {e}")
''')
    
    print(f"✓ Created conftest.py")

def create_all_test_suites():
    """Create all 10 test suites"""
    
    # Check if human_eval package is available
    try:
        problems = read_problems()
    except Exception as e:
        print("\n" + "="*80)
        print("ERROR: Cannot load HumanEval dataset")
        print("="*80)
        print(f"\n{str(e)}\n")
        print("Please install human-eval package:")
        print("  pip install human-eval")
        print("\nOr if you have the dataset locally:")
        print("  pip install -e /path/to/human-eval")
        sys.exit(1)
    
    test_dir = Path('tests')
    test_dir.mkdir(exist_ok=True)
    
    # Create __init__.py
    (test_dir / '__init__.py').touch()
    
    # Your 10 problems
    problem_nums = [0, 1, 2, 10, 11, 12, 20, 25, 31, 37]
    
    print("\n" + "="*80)
    print("CREATING 10 TEST SUITES")
    print("="*80 + "\n")
    
    created = 0
    for prob_num in problem_nums:
        task_id = f"HumanEval/{prob_num}"
        if task_id in problems:
            if create_test_suite(prob_num, problems[task_id], test_dir):
                created += 1
        else:
            print(f"✗ Problem {task_id} not found in HumanEval dataset")
    
    # Create conftest.py
    print()
    create_conftest(test_dir)
    
    print("\n" + "="*80)
    print(f"✓ Created {created} test suites + conftest.py")
    print("="*80 + "\n")
    
    # Show what was created
    print("Test files created:")
    for test_file in sorted(test_dir.glob('test_*.py')):
        print(f"  - {test_file.name}")
    
    print("\nYou can now run coverage with:")
    print("  python scripts/run_all_coverage.py")
    print()

def main():
    """Main entry point"""
    
    # Check if we're in the right directory
    if not Path('scripts').exists():
        print("\n" + "="*80)
        print("ERROR: Please run this script from the exercise2 directory")
        print("="*80)
        print("\nTry: cd exercise2 && python scripts/create_test_suites.py")
        sys.exit(1)
    
    create_all_test_suites()

if __name__ == '__main__':
    main()