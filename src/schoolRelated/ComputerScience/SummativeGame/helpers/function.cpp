#ifndef FUNCTION_CPP
#define FUNCTION_CPP

#include <math.h>
#include "structs.cpp"
#include "globals.cpp"

bool can_collide(Hitbox a, Hitbox b) {
    for (int i = 0; i < 3; i++) {
        if (a.collision.collisionmask[i] == b.collision.collisionlayer) {
            return true;
        }
    }
    return false;
}

// Returns 0 for no collision, 1 for left, 2 for right, 3 for top, 4 for bottom, relative to 'a'
int collision_type(Object a, Object b) {
    if (!can_collide(a.hitbox, b.hitbox)) {
        return 0;
    }

    if (a.position.x - a.hitbox.size.x / 2 < b.position.x + b.hitbox.size.x / 2) return 1;
    if (a.position.x + a.hitbox.size.x / 2 > b.position.x - b.hitbox.size.x / 2) return 2;
    if (a.position.y - a.hitbox.size.y / 2 < b.position.y + b.hitbox.size.y / 2) return 3;
    if (a.position.y + a.hitbox.size.y / 2 > b.position.y - b.hitbox.size.y / 2) return 4;
    return 0;
}

bool is_colliding(Object a, Object b) {
    if (collision_type(a, b) != 0) {
        return true;
    }
    return false;
}

Object check_collisions(Object obj, Object objects[], int amount) {
    for (int i = 0; i < amount; i++) {
        int ct = collision_type(obj, objects[i]);
        if (ct == 0) {
            continue;
        }
        
        // If it's colliding on the left or right, stop horizontal movement
        if (ct == 1 && obj.velocity.x < 0) {
            obj.velocity.x = 0;
        }
        if (ct == 2 && obj.velocity.x > 0) {
            obj.velocity.x = 0;
        }

        // Stop vertical movement if colliding on top or bottom
        if (ct == 3 && obj.velocity.y > 0) {
            obj.velocity.y = 0;
        }
        if (ct == 4 && obj.velocity.y < 0) {
            obj.velocity.y = 0;
        }
    }

    return obj;
}

#endif