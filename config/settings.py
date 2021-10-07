requirements = ["git"]


def check_system_requirement(system_binaries):
    missing = list()
    for requirement in requirements:
        if requirement not in system_binaries:
            missing.append(requirement)
    return missing
