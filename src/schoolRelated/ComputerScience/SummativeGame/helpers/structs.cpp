#ifndef STRUCTS_CPP
#define STRUCTS_CPP

struct Vector2 {
    float x;
    float y;
};

struct Vector2i {
    int x;
    int y;
};

struct CollisionData {
    // 0 = no collision, 1 = player, 2 = enemy, 3 = environment
    int collisionlayer; // What layer it is on
    int collisionmask[3]; // What layers it collides with
};

// Assuming that the middle point of the hitbox is its position
struct Hitbox {
    Vector2i size;
    CollisionData collision;
};

struct Object {
    Hitbox hitbox;
    Vector2i velocity;
    Vector2i position;
};

#endif
