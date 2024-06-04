import subprocess
import uuid
import os

# Set environment variable
os.environ['PYTHONIOENCODING'] = 'utf-8'

# Define the feature_extractor_dims and layers_for_hidden_representation grids
feature_extractor_dims_grid3 = [  # for dim ==3 
    [100, 100, 30],
    [100, 100, 50],
    [100, 100, 100]
]


feature_extractor_dims_grid2 = [  # for dim == 2
    [100, 30],
    [100, 50],
    [100, 100]
]

layers_for_hidden_representation_grid3 = [3]

layers_for_hidden_representation_grid2 = [2]

def run_experiment(model, max_steps, dataset, use_best_hyperparams, run_repeats_and_cv, **kwargs):
    experiment_name = f"experiment_{dataset}_{uuid.uuid4().hex[:8]}"
    
    command = [
        "python", "src/main.py",
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
        if isinstance(value, list):
            command.append(f"--{key}")
            command.extend(map(str, value))
        else:
            command.append(f"--{key}")
            command.append(str(value))
    
    subprocess.run(command)

def main():
    models = ["remove_SPN_wpfs", "remove_WPN_wpfs", "wpfs"]
    max_steps = 100
    use_best_hyperparams = True
    run_repeats_and_cv = True
    
    datasets = [
        'lung', 'prostate', 'toxicity', 'cll', 'smk'
    ]
    for model in models:
        for dataset in datasets:
            for feature_extractor_dims in feature_extractor_dims_grid2:
                for layers_for_hidden_representation in layers_for_hidden_representation_grid2:
                    params = {
                        'feature_extractor_dims': feature_extractor_dims,
                        'layers_for_hidden_representation': layers_for_hidden_representation
                    }
                    run_experiment(model, max_steps, dataset, use_best_hyperparams, run_repeats_and_cv, **params)
                    
    for model in models:
        for dataset in datasets:
            for feature_extractor_dims in feature_extractor_dims_grid3:
                for layers_for_hidden_representation in layers_for_hidden_representation_grid3:
                    params = {
                        'feature_extractor_dims': feature_extractor_dims,
                        'layers_for_hidden_representation': layers_for_hidden_representation
                    }
                    run_experiment(model, max_steps, dataset, use_best_hyperparams, run_repeats_and_cv, **params)

if __name__ == "__main__":
    main()