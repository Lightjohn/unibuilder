from .base import Base


class Dnf(Base):

    @staticmethod
    def is_valid(installed_binaries):
        if "dnf" in installed_binaries:
            return True
        return False

    def __str__(self):
        return "System is Fedora like"
