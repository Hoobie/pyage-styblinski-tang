class VectorGenotype(object):
    def __init__(self, x, y, z, s, t):
        super(VectorGenotype, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        self.s = s
        self.t = t
        self.fitness = None

    def __str__(self):
        return "(%s, %s, %s, %s, %s), f:%s" % (self.x, self.y, self.z, self.s, self.t, self.fitness)
    def __repr__(self):
        return self.__str__()