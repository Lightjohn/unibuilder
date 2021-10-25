from .base import Base


class Cargo(Base):
    def is_valid(self, local_files):
        pass

    def init(self):
        pass

    def compile(self):
        pass

    def install(self):
        pass

    def __str__(self):
        return "Build system: Cargo / Rust"
