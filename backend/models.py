from pydantic import BaseModel


class UserProfile(BaseModel):
    state: str
    business_type: str
    num_employees: int


class GenerateRequest(BaseModel):
    query: str
    user_profile: UserProfile
    topic:  str
