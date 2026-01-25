# Version Control Guide - Tracking GPU Performance Over Time

## Why Track Results in Git

By keeping result files in version control, you can:

✅ **Compare performance over time** - See if performance degrades or improves
✅ **Track driver updates** - Benchmark before/after driver changes
✅ **Document hardware changes** - Record when you swap cards
✅ **Detect issues** - Spot thermal throttling or other problems
✅ **Share results** - Collaborate and compare with others

## What's Tracked

### Result Files (JSON)
All benchmark and test results are tracked:
```
results/benchmark_GPU0_*.json
results/stress_test_GPU0_*.json
results/gpu_identification_GPU0_*.json
```

### Documentation
All markdown documentation is tracked:
```
docs/*.md
README.md
STRUCTURE.md
```

### Scripts
All Python and shell scripts are tracked:
```
scripts/*.py
scripts/*.sh
```

## What's NOT Tracked

According to `.gitignore`:
- Python cache files (`__pycache__/`, `*.pyc`)
- Comparison reports (`comparison_*.txt`) - can be regenerated
- Temp files (`*.tmp`, `*.log`)

## Workflow: Tracking Your GPU Tests

### Initial Setup (Already Done)

```bash
cd gpu_benchmarks
git add .
git commit -m "Add GPU benchmarking suite with initial RTX 3090 results"
```

### After Each Test Session

```bash
# Run your tests
./benchmark
# Or:
python scripts/test_all_gpus.py --benchmark --stress --duration 600

# Add new results
git add results/*.json

# Commit with descriptive message
git commit -m "RTX 3090 XC3 ULTRA - baseline benchmarks"
```

### Card Swap Workflow

When you swap cards:

```bash
# 1. Test new card
python scripts/identify_gpu.py --gpu 0 --save
python scripts/test_all_gpus.py --benchmark --stress --duration 600

# 2. Add results
git add results/benchmark_GPU0_*RTX_4090*.json
git add results/stress_test_GPU0_*RTX_4090*.json
git add results/gpu_identification_GPU0_*.json

# 3. Commit with card info
git commit -m "Add RTX 4090 FTW3 ULTRA benchmark results"

# 4. Optional: Tag the commit
git tag -a rtx4090-baseline -m "RTX 4090 FTW3 ULTRA baseline benchmarks"
```

### Comparing Results Over Time

#### View changes between commits
```bash
# See what changed in results
git diff HEAD~1 HEAD -- results/

# Compare specific files
git diff rtx3090-baseline:results/benchmark_*.json rtx4090-baseline:results/benchmark_*.json
```

#### View result file history
```bash
# See all commits that changed a file
git log -- results/benchmark_GPU0_NVIDIA_GeForce_RTX_3090*.json

# See diff for specific commit
git show <commit-hash>
```

#### Compare old vs new performance
```bash
# Checkout old results temporarily
git show HEAD~5:results/benchmark_GPU0_*.json > old_results.json

# Compare with current
python scripts/compare_results.py
```

## Example Scenarios

### Scenario 1: Driver Update

**Before update:**
```bash
# Run baseline
python scripts/test_all_gpus.py --benchmark --stress
git add results/*.json
git commit -m "RTX 3090 - Driver 590.48.01 baseline"
git tag driver-590.48.01
```

**After update:**
```bash
# Update driver to 595.29
# Reboot
# Run tests again
python scripts/test_all_gpus.py --benchmark --stress
git add results/*.json
git commit -m "RTX 3090 - Driver 595.29.00 - 5% performance improvement"
git tag driver-595.29.00

# Compare
git diff driver-590.48.01 driver-595.29.00 -- results/
```

### Scenario 2: Testing 4 Cards

```bash
# Card 1: RTX 3090
python scripts/test_all_gpus.py --benchmark --stress
git add results/*RTX_3090*.json
git commit -m "Card 1: RTX 3090 XC3 ULTRA - baseline"
git tag card1-rtx3090

# Card 2: RTX 4090 (after swap)
python scripts/test_all_gpus.py --benchmark --stress
git add results/*RTX_4090*.json
git commit -m "Card 2: RTX 4090 FTW3 ULTRA - baseline"
git tag card2-rtx4090

# Card 3: RTX 3080 (after swap)
python scripts/test_all_gpus.py --benchmark --stress
git add results/*RTX_3080*.json
git commit -m "Card 3: RTX 3080 TUF GAMING - baseline"
git tag card3-rtx3080

# Card 4: RTX 3070 (after swap)
python scripts/test_all_gpus.py --benchmark --stress
git add results/*RTX_3070*.json
git commit -m "Card 4: RTX 3070 GAMING X - baseline"
git tag card4-rtx3070

# View all card tests
git log --oneline --decorate
```

### Scenario 3: Thermal Issue Investigation

```bash
# Initial baseline (good cooling)
python scripts/test_all_gpus.py --benchmark --stress --duration 1800
git add results/*.json
git commit -m "RTX 3090 - Good cooling, 73°C under load"

# (Dust accumulates over months)

# Re-test later
python scripts/test_all_gpus.py --benchmark --stress --duration 1800
git add results/*.json
git commit -m "RTX 3090 - 6 months later, 82°C under load, 5% slower"

# Compare
git diff HEAD~1 HEAD -- results/
# You'll see higher temps and lower performance in the JSON
```

## Using Git Tags for Milestones

Tags help mark important benchmarks:

```bash
# Tag baseline results
git tag -a baseline-2026-01 -m "January 2026 baseline benchmarks"

# Tag after major change
git tag -a post-cooler-upgrade -m "After installing better cooler"

# List all tags
git tag -l

# View tag details
git show baseline-2026-01

# Compare with tag
git diff baseline-2026-01 HEAD -- results/
```

## Organizing Commits

### Good Commit Messages

**Good:**
```
RTX 3090 XC3 ULTRA - baseline benchmarks (420W, 73°C load)
RTX 4090 FTW3 ULTRA - 95% faster than RTX 3090
RTX 3090 - After driver 595.29 update: +3% performance
RTX 3090 - Thermal paste replaced: -8°C under load
```

**Not as helpful:**
```
Updated results
New benchmarks
Test
```

### Commit Structure

```bash
# Each card gets its own commit
git commit -m "Card 1: RTX 3090 XC3 ULTRA baseline"

# Driver updates are separate commits
git commit -m "RTX 3090 - Driver 595.29: +3% performance"

# Hardware changes are separate commits
git commit -m "RTX 3090 - New thermal paste: -8°C temps"
```

## Viewing History

### See all result commits
```bash
git log --oneline -- results/
```

### See detailed changes
```bash
git log -p -- results/
```

### Graph view
```bash
git log --graph --oneline --all --decorate
```

### Filter by GPU model
```bash
git log --grep="RTX 3090" --oneline
git log --grep="RTX 4090" --oneline
```

## Advanced: Branching for Experiments

If you're testing different configurations:

```bash
# Create branch for overclocking tests
git checkout -b overclocking-tests

# Run OC tests
python scripts/test_all_gpus.py --benchmark --stress
git add results/*.json
git commit -m "RTX 3090 - +150MHz core, +500MHz mem"

# Return to main
git checkout main

# Compare OC vs stock
git diff main overclocking-tests -- results/
```

## JSON Diff Example

When you run `git diff` on JSON result files, you'll see:

```diff
diff --git a/results/benchmark_GPU0_RTX_3090.json b/results/benchmark_GPU0_RTX_3090.json
@@ -15,7 +15,7 @@
   "matmul": [
     {
       "size": 8192,
-      "gflops": 25493.0,
+      "gflops": 26204.5,
       "avg_time_ms": 43.13
     }
   ]
```

This shows performance improved from 25,493 to 26,204 GFLOPS!

## Best Practices

1. **Commit after each test session** - Don't let results pile up
2. **Use descriptive messages** - Include GPU model, changes, temps
3. **Tag important milestones** - Baselines, driver updates, hardware changes
4. **Don't delete old results** - Keep history for comparison
5. **Archive in branches** - Move very old results to archive branches if needed

## Summary

✅ Result files are tracked in Git
✅ You can see performance changes over time
✅ Easy to compare before/after any change
✅ Full history of all GPU tests preserved
✅ Tags help mark important milestones

**Your current results are ready to commit:**
```bash
cd gpu_benchmarks
git add results/*.json
git commit -m "Initial RTX 3090 XC3 ULTRA baseline benchmarks"
git push
```

Now whenever you re-run tests, Git will track the differences! 📊
