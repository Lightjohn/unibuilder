from system.cmd import exec_cmd, create_make_cmd
from .base import Base


class Autotools(Base):
    files = ["autogen.sh"]

    def init(self):
        exec_cmd("sh", "autogen.sh")
        exec_cmd("sh", "configure")

    def compile(self):
        exec_cmd(*create_make_cmd())

    def install(self):
        pass

    def __str__(self):
        return "Build system: Autotools"
