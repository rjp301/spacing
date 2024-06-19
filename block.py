from dataclasses import dataclass


@dataclass
class Block:
    beg: float
    end: float
    gov: str = "beg"
    # Governing dimension determining order
    # Can be mid, beg, or end

    def __post_init__(self):
        self.mid = (self.beg + self.end) / 2
        self.len = abs(self.end - self.beg)

    def dist_other(self, other):
        getattr(self, self.gov)
        getattr(other, self.gov)
