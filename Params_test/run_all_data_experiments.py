import subprocess
import uuid

def run_experiment(model, max_steps, dataset, use_best_hyperparams, run_repeats_and_cv):
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
    
    subprocess.run(command)

if __name__ == "__main__":
    
    # wpfs, dietnetworks , cae, fsnet
    model = "wpfs"    # you can change this
    max_steps = 100
    use_best_hyperparams = True
    run_repeats_and_cv = True
    
    datasets = [
        'metabric-pam50', 'metabric-dr', 'tcga-2ysurvival', 'tcga-tumor-grade',
        'lung', 'prostate', 'toxicity', 'cll', 'smk'
    ]
    
    for dataset in datasets:
        run_experiment(model, max_steps, dataset, use_best_hyperparams, run_repeats_and_cv)
