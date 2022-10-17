class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, len_to_set):
        if not isinstance(len_to_set, float):
            raise Exception("Parameter is float")
        if len_to_set < 0.0 or len_to_set > 20.0:
            raise Exception("New length 'x' must be 0.0 < x < 20.0")
        self._length = len_to_set

    @width.setter
    def width(self, width_to_set):
        if not isinstance(width_to_set, float):
            raise Exception("Parameter is float")
        if width_to_set < 0.0 or width_to_set > 20.0:
            raise Exception("New length 'x' must be 0.0 < x < 20.0")
        self._width = width_to_set

    def __str__(self):
        return f"Width = {self.width}\nLength = {self.length}"
