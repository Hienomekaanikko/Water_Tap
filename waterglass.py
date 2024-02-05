class WaterGlass:
    def __init__(self):
        self.dl = 0
    def fill_glass(self):
        self.dl += 1
        if self.dl < 2:
            return f"the glass is not full yet."
        elif self.dl >= 2:
            return f"the glass is full."
        else:
            return f"the glass is overflowing."
    def empty_glass(self):
        return f"glass is now empty."
