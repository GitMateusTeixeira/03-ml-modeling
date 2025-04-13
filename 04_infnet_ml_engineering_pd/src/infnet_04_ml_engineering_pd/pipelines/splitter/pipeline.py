from kedro.pipeline import node, Pipeline, pipeline
from . import nodes  # Importando o arquivo nodes que contém a função read_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
        # Node para dividir os dados de desenvolvimento em treino e teste
        node(
            func=nodes.split_data,
            inputs=dict(x_features_file="x_features_dev", y_features_file="y_features_dev"),
            outputs=dict(
                x_train="x_train",
                x_test="x_test",
                y_train="y_train",
                y_test="y_test"
                ),
                
                name="split_dev_data_node",
            ),
        ]
    )