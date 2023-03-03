import uvicorn
from .settings import settings

uvicorn.run(
    'money_movement.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True  # Перезагрузка сервера при обновлении кода
)