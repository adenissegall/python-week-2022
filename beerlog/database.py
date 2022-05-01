from sqlmodel import create_engine
import models
from config import settings

engine = create_engine(settings.database.url)

models.SQLModel.metadata.create_all(engine)