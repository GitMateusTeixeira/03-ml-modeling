from kedro.pipeline import node, Pipeline, pipeline
from . import nodes  # Importando o arquivo nodes que contém a função read_data


def create_pipeline(**kwargs) -> Pipeline:
    """
    Cria o pipeline responsável por extrair features dos dados de desenvolvimento e produção,
    dividir os dados de desenvolvimento em treino e teste, treinar modelos e realizar inferência.

    Returns:
        Pipeline: Pipeline completo de extração de features, divisão de dados, treinamento e inferência.
    """
    return Pipeline(
        [
            # Node para extração de features dos dados de desenvolvimento
            node(
                func=nodes.featuring,
                inputs=["data_filtered_dev", "params:dev_suffix"],
                outputs=["x_features_dev", "y_features_dev"],
                name="extract_dev_features_node",
            ),

                        # Node para extração de features dos dados de produção
            node(
                func=nodes.featuring,
                inputs=["data_filtered_prod", "params:prod_suffix"],
                outputs=["x_features_prod", "y_features_prod"],
                name="extract_prod_features_node",
            ),
        ]
    )