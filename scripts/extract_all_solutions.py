#!/usr/bin/env python3
"""
Extract all 40 solutions from Exercise 1 JSONL files
Organize by model and strategy
"""
import json
from pathlib import Path
import sys

def extract_solutions_by_config(jsonl_file, output_dir, config_name):
    """Extract solutions from JSONL file, organized by problem"""
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py
    (output_dir / '__init__.py').touch()
    
    solutions_by_problem = {}
    
    # Read JSONL file
    try:
        with open(jsonl_file, 'r') as f:
            for line in f:
                sample = json.loads(line)
                task_id = sample['task_id']
                problem_num = task_id.split('/')[-1]
                
                # Take first occurrence of each problem (or first passing one)
                if problem_num not in solutions_by_problem:
                    solutions_by_problem[problem_num] = {
                        'task_id': task_id,
                        'completion': sample['completion'],
                        'passed': sample.get('passed', False)
                    }
                elif sample.get('passed', False) and not solutions_by_problem[problem_num]['passed']:
                    # Prefer passing solutions over failing ones
                    solutions_by_problem[problem_num] = {
                        'task_id': task_id,
                        'completion': sample['completion'],
                        'passed': sample.get('passed', False)
                    }
    except FileNotFoundError:
        print(f"✗ File not found: {jsonl_file}")
        print(f"   Please check if the file exists at this location")
        return 0
    except json.JSONDecodeError as e:
        print(f"✗ Error parsing JSON in {jsonl_file}: {e}")
        return 0
    
    # Write each solution to file
    count = 0
    for problem_num, data in sorted(solutions_by_problem.items(), key=lambda x: int(x[0])):
        output_file = output_dir / f"humaneval_{problem_num}.py"
        
        with open(output_file, 'w') as f:
            f.write(f'"""\n')
            f.write(f'{data["task_id"]}\n')
            f.write(f'Configuration: {config_name}\n')
            f.write(f'Status: {"PASSED" if data["passed"] else "FAILED"}\n')
            f.write(f'"""\n\n')
            f.write(data['completion'])
        
        status = "✓" if data['passed'] else "✗"
        print(f"{status} {config_name:35s} | HumanEval/{problem_num:2s} -> {output_file.name}")
        count += 1
    
    return count

def main():
    """Extract all solutions from all configurations"""
    
    # Check if running from correct directory
    if not Path('part1').exists():
        print("\n" + "="*80)
        print("ERROR: 'part1' directory not found!")
        print("="*80)
        print("\nPlease run this script from the 'exercise2' directory.")
        print("Your current directory structure should be:")
        print("  exercise2/")
        print("    ├── part1/              ← JSONL files here")
        print("    ├── scripts/            ← This script")
        print("    ├── solutions/          ← Will be created")
        print("    └── tests/              ← Will be created")
        print("\nTry: cd exercise2 && python scripts/extract_all_solutions.py")
        sys.exit(1)
    
    # List files in part1 to help debug
    part1_dir = Path('part1')
    print("\n" + "="*80)
    print("Files found in part1/ directory:")
    print("="*80)
    for f in sorted(part1_dir.glob('*.jsonl')):
        print(f"  ✓ {f.name}")
    print()
    
    # Your exact file names from the screenshot
    configurations = [
        {
            'file': 'part1/codellama_7b_CoT.jsonl',
            'output': 'solutions/codellama_7b_cot',
            'name': 'CodeLlama-7B + CoT'
        },
        {
            'file': 'part1/codellama_7b_Self-Planning.jsonl',
            'output': 'solutions/codellama_7b_planning',
            'name': 'CodeLlama-7B + Self-Planning'
        },
        {
            'file': 'part1/deepseek-coder_6.7b_CoT.jsonl',
            'output': 'solutions/deepseek_coder_6.7b_cot',
            'name': 'DeepSeek-6.7B + CoT'
        },
        {
            'file': 'part1/deepseek-coder_6.7b_Self-Planning.jsonl',
            'output': 'solutions/deepseek_coder_6.7b_planning',
            'name': 'DeepSeek-6.7B + Self-Planning'
        }
    ]
    
    print("="*80)
    print("EXTRACTING ALL 40 SOLUTIONS")
    print("="*80 + "\n")
    
    total_solutions = 0
    for config in configurations:
        print(f"\n>>> {config['name']}")
        print("-"*80)
        
        # Check if file exists
        if not Path(config['file']).exists():
            print(f"✗ File not found: {config['file']}")
            print(f"   Skipping this configuration...")
            continue
        
        count = extract_solutions_by_config(
            config['file'], 
            config['output'], 
            config['name']
        )
        total_solutions += count
    
    print("\n" + "="*80)
    print(f"✓ Extracted {total_solutions} solutions total (40 expected)")
    print("="*80 + "\n")
    
    if total_solutions < 40:
        print("⚠ Warning: Expected 40 solutions but got fewer.")
        print("  Check if all JSONL files exist in part1/ directory")

if __name__ == '__main__':
    main()