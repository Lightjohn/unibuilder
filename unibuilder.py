import argparse
import os
import sys

from config.settings import check_system_requirement
from system.dependency import get_bins_from_path
from system.uri import is_git_url, is_local_uri
from system.cmd import clone_or_pull_git, INVALID_INPUT, MISSING_DEPS, INVALID_SYSTEM, INVALID_BUILD_TOOLS
from tools import Autotools, Cargo, Cmake, Go, Makefile, Qmake
from tools import Apt, Dnf, Pacman


def check_basic_requirements(system_binaries):
    missing = check_system_requirement(system_binaries)
    if missing:
        print(f"Please first install: {', '.join(missing)}")
        sys.exit(MISSING_DEPS)


def parse_args():
    parser = argparse.ArgumentParser(description='Build any software from git')
    parser.add_argument('uri', help='can be a local path or a git url')
    parser.add_argument('-o', help='Destination, where should we output data', required=False, default=None)
    parser.add_argument('-y', help='Assume yes for any question', default=False)
    parser.add_argument('-i', help='Install to system (will need sudo)', default=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    uri = args.uri
    ask = args.y
    destination = args.o

    # Checking system for basic tools
    installed_binaries = get_bins_from_path()
    check_basic_requirements(installed_binaries)

    # Cloning or going to directory
    if is_git_url(uri):
        clone_or_pull_git(uri, destination)
    elif is_local_uri(uri):
        # Nothing to do (for now, maybe pull if git?)
        pass
    else:
        print("Unrecognised input:", uri)
        sys.exit(INVALID_INPUT)

    # Trying to detect os (debian like, arch, fedora...)
    pm = None
    for package_manager in [Apt, Dnf, Pacman]:
        pm = package_manager()
        if pm.is_valid(installed_binaries):
            break
    else:
        print("Could not recognise system")
        sys.exit(INVALID_SYSTEM)
    print(pm)

    # Trying to detect uri build system
    # listdir or walk?
    local_files = os.listdir(destination)

    # order matter for compiling system: ie CMakeList can use another (qmake) so should be first
    ct = None
    for compiling_tool in [Autotools, Cargo, Cmake, Go, Makefile, Qmake]:
        ct = compiling_tool()
        if ct.is_valid(local_files):
            break
    else:
        print("Could not guess compilation tool used...")
        sys.exit(INVALID_BUILD_TOOLS)
    print(ct)

    # At this point we have system (pm) and build (tool)

    # Extracting details from README if any to solve dependencies
    os.chdir(destination)

    # Start compilation
    ct.init()
    ct.compile()

    # start install if asked
    if args.i:
        ct.install()

    # Done


