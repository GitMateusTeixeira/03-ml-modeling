from kedro.pipeline import node, Pipeline, pipeline
from . import nodes


def create_pipeline(**kwargs) -> Pipeline:

    return pipeline(
        [
            node(
                func=nodes.get_data,
                inputs=None,
                outputs='raw_data_downloaded',
                name='get_data',
            )
        ]
    )