
def load_dict(
    dir_path=None,
    level=None,
):
    return f'from {dir_path}.hero{str(level)}.source import HERO'

_import = load_dict(
    dir_path='config.sources.heroes',
    level=1,
)

_import

