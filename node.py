from dataclasses import dataclass


@dataclass
class Node:
    x: float
    data: any

    def dist_other(self, other):
        return other.x - self.x
