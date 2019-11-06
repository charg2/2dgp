import Const;

class Physx:
    def __init__(self):
        #self.mass = 1; # 1kg
        self.velocity_x = 0;
        self.velocity_y = 0;

        self.force_x = 0;
        self.force_y = 0;
        
        self.angle_rate = 0;

        self.is_ground:bool = True;
        self.epsilon_in_physx:float = 1.0;
        
        self.has_grivity = False;
        self.acceleration_of_gravity:float = 0.0;
    

    def set_falling(self, bool) -> None:
        self.isfalling = bool;
        return;

    def set_mass(self, mass) -> None:
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

    def is_falling(self) -> bool:
        return self.is_falling;

    def get_can_jump(self) -> bool :
        return 0 == self.velocity_y;

    # Example Physx.calc_length_from_origin(vec_x, vec_y) ;
    def calc_length_from_origin(vec_x, vec_y) -> float:
        return ((vec_x * vec_x) + (vec_y * vec_y)) ** 1/2;

    ## f = ma 
    ## a = f / m
    ## 1N = 1kg m/s^2
    #def calc_accelation(self, time:float) -> None:
    #    self.accelation_x = (self.force_x/self.mass) * time;
    #    self.accelation_y = (self.force_y/self.mass) * time;
    #    return;

    #def calc_velocity(self, Time):
        
    #    # velocity = previous velocity + (time * accelation);
    #    self.calc_accelation(Time);
    #    self.set_velocity(self.accelation_x * Time, self.accelation_y * Time);
        
    #    if True == self.is_falling:
    #        self.set_velocity(self.friction_x * Time, -self.gravimetric_unit * Time*Time);
    #    else:
    #        if( abs(self.velocity_y) > self.epsilon_in_physx):
    #            self.velocity_y =self. repulsive_coef*-self.velocity_y; 
    #            self.set_velocity(self.friction_x * Time,0);
    #            self.is_falling = True;
    #        else:
    #            self.velocity_y = 0;
    #            self.set_velocity(self.friction_x * Time,0);
    #    return;  


if "__main__" == __name__ :
    p:Physx = Physx();
    print(p.get_can_jump());
    print(p.set_velocity(1, 2));
    print(p.get_velocities());
    #print(type(Physx.calc_length_from_origin(2.3, 3.1)));
    print(Physx.calc_length_from_origin(2.3, 3.1));

