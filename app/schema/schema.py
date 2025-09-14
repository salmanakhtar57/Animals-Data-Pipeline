from pydantic import BaseModel

class PipelineResponse(BaseModel):
    status: str
    fetched_file: str
    fetched: int
    posted: int
