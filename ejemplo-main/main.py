import logging
import sklearn


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Hello World")
logger.info(f"Scikit-learn version: {sklearn.__version__}")