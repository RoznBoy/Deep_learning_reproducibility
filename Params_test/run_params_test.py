import subprocess
import uuid
from itertools import product

# Define the parameter grid
param_grid = {
    'lr': [3e-2, 3e-3, 3e-4],
    'batch_size': [8,16],
    'dropout_rate': [0.1, 0.3, 0.5],
    'weight_decay': [1e-4, 1e-5, 0],

}

def run_experiment(model, max_steps, dataset, use_best_hyperparams, run_repeats_and_cv, **kwargs):
    experiment_name = f"experiment_{dataset}_{uuid.uuid4().hex[:8]}"
    
    command = [
        "python", "../src/params_test_main.py",
        "--model", model,
        "--max_steps", str(max_steps),
        "--dataset", dataset,
        "--experiment_name", experiment_name
    ]
    
    if use_best_hyperparams:
        command.append("--use_best_hyperparams")
    if run_repeats_and_cv:
        command.append("--run_repeats_and_cv")
    
    for key, value in kwargs.items():
        command.append(f"--{key}")
        command.append(str(value))
    
    subprocess.run(command)

def main():
    model = "wpfs"
    max_steps = 100
    use_best_hyperparams = True
    run_repeats_and_cv = True
    
    datasets = [
        
        'lung', 'prostate', 'toxicity', 'cll', 'smk'
    ]
    
    keys, values = zip(*param_grid.items())
    for dataset in datasets:
        for param_values in product(*values):
            params = dict(zip(keys, param_values))
            run_experiment(model, max_steps, dataset, use_best_hyperparams, run_repeats_and_cv, **params)

if __name__ == "__main__":
    main()
