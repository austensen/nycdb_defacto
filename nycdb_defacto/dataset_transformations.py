from nycdb.dataset_transformations import to_csv


def defacto_exclude_bbls(dataset):
    return to_csv(dataset.files[0].dest)
