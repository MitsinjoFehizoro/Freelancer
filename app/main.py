from pydantic import ValidationError
from uuid import uuid4
from .models.profile import Profile
from .models.project import Project
from datetime import date

data_client = {
    "id": uuid4(),
    "username": "mitsinjo",
    "email": "mitsinjo@gmail.com",
    "role": "client",
    "bio": "client mahafatrapo",
    "skills": ["python", "java"],
}

data_freelancer = {
    "id": uuid4(),
    "username": "rakoto",
    "email": "rakoto@gmail.com",
    "role": "freelancer",
    "hourly_rate": "50",
    "bio": "freelancer mahafatrapo",
    "skills": ["python", "javascript"],
}


data_project = {
    "title": "teste",
    "description": "teste tesste teste teste",
    "budget": 500,
    "deadline": date(2025, 4, 17),
}

print("---------------------------------- Debut ----------------------------------\n")
try:
    print("=============== CLIENT ===============")
    client = Profile.model_validate(data_client)
    print(f"{client}\n")

    print("=============== FREELANCER ===============")
    freelancer = Profile.model_validate(data_freelancer)
    print(f"{freelancer}\n")

    print("=============== PROJECT ===============")
    data_project["client"] = client
    data_project["freelancer"] = freelancer
    project = Project.model_validate(data_project)
    print(f"{project}\n")


except ValidationError as e:
    print(e)

print("---------------------------------- Fin ----------------------------------\n")
