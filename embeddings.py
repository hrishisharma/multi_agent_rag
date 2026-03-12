import os
from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings


def _configure_hf_logging() -> None:
    # Silence noisy HF/transformers advisory logs (e.g. load reports for benign keys)
    os.environ.setdefault("TRANSFORMERS_NO_ADVISORY_WARNINGS", "1")
    try:
        from transformers.utils import logging as hf_logging  # type: ignore

        hf_logging.set_verbosity_error()
        hf_logging.disable_progress_bar()
    except Exception:
        # If transformers isn't installed directly (or API differs), keep going.
        pass

    # Silence HF Hub warnings (e.g. unauthenticated request advisory).
    try:
        from huggingface_hub.utils import logging as hub_logging  # type: ignore

        hub_logging.set_verbosity_error()
        hub_logging.disable_progress_bars()
    except Exception:
        pass


@lru_cache(maxsize=1)
def get_embeddings() -> HuggingFaceEmbeddings:
    _configure_hf_logging()
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

