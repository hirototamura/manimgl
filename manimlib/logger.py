import logging

from rich.logging import RichHandler

__all__ = ["log", "logger"]


FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.WARNING, format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("manimgl")
logger = log  # Alias for compatibility with manim_voiceover
