from kedro.pipeline import Pipeline
from .pipelines import get_data, read_data, featuring, splitter, trainer

def register_pipelines() -> dict[str, Pipeline]:

    get_data_pipeline = get_data.create_pipeline() # pasta + nome da função
    read_data_pipeline = read_data.create_pipeline()
    featuring_pipeline = featuring.create_pipeline()
    splitter_pipeline = splitter.create_pipeline()
    trainer_pipeline = trainer.create_pipeline()

    return {
        'get_data': get_data_pipeline,  # dicionario com as funções
        'read_data': read_data_pipeline,
        'featuring': featuring_pipeline,
        'splitter': splitter_pipeline,
        'trainer': trainer_pipeline,

        "__default__": (
            get_data_pipeline
            + read_data_pipeline
            + featuring_pipeline
            + splitter_pipeline
            + trainer_pipeline
        ),
    }
