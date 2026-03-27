from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime
import os

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Tiered Context
    l0_strategy = Column(Text)
    l1_architecture = Column(Text)
    
    # Hardware Profiles
    hardware_profile = Column(String) # e.g., 'RTX_5090', 'JETSON_ORIN'
    # LLM Configuration
    llm_provider = Column(String, default="local") # Default to 5090
    main_model = Column(String, default="deepseek-coder-v2:16b")
    swarm_model = Column(String, default="llama3.1:8b")
    api_key = Column(String) # Optional

    checkpoints = relationship("Checkpoint", back_populates="project")

class Checkpoint(Base):
    __tablename__ = 'checkpoints'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    # State Data
    active_persona = Column(String)
    mental_state_summary = Column(Text) # AI's current "thoughts"
    code_diff = Column(Text)
    
    project = relationship("Project", back_populates="checkpoints")

# Database initialization
# Use absolute path so it works from any directory
DB_PATH = "/home/tmainetucker/Repos/nexus/data/nexus.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
engine = create_engine(f'sqlite:///{DB_PATH}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
