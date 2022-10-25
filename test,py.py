# import numpy as np;

# print(np.__file__)
# print(np.__version__)

# import tensorflow as tf;
# print(tf.__version__)

# print(tf.config.list_physical_devices("GPU"))

import sys

import tensorflow.keras
# import numpy as np;
# import pandas as pd
# import sklearn as sk
import tensorflow as tf

print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
# print(f"Pandas {pd.__version__}")
# print(f"Scikit-Learn {sk.__version__}")
print("GPU is", "available" if tf.test.is_gpu_available() else "NOT AVAILABLE")