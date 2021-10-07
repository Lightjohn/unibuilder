from .base import Base


class Apt(Base):

    @staticmethod
    def is_valid(installed_binaries):
        if "apt-get" in installed_binaries:
            return True
        return False

    def __str__(self):
        return "System is Debian-Ubuntu like"
