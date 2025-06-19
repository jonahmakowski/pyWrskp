use crate::pieces::*;
use std::io;

pub struct Board {
    pub pieces: Vec<Piece>,
    pub size: (i32, i32),
    pub turn: String,
}

impl Board {
    pub fn new() -> Self {
        Self {
            pieces: vec![
                Piece::new("Rook".to_string(), "White".to_string(), 0, 0),
                Piece::new("Knight".to_string(), "White".to_string(), 1, 0),
                Piece::new("Bishop".to_string(), "White".to_string(), 2, 0),
                Piece::new("Queen".to_string(), "White".to_string(), 3, 0),
                Piece::new("King".to_string(), "White".to_string(), 4, 0),
                Piece::new("Bishop".to_string(), "White".to_string(), 5, 0),
                Piece::new("Knight".to_string(), "White".to_string(), 6, 0),
                Piece::new("Rook".to_string(), "White".to_string(), 7, 0),
                
                Piece::new("Pawn".to_string(), "White".to_string(), 0, 1),
                Piece::new("Pawn".to_string(), "White".to_string(), 1, 1),
                Piece::new("Pawn".to_string(), "White".to_string(), 2, 1),
                Piece::new("Pawn".to_string(), "White".to_string(), 3, 1),
                Piece::new("Pawn".to_string(), "White".to_string(), 4, 1),
                Piece::new("Pawn".to_string(), "White".to_string(), 5, 1),
                Piece::new("Pawn".to_string(), "White".to_string(), 6, 1),
                Piece::new("Pawn".to_string(), "White".to_string(), 7, 1),
                
                Piece::new("Rook".to_string(), "Black".to_string(), 0, 7),
                Piece::new("Knight".to_string(), "Black".to_string(), 1, 7),
                Piece::new("Bishop".to_string(), "Black".to_string(), 2, 7),
                Piece::new("Queen".to_string(), "Black".to_string(), 3, 7),
                Piece::new("King".to_string(), "Black".to_string(), 4, 7),
                Piece::new("Bishop".to_string(), "Black".to_string(), 5, 7),
                Piece::new("Knight".to_string(), "Black".to_string(), 6, 7),
                Piece::new("Rook".to_string(), "Black".to_string(), 7, 7),
                
                Piece::new("Pawn".to_string(), "Black".to_string(), 0, 6),
                Piece::new("Pawn".to_string(), "Black".to_string(), 1, 6),
                Piece::new("Pawn".to_string(), "Black".to_string(), 2, 6),
                Piece::new("Pawn".to_string(), "Black".to_string(), 3, 6),
                Piece::new("Pawn".to_string(), "Black".to_string(), 4, 6),
                Piece::new("Pawn".to_string(), "Black".to_string(), 5, 6),
                Piece::new("Pawn".to_string(), "Black".to_string(), 6, 6),
                Piece::new("Pawn".to_string(), "Black".to_string(), 7, 6),
            ],
            size: (8, 8),
            turn: "White".to_string(),
        }
    }

    pub fn display(&self) {
        println!("{}", "-".repeat(((self.size.0 * 2) as usize) + 1));
        for y in (0..self.size.1).rev() {
            print!("{} ", y);
            for x in 0..self.size.0 {
                let mut found = false;
                for piece in &self.pieces {
                    if piece.x == x && piece.y == y {
                        print!("{} ", piece.symbol);
                        found = true;
                        break;
                    }
                }
                if !found {
                    print!(". ");
                }
            }
            println!();
        }
        print!("  ");
        for x in 0..self.size.0 {
            print!("{} ", x);
        }
        println!("\n{}", "-".repeat(((self.size.0 * 2) as usize) + 1));
    }

    pub fn move_piece(&mut self, piece_x: i32, piece_y: i32, move_index: i32) {
        let mut kill = (-1, -1);
        let mut new_x = -1;
        let mut new_y = -1;
        let mut piece = Piece::new("".to_string(), "".to_string(), 0, 0);

        for p in &mut self.pieces {
            if p.x == piece_x && p.y == piece_y {
                p.move_select(move_index);
                new_x = p.x;
                new_y = p.y;
                piece = p.clone();
            }
        }

        for scan_piece in &self.pieces {
            if scan_piece.x == new_x && scan_piece.y == new_y && scan_piece.color != piece.color {
                println!("Captured {} at ({}, {}).", scan_piece.name, new_x, new_y);
                kill = (scan_piece.x, scan_piece.y);
                break;
            }
        }

        if kill != (-1, -1) {
            self.kill_piece(kill.0, kill.1);
        }

        self.pieces.push(piece.clone());

        self.turn = self.get_opponent_color(&self.turn);

        self.delete_duplicate_pieces();
    }

    pub fn valid_move(&self, piece_x: i32, piece_y: i32, move_index: i32) -> bool {
        let piece: &Piece;

        if let Some(piece_iter) = self.pieces.iter().find(|p| p.x == piece_x && p.y == piece_y) {
            piece = piece_iter;
        } else {
            println!("VALID_MOVE: No piece found at position ({}, {}).", piece_x, piece_y);
            return false;
        }

        if move_index < 0 || move_index as usize >= piece.moves.len() {
            println!("Invalid move index for piece {}.", piece.name);
            return false;
        }

        let (dx, dy) = piece.moves[move_index as usize];
        let (new_x, new_y) = (piece.x + dx, piece.y + dy);

        for scan_piece in &self.pieces {
            if scan_piece.x == new_x && scan_piece.y == new_y {
                if scan_piece.color == piece.color {
                    return false;
                }
            }
        }
        if new_x > self.size.0 - 1 || new_x < 0 || new_y > self.size.1 - 1 || new_y < 0 {
            return false;
        }
        if !piece.path_check || (dx.abs() == 1 && dy.abs() == 1) {
            return true;
        }

        // For pieces that check paths (Rook, Bishop, Queen), we need to ensure the path is clear
        let mut step_x = 0;
        let mut step_y = 0;
        
        if dx != 0 {
            step_x = dx / dx.abs();
        }
        
        if dy != 0 {
            step_y = dy / dy.abs();
        }

        let mut scanning_x = piece.x + step_x;
        let mut scanning_y = piece.y + step_y;
    
        while scanning_x != new_x || scanning_y != new_y {
            for scan_piece in &self.pieces {
                if scan_piece.x == scanning_x && scan_piece.y == scanning_y {
                    return false;
                }
            }
            scanning_x += step_x;
            scanning_y += step_y;
        }
        true
    }
    
    pub fn count_score(&self, color: &String) -> (i32, bool) {
        let mut score = 0;
        let mut has_king = false;
        for piece in &self.pieces {
            if piece.color == *color {
                score += piece.value;
                if piece.invaluable {
                    has_king = true;
                }
            }
        }
        return (score, has_king);
    }

    fn kill_piece(&mut self, piece_x: i32, piece_y: i32) {
        self.pieces.retain(|piece| !(piece.x == piece_x && piece.y == piece_y));
    }

    pub fn deep_clone(&self) -> Self {
        Self {
            pieces: self.pieces.iter().map(|p| p.clone()).collect(),
            size: self.size,
            turn: self.turn.clone(),
        }
    }

    pub fn get_opponent_color(&self, color: &String) -> String {
        if color == "White" {
            "Black".to_string()
        } else {
            "White".to_string()
        }
    }

    fn get_piece_at(&self, x: i32, y: i32) -> Option<&Piece> {
        self.pieces.iter().find(|p| p.x == x && p.y == y)
    }

    fn delete_duplicate_pieces(&mut self) {
        let mut unique_pieces: Vec<&Piece> = Vec::new();
        for piece in &self.pieces {
            if !unique_pieces.iter().any(|p: &&Piece| p.x == piece.x && p.y == piece.y && p.color == piece.color) {
                unique_pieces.push(piece);
            }
        }
        self.pieces = unique_pieces.iter().map(|p| (*p).clone()).collect();
    }

    pub fn user_turn(&mut self) {
        let mut piece_x = String::new();
        let mut piece_y = String::new();
        let mut move_index = String::new();

        io::stdin().read_line(&mut piece_x).expect("Failed to read line");
        io::stdin().read_line(&mut piece_y).expect("Failed to read line");

        let piece_x: i32 = piece_x.trim().parse().expect("Please enter a valid number for piece X position");
        let piece_y: i32 = piece_y.trim().parse().expect("Please enter a valid number for piece Y position");

        if let Some(piece) = self.get_piece_at(piece_x, piece_y) {
            println!("Selected piece: {} ({}) at ({}, {})", piece.symbol, piece.name, piece.x, piece.y);
            println!("Available moves: {:?}", piece.moves);
            io::stdin().read_line(&mut move_index).expect("Failed to read line");
            let move_index: i32 = move_index.trim().parse().expect("Please enter a valid number for move index");

            if piece.color.to_string() == self.turn.to_string() {
                self.move_piece(piece_x, piece_y, move_index);
                self.display();
            } else {
                println!("Invalid move. Try again.");
            }
        } else {
            println!("No piece found at ({}, {}).", piece_x, piece_y);
        }
    }
}
