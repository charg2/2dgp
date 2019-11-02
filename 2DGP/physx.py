import Const;

class Physx:
    def __init__(self):
        self.mass = 1; # 1kg

        self.velocity_x = 0;
        self.velocity_y = 0;

        self.friction_x = 0;
        self.friction_y = 0;
       
        self.force_x = 0;
        self.force_y = 0;
               
        self.accelation_x = 0;
        self.accelation_y = 0;

        self.gravimetric_unit = 980.665/1.13; # 980.665m/s2 -> 100cm/s
        self.isfalling = True;
    
    def set_falling(self, bool) -> None:
        self.isfalling = bool;
        return;

    def set_mass(self,mass) -> None:
        self.mass = mass;
        return;

    def set_velocity(self,x,y) -> None:
        self.velocity_x += x;
        self.velocity_y += y;
        return;

    def get_velocities(self) -> tuple:
        return self.velocity_x, self.velocity_y;

    def set_force(self,x,y) :
        self.force_x = x;
        self.force_y = y;
        return;  

    def is_falling(self):
        return self.is_falling;

    def get_can_jump(self) -> bool :
        return 0 == self.velocity_y;

    # Example Physx.calc_length_from_origin(vec_x, vec_y) ;
    def calc_length_from_origin(vec_x, vec_y) -> float:
        return ((vec_x * vec_x) + (vec_y * vec_y)) ** 1/2;

if "__main__" == __name__ :
    p:Physx = Physx();
    print(p.get_can_jump());
    print(p.set_velocity(1, 2));
    print(p.get_velocities());
    #print(type(Physx.calc_length_from_origin(2.3, 3.1)));
    print(Physx.calc_length_from_origin(2.3, 3.1));