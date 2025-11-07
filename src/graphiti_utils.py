from rich.pretty import pprint

from graphiti_core.edges import EntityEdge

def pretty_print(entity: EntityEdge | list[EntityEdge]):
    if isinstance(entity, EntityEdge):
        data = {k: v for k, v in entity.model_dump().items() if k != 'fact_embedding'}
    elif isinstance(entity, list):
        data = [{k: v for k, v in e.model_dump().items() if k != 'fact_embedding'} for e in entity]
    else:
        pprint(entity)
        return
    pprint(data)