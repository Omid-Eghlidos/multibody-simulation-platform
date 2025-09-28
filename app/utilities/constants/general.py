"""
general.py
----------
Defines general-purpose constant values used across the application.
Includes configuration parameters such as the number of warmups and repetitions.
"""


class General:
    """
    General
    -------
    Contains general constants for configurable application parameters.

    Attributes
    ----------
    NO_OF_WARMUPS : int
        Number of warm-up iterations before main processing.
    NO_OF_REPS : int
        Number of repetitions to execute during benchmarking or testing.
    """

    NO_OF_WARMUPS: int = 0
    NO_OF_REPS: int = 10
    TMP_PATH: str = '/tmp/image_processing'
    LOCAL_MODEL_PATH: str = 'app/models/'
    S3_BUCKET: str = 'isloth-models'