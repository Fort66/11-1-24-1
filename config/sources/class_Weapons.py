from pygame.math import Vector2
from math import pi


class Weapons:
    def load_weapons(self, obj, source, angle):
        obj.pos_weapons = []
        for value in source:
            obj.pos_weapons.append(value)

    def pos_rotation(self, obj, angle):
        self.angle = angle
        result = []
        for value in obj.pos_weapons:
            newX, newY = self.vector_rotation(value, -angle / 180 * pi)
            result.append([obj.rect.centerx + newX, obj.rect.centery + newY])
        return result

    def vector_rotation(self, vector, angle):
        vector = Vector2(vector)
        return vector.rotate_rad(angle)

    # def update_pos(self):
    #     value = self.pos_rotation(self.angle)
    #     for pos in value:
    #         pos[0] += self.direction.x
    #         pos[1] += self.direction.y

    #         return weapons.pos_rotation(self, self.angle)
