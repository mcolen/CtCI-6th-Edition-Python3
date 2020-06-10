"""Solution to 4.7 Build Order.

You are given a list of projects and a list of dependencies (which is a
list of pairs of projects, where the second project is dependent on the
first project). All of a project's dependencies must be built before the
project is. Find a build order that will allow the projects to be built.
If there is no valid build order, return an error.

EXAMPLE
Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""

from typing import List, Tuple, TypeVar, Sequence


class NoValidBuildOrderError(Exception):
    """Raised when there is a circular dependency in given projects."""


T = TypeVar('T')


def build_order(projects: Sequence[T],
                dependencies: Sequence[Tuple[T, T]]) -> List[T]:
    """Finds a build order that will allow projects to be built.

    Args:
        projects: A sequence of "projects" (which could be anything).
        dependencies: List of pairs of projects where the second project
            is dependent on the first project.

    Returns:
        List of projects in an order such that they could all be built
            subject to given dependencies.

    Raises:
        NoValidBuildOrderError: There was a cycle in given dependencies.
    """
    order = []
    dep_count = {project: 0 for project in projects}
    for _, dependant in dependencies:
        dep_count[dependant] += 1
    unblocked = {project for project, count in dep_count.items() if count == 0}

    while unblocked:
        project = unblocked.pop()
        order.append(project)
        dependants = [
            dependant for dependency, dependant in dependencies
            if dependency == project
        ]
        for dependant in dependants:
            dep_count[dependant] -= 1
            if not dep_count[dependant]:
                unblocked.add(dependant)

    if len(order) < len(projects):
        raise NoValidBuildOrderError()
    return order
