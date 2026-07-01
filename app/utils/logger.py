from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "{message}",
    level="INFO"
)

logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO"
)