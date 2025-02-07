from backend.cli import cli
from Nipuna import Nipuna

if __name__ == '__main__':
    nipuna_client = Nipuna()
    nipuna_client.init_yaml("nipuna/sample.yaml")
    # cli()