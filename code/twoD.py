# basically just two dimension file hehehe hahahaha



class Vector2:
    # Vector2 is base class for storing data X, Y
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    # methods and stuff

    @staticmethod
    def zero():
        return Vector2(0, 0)
    


    @staticmethod 
    def is_vector(v): return isinstance(v, Vector2)

    @staticmethod
    def length(v): # really just gets a vectors distance from 0,0
        return ((v.x*v.x) + (v.y*v.y)) ** 0.5 
    
    @staticmethod
    def normalize(v):
        len = Vector2.length(v)
        if len == 0: return Vector2.zero() # if len == 0 return 0,0 vector2
        return Vector2(v.x/len, v.y/len)

    @staticmethod
    def move(s, e, d):
        dir = Vector2.normalize(Vector2(e.x - s.x, e.y - s.y)) # get normalized dir from s -> e
        return Vector2(
            s.x + dir.x * d,
            s.y + dir.y * d
        )

    @staticmethod
    def rmove(s, e, d, xr=None, yr=None):
        if xr == None: xr = e.x
        if yr == None: yr = e.x

        m = Vector2.move(s, e, d)
        if m.x > xr: m.x = xr
        if m.y > yr: m.y = yr
        return m

class Box:
    # box is dynamic class with 4 vector2. restricted, mostly used for hitboxes. can rotate
    # only 4 vertices, i make triangle later so polygons
    # more effiencient than 2 triangles ( i think )
    def __init__(self, p1, p2, p3, p4):
        # p1 -> p4 are all vector2

        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4



class TDM:
    # static method class for math thats helpful for twoD file

    @staticmethod
    def slope(p1, p2):
        return Vector2(p2.x - p1.x, p2.y - p1.y)
    
    @staticmethod
    def is_perpendictular(p1, p2, o):
        s1 = TDM.slope(p1, p2)
        return Vector2(-s1.y, -s1.y) == TDM.slope(p2, p1)


        
