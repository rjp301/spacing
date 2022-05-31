from dataclasses import dataclass

@dataclass
class Block:
  beg: float
  end: float

  def __post_init__(self):
    self.mid = (self.beg + self.end)/2
    self.len = abs(self.end - self.beg)

  