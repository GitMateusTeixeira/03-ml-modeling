from kedro.pipeline import node, Pipeline, pipeline
from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # Node para treinar e avaliar os modelos com os dados de desenvolvimento
        node(
            func=nodes.trainer,
            inputs=["X_train", "y_train", "X_test", "y_test"],
            outputs=dict(
                decision_tree_model="decision_tree_model",
                logistic_regression_model="logistic_regression_model",
                results_file="results_file",
            ),
            name="trainer",
        ),

        # Node para realizar inferência nos dados de produção
        node(
            func=nodes.inference,
            inputs=[
                    "decision_tree_model",  # Modelo de árvore de decisão
                    "logistic_regression_model",  # Modelo de regressão logística
                    "x_features_prod",  # Dados de produção (X)
                    "y_features_prod"
                ],
            outputs="predictions",
            name="inference",
            ),
        ]
    )