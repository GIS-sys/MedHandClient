class Action:
    MOVE = "MOVE"

    def __init__(self, kind, *args, **kwargs):
        self.kind = kind
        self.fields = []
        if kind == Action.MOVE:
            self.dx = kwargs["dx"]
            self.dy = kwargs["dy"]
            self.fields = ["dx", "dy"]

    def __repr__(self):
        res = f"Action{self.kind}("
        for k in self.fields:
            res += f"{k}={getattr(self, k)},"
        res += ")"
        return res
