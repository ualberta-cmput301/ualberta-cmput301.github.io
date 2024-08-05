from bpyutils.model.package import Package

def get_locale():
    return "es"

def generate_translations(path, target_dir = None, check = False):
    package = Package.from_path(path)