from .base import Base


class Pacman(Base):

    @staticmethod
    def is_valid(installed_binaries):
        if "pacman" in installed_binaries:
            return True
        return False

    def __str__(self):
        return "System is Arch Linux"
