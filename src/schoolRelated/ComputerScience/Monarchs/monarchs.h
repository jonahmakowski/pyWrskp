const int SCREEN_W = 1280;       // screen width
const int SCREEN_H = 480;       // screen height

const int COL_1 = 5;    //tabs for chart layout
const int COL_2 = 180;
const int COL_3 = 400;
const int COL_4 = 700;

//#define BACKGROUND al_map_rgb(0x09, 0x31, 0x45)
#define BACKGROUND al_map_rgb(0xff, 0xff, 0xff)
#define FOREGROUND al_map_rgb(0x3C, 0x64, 0x78)

//define structs here
struct Date {
    int year;
    char month[14];
    int day;
};

struct Person {
    char name[14];
    char regnal[6];
    Date birth, death;
};

void initializeAllegro();
int checkSetup(ALLEGRO_DISPLAY *display, ALLEGRO_FONT *font);
void printTitle(ALLEGRO_FONT *font);
int readFile(Person p[], int &counter);
void printDatabase(ALLEGRO_FONT *font, Person p[], int counter);
void show_instructions();
void sort_by_age_at_death(Person p[], int counter);
void sort_by_death_year(Person p[], int counter);
void write_data_to_file(Person p[], int counter);
void draw_stuff(ALLEGRO_FONT *font, Person monarchs[], int number);
void add_monarch(Person p[], int &counter);
void remove_monarch(Person p[], int &counter);
