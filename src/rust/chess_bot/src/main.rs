mod board;
mod bot;
mod pieces;
use board::*;
use bot::*;

fn main() {
    let mut b = Board::new();
    b.display();
    while true {
        play_best_move(&mut b, &"White".to_string(), 1);
        b.display();
        b.user_turn();
        b.display();
    }
}
