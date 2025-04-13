import mlflow
from kedro.framework.hooks import hook_impl
from kedro.pipeline.node import Node
import logging

logger = logging.getLogger(__name__)

class MlflowHooks:
    @hook_impl
    def before_pipeline_run(self, run_params: dict) -> None:
        # Executar antes do pipeline começar
        experiment_name = "infnet_04_ml_engineering_pd"
        experiment = mlflow.get_experiment_by_name(experiment_name)

        if not experiment:
            mlflow.create_experiment(experiment_name)
            logger.info(f"Experimento '{experiment_name}' criado com sucesso.")

        else:
            logger.info(f"Experimento '{experiment_name}' já existe. Reutilizando.")

        mlflow.set_experiment(experiment_name)

    @hook_impl
    def before_node_run(self, node: Node) -> None:
        # Inicia um run para cada nó
        run_name = node.name or "unnamed_node"

        mlflow.start_run(run_name=run_name, nested=True)
        mlflow.set_tag("project_name", "projeto-ml-kobe")
        mlflow.set_tag("stage", node._namespace.split(".")[-1] if node._namespace else "unknown")
        
        logger.info(f"Iniciando run para o nó: {run_name}")

    @hook_impl
    def after_node_run(self, node: Node) -> None:
        # Finaliza o run após cada nó
        mlflow.end_run()
        logger.info(f"Run finalizado para o nó: {node.name}")