from dataclasses import dataclass, asdict


@dataclass
class MyConfig:
    PORT: int = 5000
    HOST: str = '0.0.0.0'

    def to_dict(self) -> dict:
        return asdict(self)


def get_config() -> MyConfig:
    return MyConfig()


config = get_config()
