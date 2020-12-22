import os
from tensorflow.keras.preprocessing import image_dataset_from_directory

from cnn_model import config


def create_dataset(*, batch_size=32, random_seed=42):
    train_ds = image_dataset_from_directory(
        os.path.join(config.DATASET_DIR, 'train'),
        validation_split=0.2,
        subset="training",
        seed=random_seed,
        batch_size=batch_size)

    val_ds = image_dataset_from_directory(
        os.path.join(config.DATASET_DIR, 'train'),
        validation_split=0.2,
        subset="validation",
        seed=random_seed,
        batch_size=batch_size)

    test_ds = image_dataset_from_directory(
        os.path.join(config.DATASET_DIR, 'test'),
        seed=random_seed,
        batch_size=batch_size)

    return train_ds, val_ds, test_ds