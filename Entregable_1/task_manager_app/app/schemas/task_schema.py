"""Esquemas Pydantic para validar datos de tareas."""

from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field, field_validator

PriorityValue = Literal["baja", "media", "alta", "bloqueante"]
StatusValue = Literal["pendiente", "en progreso", "en revisión", "completada"]


class TaskCreate(BaseModel):
    """Datos requeridos para crear una tarea."""

    title: str
    description: str
    priority: PriorityValue
    effort_hours: Decimal = Field(ge=0)
    status: StatusValue
    assigned_to: str

    @field_validator("title", "assigned_to")
    @classmethod
    def validate_non_empty_text(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Este campo no debe estar vacío.")
        return value


class TaskUpdate(BaseModel):
    """Datos opcionales para actualizar una tarea."""

    title: str | None = None
    description: str | None = None
    priority: PriorityValue | None = None
    effort_hours: Decimal | None = Field(default=None, ge=0)
    status: StatusValue | None = None
    assigned_to: str | None = None

    @field_validator("title", "assigned_to")
    @classmethod
    def validate_optional_non_empty_text(cls, value: str | None) -> str | None:
        if value is not None and not value.strip():
            raise ValueError("Este campo no debe estar vacío.")
        return value


class TaskResponse(BaseModel):
    """Datos devueltos por la API para una tarea."""

    id: str
    title: str
    description: str
    priority: PriorityValue
    effort_hours: Decimal = Field(ge=0)
    status: StatusValue
    assigned_to: str
