"""Configuracion principal de la aplicacion FastAPI."""

from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    description="API para gestionar tareas asignadas a usuarios usando FastAPI y persistencia en JSON.",
    version="1.0.0",
)

# Se registra cuando el router de tareas este disponible en la siguiente fase.
try:
    from app.routes.task_routes import router as task_router
except ImportError:
    task_router = None

if task_router is not None:
    app.include_router(task_router)
