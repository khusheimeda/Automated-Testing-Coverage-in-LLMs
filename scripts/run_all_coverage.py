#!/usr/bin/env python3
"""
Run coverage for all 40 solutions using the 10 test suites
Generate 40 separate coverage reports
"""
import subprocess
import json
from pathlib import Path
import sys
import os
import shutil

def check_dependencies():
    """Check if required tools are installed"""
    
    print("\n" + "="*80)
    print("CHECKING DEPENDENCIES")
    print("="*80 + "\n")
    
    # Check for pytest
    pytest_path = shutil.which('pytest')
    if pytest_path:
        print(f"✓ pytest found at: {pytest_path}")
    else:
        print("✗ pytest not found")
        print("\nPlease install required packages:")
        print("  pip3 install pytest pytest-cov coverage human-eval")
        print("\nOr create a virtual environment:")
        print("  python3 -m venv venv")
        print("  source venv/bin/activate  # On Mac/Linux")
        print("  pip install pytest pytest-cov coverage human-eval")
        return False
    
    # Check for pytest-cov
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pytest', '--version'],
            capture_output=True,
            text=True
        )
        print(f"✓ pytest version: {result.stdout.strip()}")
    except Exception as e:
        print(f"✗ Error checking pytest: {e}")
        return False
    
    # Check for coverage
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'coverage', '--version'],
            capture_output=True,
            text=True
        )
        print(f"✓ coverage version: {result.stdout.strip()}")
    except Exception as e:
        print(f"⚠ coverage not found (pytest-cov should still work)")
    
    print()
    return True

def check_setup():
    """Check if all required directories and files exist"""
    issues = []
    
    # Check for solutions directory
    if not Path('solutions').exists():
        issues.append("solutions/ directory not found. Run extract_all_solutions.py first.")
    
    # Check for tests directory
    if not Path('tests').exists():
        issues.append("tests/ directory not found. Run create_test_suites.py first.")
    
    # Check for conftest.py
    if not Path('tests/conftest.py').exists():
        issues.append("tests/conftest.py not found. Run create_test_suites.py first.")
    
    # Check for at least one solution directory
    solution_dirs = [
        'solutions/codellama_7b_cot',
        'solutions/codellama_7b_planning',
        'solutions/deepseek_coder_6.7b_cot',
        'solutions/deepseek_coder_6.7b_planning'
    ]
    
    found_solutions = False
    for dir_path in solution_dirs:
        if Path(dir_path).exists():
            found_solutions = True
            break
    
    if not found_solutions:
        issues.append("No solution directories found. Run extract_all_solutions.py first.")
    
    if issues:
        print("\n" + "="*80)
        print("SETUP ISSUES DETECTED")
        print("="*80)
        for issue in issues:
            print(f"✗ {issue}")
        print("\nPlease run the setup scripts first:")
        print("  1. python3 scripts/extract_all_solutions.py")
        print("  2. python3 scripts/create_test_suites.py")
        print("  3. python3 scripts/run_all_coverage.py")
        print("="*80 + "\n")
        return False
    
    return True

def run_coverage_for_config(config_dir, config_name, problem_nums):
    """Run coverage for all problems in a configuration"""
    
    results = []
    
    # Check if solution directory exists
    solution_dir = Path(f'solutions/{config_dir}')
    if not solution_dir.exists():
        print(f"  ✗ Solution directory not found: {solution_dir}")
        return results
    
    # Create output directory for this configuration
    output_dir = Path(f'coverage_reports/{config_dir}')
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for prob_num in problem_nums:
        solution_file = Path(f'solutions/{config_dir}/humaneval_{prob_num}.py')
        test_file = Path(f'tests/test_humaneval_{prob_num}.py')
        
        if not solution_file.exists():
            print(f"  ✗ HumanEval/{prob_num:2d}: Solution file not found")
            results.append({
                'config': config_name,
                'config_dir': config_dir,
                'problem': f'HumanEval/{prob_num}',
                'tests_passed': False,
                'line_coverage': 0,
                'branch_coverage': 0,
                'error': 'Solution file not found'
            })
            continue
        
        if not test_file.exists():
            print(f"  ✗ HumanEval/{prob_num:2d}: Test file not found")
            results.append({
                'config': config_name,
                'config_dir': config_dir,
                'problem': f'HumanEval/{prob_num}',
                'tests_passed': False,
                'line_coverage': 0,
                'branch_coverage': 0,
                'error': 'Test file not found'
            })
            continue
        
        # Run pytest with coverage using python -m pytest
        cmd = [
            sys.executable,  # Use current Python interpreter
            '-m', 'pytest',
            str(test_file),
            f'--solution-dir=solutions/{config_dir}',
            f'--cov=solutions/{config_dir}',
            '--cov-branch',
            '--cov-report=json',
            '--cov-report=term-missing',
            f'--cov-report=html:{output_dir}/html_{prob_num}',
            '-v',
            '--tb=short',
            '-q'  # Quiet mode - less verbose
        ]
        
        # Run the command
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True,
                cwd=Path.cwd(),
                timeout=30  # 30 second timeout per test
            )
        except subprocess.TimeoutExpired:
            print(f"  ✗ HumanEval/{prob_num:2d}: Test timed out")
            results.append({
                'config': config_name,
                'config_dir': config_dir,
                'problem': f'HumanEval/{prob_num}',
                'tests_passed': False,
                'line_coverage': 0,
                'branch_coverage': 0,
                'error': 'Test timed out'
            })
            continue
        except Exception as e:
            print(f"  ✗ HumanEval/{prob_num:2d}: Error running pytest - {str(e)}")
            results.append({
                'config': config_name,
                'config_dir': config_dir,
                'problem': f'HumanEval/{prob_num}',
                'tests_passed': False,
                'line_coverage': 0,
                'branch_coverage': 0,
                'error': f'Pytest error: {str(e)}'
            })
            continue
        
        # Parse JSON coverage
        coverage_json_path = Path('coverage.json')
        
        if not coverage_json_path.exists():
            print(f"  ✗ HumanEval/{prob_num:2d}: Coverage file not generated")
            # Print stderr for debugging
            if result.stderr:
                print(f"     Error output: {result.stderr[:200]}")
            results.append({
                'config': config_name,
                'config_dir': config_dir,
                'problem': f'HumanEval/{prob_num}',
                'tests_passed': False,
                'line_coverage': 0,
                'branch_coverage': 0,
                'error': 'Coverage file not generated'
            })
            continue
        
        try:
            with open(coverage_json_path, 'r') as f:
                cov_data = json.load(f)
            
            # Find coverage for this specific file
            file_key = None
            for key in cov_data['files'].keys():
                if f'humaneval_{prob_num}.py' in key:
                    file_key = key
                    break
            
            if file_key:
                file_data = cov_data['files'][file_key]
                summary = file_data['summary']
                
                # Calculate branch coverage
                num_branches = summary.get('num_branches', 0)
                covered_branches = summary.get('covered_branches', 0)
                branch_coverage = (covered_branches / num_branches * 100) if num_branches > 0 else 100.0
                
                results.append({
                    'config': config_name,
                    'config_dir': config_dir,
                    'problem': f'HumanEval/{prob_num}',
                    'tests_passed': result.returncode == 0,
                    'line_coverage': summary['percent_covered'],
                    'branch_coverage': branch_coverage,
                    'num_statements': summary['num_statements'],
                    'missing_lines': summary['missing_lines'],
                    'covered_lines': summary['covered_lines'],
                    'num_branches': num_branches,
                    'covered_branches': covered_branches
                })
                
                status = "✓" if result.returncode == 0 else "✗"
                line_cov = summary['percent_covered']
                print(f"  {status} HumanEval/{prob_num:2d}: Line {line_cov:5.1f}% | Branch {branch_coverage:5.1f}%")
            else:
                print(f"  ✗ HumanEval/{prob_num:2d}: Coverage data not found in JSON")
                results.append({
                    'config': config_name,
                    'config_dir': config_dir,
                    'problem': f'HumanEval/{prob_num}',
                    'tests_passed': False,
                    'line_coverage': 0,
                    'branch_coverage': 0,
                    'error': 'Coverage data not found in JSON'
                })
        
        except json.JSONDecodeError as e:
            print(f"  ✗ HumanEval/{prob_num:2d}: Error parsing coverage.json - {str(e)}")
            results.append({
                'config': config_name,
                'config_dir': config_dir,
                'problem': f'HumanEval/{prob_num}',
                'tests_passed': False,
                'line_coverage': 0,
                'branch_coverage': 0,
                'error': f'JSON parse error: {str(e)}'
            })
        
        except Exception as e:
            print(f"  ✗ HumanEval/{prob_num:2d}: Error - {str(e)}")
            results.append({
                'config': config_name,
                'config_dir': config_dir,
                'problem': f'HumanEval/{prob_num}',
                'tests_passed': False,
                'line_coverage': 0,
                'branch_coverage': 0,
                'error': str(e)
            })
        
        # Clean up coverage.json for next iteration
        if coverage_json_path.exists():
            try:
                coverage_json_path.unlink()
            except:
                pass
    
    return results

def run_all_coverage():
    """Run coverage for all 40 solutions"""
    
    # Check dependencies
    if not check_dependencies():
        return []
    
    # Check setup
    if not check_setup():
        return []
    
    # Your exact configuration names matching the directory structure
    configurations = [
        ('codellama_7b_cot', 'CodeLlama-7B + CoT'),
        ('codellama_7b_planning', 'CodeLlama-7B + Self-Planning'),
        ('deepseek_coder_6.7b_cot', 'DeepSeek-6.7B + CoT'),
        ('deepseek_coder_6.7b_planning', 'DeepSeek-6.7B + Self-Planning')
    ]
    
    problem_nums = [0, 1, 2, 10, 11, 12, 20, 25, 31, 37]
    
    all_results = []
    
    print("\n" + "="*80)
    print("RUNNING COVERAGE FOR ALL 40 SOLUTIONS")
    print("="*80 + "\n")
    
    for config_dir, config_name in configurations:
        print(f"\n>>> {config_name}")
        print("-"*80)
        
        results = run_coverage_for_config(config_dir, config_name, problem_nums)
        all_results.extend(results)
    
    return all_results

def generate_summary_table(results):
    """Generate comprehensive summary table"""
    
    if not results:
        print("\n✗ No results to summarize")
        return
    
    print("\n" + "="*100)
    print("BASELINE COVERAGE SUMMARY - ALL 40 SOLUTIONS")
    print("="*100 + "\n")
    
    # Group by problem
    problems = sorted(set(r['problem'] for r in results), 
                     key=lambda x: int(x.split('/')[-1]))
    
    configs = [
        ('CodeLlama-7B + CoT', 'codellama_7b_cot'),
        ('CodeLlama-7B + Self-Planning', 'codellama_7b_planning'),
        ('DeepSeek-6.7B + CoT', 'deepseek_coder_6.7b_cot'),
        ('DeepSeek-6.7B + Self-Planning', 'deepseek_coder_6.7b_planning')
    ]
    
    # Print header
    print(f"{'Problem':<15} | ", end='')
    for name, _ in configs:
        print(f"{name[:20]:>20} | ", end='')
    print()
    print("-"*120)
    
    # Print each problem with line coverage
    for problem in problems:
        print(f"{problem:<15} | ", end='')
        
        for config_name, config_dir in configs:
            # Find result for this problem + config
            result = next((r for r in results 
                          if r['problem'] == problem and r.get('config_dir') == config_dir), 
                         None)
            
            if result and 'error' not in result:
                status = "✓" if result['tests_passed'] else "✗"
                line_cov = result['line_coverage']
                branch_cov = result.get('branch_coverage', 0)
                print(f"{status} L:{line_cov:5.1f}% B:{branch_cov:5.1f}% | ", end='')
            elif result and 'error' in result:
                print(f"✗ ERROR             | ", end='')
            else:
                print(f"       N/A           | ", end='')
        print()
    
    # Calculate averages
    print("-"*120)
    print(f"{'Average':<15} | ", end='')
    for config_name, config_dir in configs:
        config_results = [r for r in results 
                         if r.get('config_dir') == config_dir and 'error' not in r]
        if config_results:
            avg_line = sum(r['line_coverage'] for r in config_results) / len(config_results)
            avg_branch = sum(r.get('branch_coverage', 0) for r in config_results) / len(config_results)
            print(f"  L:{avg_line:5.1f}% B:{avg_branch:5.1f}% | ", end='')
        else:
            print(f"       N/A           | ", end='')
    print("\n")
    
    # Print pass rates
    print(f"{'Pass Rate':<15} | ", end='')
    for config_name, config_dir in configs:
        config_results = [r for r in results if r.get('config_dir') == config_dir]
        if config_results:
            passed = sum(1 for r in config_results if r.get('tests_passed', False))
            total = len(config_results)
            pass_rate = (passed / total * 100) if total > 0 else 0
            print(f"  {passed}/{total} ({pass_rate:5.1f}%)    | ", end='')
        else:
            print(f"       N/A           | ", end='')
    print("\n")
    
    # Save to markdown
    with open('baseline_coverage_all_40.md', 'w') as f:
        f.write("# Baseline Coverage - All 40 Solutions\n\n")
        f.write("## Line Coverage (L) and Branch Coverage (B)\n\n")
        f.write("| Problem |")
        for name, _ in configs:
            f.write(f" {name} |")
        f.write("\n|---------|")
        for _ in configs:
            f.write("---------------------------|")
        f.write("\n")
        
        for problem in problems:
            f.write(f"| {problem} |")
            for config_name, config_dir in configs:
                result = next((r for r in results 
                              if r['problem'] == problem and r.get('config_dir') == config_dir), 
                             None)
                if result and 'error' not in result:
                    status = "✓" if result['tests_passed'] else "✗"
                    line_cov = result['line_coverage']
                    branch_cov = result.get('branch_coverage', 0)
                    f.write(f" {status} L:{line_cov:.1f}% B:{branch_cov:.1f}% |")
                elif result and 'error' in result:
                    f.write(" ✗ ERROR |")
                else:
                    f.write(" N/A |")
            f.write("\n")
        
        # Add averages
        f.write("| **Average** |")
        for config_name, config_dir in configs:
            config_results = [r for r in results 
                             if r.get('config_dir') == config_dir and 'error' not in r]
            if config_results:
                avg_line = sum(r['line_coverage'] for r in config_results) / len(config_results)
                avg_branch = sum(r.get('branch_coverage', 0) for r in config_results) / len(config_results)
                f.write(f" L:{avg_line:.1f}% B:{avg_branch:.1f}% |")
            else:
                f.write(" N/A |")
        f.write("\n")
        
        # Add pass rates
        f.write("| **Pass Rate** |")
        for config_name, config_dir in configs:
            config_results = [r for r in results if r.get('config_dir') == config_dir]
            if config_results:
                passed = sum(1 for r in config_results if r.get('tests_passed', False))
                total = len(config_results)
                pass_rate = (passed / total * 100) if total > 0 else 0
                f.write(f" {passed}/{total} ({pass_rate:.1f}%) |")
            else:
                f.write(" N/A |")
        f.write("\n")
    
    print("✓ Summary saved to baseline_coverage_all_40.md")
    
    # Save detailed JSON
    with open('coverage_results_detailed.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("✓ Detailed results saved to coverage_results_detailed.json")
    
    print("\n" + "="*80 + "\n")

def main():
    """Main entry point"""
    
    # Check if we're in the right directory
    if not Path('scripts').exists():
        print("\n" + "="*80)
        print("ERROR: Please run this script from the exercise2 directory")
        print("="*80)
        print("\nTry: cd exercise2 && python3 scripts/run_all_coverage.py")
        sys.exit(1)
    
    # Run coverage
    results = run_all_coverage()
    
    # Generate summary
    if results:
        generate_summary_table(results)
    else:
        print("\n✗ No coverage results collected. Check errors above.")

if __name__ == '__main__':
    main()