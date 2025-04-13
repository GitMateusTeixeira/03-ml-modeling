from kedro.pipeline import node, Pipeline, pipeline
from . import nodes  # Importando o arquivo nodes que contém a função read_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            # Node para processar o arquivo de desenvolvimento
            node(
                func=nodes.read_data,
                inputs=dict(file_name="params:dev_file_name", output_suffix="params:dev_suffix"),
                outputs="intermediate_data_dev",
                name="process_dev_data_node",
            ),
            
            # Node para processar o arquivo de produção
            node(
                func=nodes.read_data,
                inputs=dict(file_name="params:prod_file_name", output_suffix="params:prod_suffix"),
                outputs="intermediate_data_prod",
                name="process_prod_data_node",
            ),
        ]
    )