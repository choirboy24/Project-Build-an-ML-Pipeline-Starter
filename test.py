import json
import mlflow
import tempfile
import os
import wandb
import hydra
import networkx.algorithms.dag
from omegaconf import DictConfig

@hydra.main(config_path='.', config_name='config', version_base=None)
def main():
    root_path = os.getcwd()

    train_path = os.path.abspath(os.path.join(root_path, "src/train_random_forest"))

    rf_config = os.path.abspath("rf_config.json")
    with open(rf_config, "w+") as fp:
        json.dump(dict(config["modeling"]["random_forest"].items()), fp) 

    date_feature = rf_config["features"]['date']
    nlp_feature = rf_config["features"]['nlp']
    print(date_feature)
    print(nlp_feature)

if __name__ == "__main__":
    main()