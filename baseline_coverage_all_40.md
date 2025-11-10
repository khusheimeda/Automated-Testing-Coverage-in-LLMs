# Baseline Coverage - All 40 Solutions

## Line Coverage (L) and Branch Coverage (B)

| Problem | CodeLlama-7B + CoT | CodeLlama-7B + Self-Planning | DeepSeek-6.7B + CoT | DeepSeek-6.7B + Self-Planning |
|---------|---------------------------|---------------------------|---------------------------|---------------------------|
| HumanEval/0 | ✗ L:71.4% B:50.0% | ✗ L:100.0% B:100.0% | ✗ L:100.0% B:100.0% | ✓ L:100.0% B:100.0% |
| HumanEval/1 | ✗ ERROR | ✗ ERROR | ✗ ERROR | ✗ ERROR |
| HumanEval/2 | ✓ L:77.8% B:50.0% | ✗ ERROR | ✓ L:100.0% B:100.0% | ✓ L:75.0% B:50.0% |
| HumanEval/10 | ✗ L:85.7% B:80.0% | ✗ L:60.0% B:100.0% | ✓ L:88.2% B:83.3% | ✗ ERROR |
| HumanEval/11 | ✓ L:84.6% B:75.0% | ✓ L:84.6% B:75.0% | ✓ L:88.9% B:83.3% | ✓ L:88.2% B:83.3% |
| HumanEval/12 | ✗ ERROR | ✗ ERROR | ✗ L:100.0% B:100.0% | ✗ L:100.0% B:100.0% |
| HumanEval/20 | ✗ L:100.0% B:100.0% | ✗ L:100.0% B:100.0% | ✓ L:90.0% B:83.3% | ✗ L:100.0% B:100.0% |
| HumanEval/25 | ✗ L:100.0% B:100.0% | ✓ L:90.5% B:87.5% | ✓ L:100.0% B:100.0% | ✗ L:91.3% B:87.5% |
| HumanEval/31 | ✓ L:100.0% B:100.0% | ✗ L:85.7% B:83.3% | ✗ L:71.4% B:66.7% | ✓ L:100.0% B:100.0% |
| HumanEval/37 | ✗ L:100.0% B:100.0% | ✗ ERROR | ✓ L:89.5% B:83.3% | ✗ L:100.0% B:100.0% |
| **Average** | L:89.9% B:81.9% | L:86.8% B:91.0% | L:92.0% B:88.9% | L:94.3% B:90.1% |
| **Pass Rate** | 3/10 (30.0%) | 2/10 (20.0%) | 6/10 (60.0%) | 4/10 (40.0%) |
