"""
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
