pub struct Piece {
    name: String,
    color: String,
    x: i32,
    y: i32,
    symbol: char,
    moves: Vec<(i32, i32)>,
    path_check: bool,
}

pub struct Board {
    pieces: Vec<Piece>,
    size: (i32, i32),
}

impl Piece {
    pub fn new(n: String, c: String, x_pos: i32, y_pos: i32) -> Self {
        Self {
            moves: match n.as_str() {
                "Pawn" => vec![(0, 1)], // Pawns move forward one step
                "Rook" => {
                    let mut rook_moves = Vec::new();
                    for i in 1..8 {
                        rook_moves.push((i, 0)); // Right
                        rook_moves.push((-i, 0)); // Left
                        rook_moves.push((0, i)); // Up
                        rook_moves.push((0, -i)); // Down
                    }
                    rook_moves
                }
                "Knight" => vec![
                    (2, 1),
                    (1, 2),
                    (-1, 2),
                    (-2, 1),
                    (-2, -1),
                    (-1, -2),
                    (1, -2),
                    (2, -1),
                ], // Knights move in an L-shape
                "Bishop" => {
                    let mut bishop_moves = Vec::new();
                    for i in 1..8 {
                        bishop_moves.push((i, i)); // Diagonal up-right
                        bishop_moves.push((-i, i)); // Diagonal up-left
                        bishop_moves.push((i, -i)); // Diagonal down-right
                        bishop_moves.push((-i, -i)); // Diagonal down-left
                    }
                    bishop_moves
                }
                "Queen" => {
                    let mut queen_moves = Vec::new();
                    for i in 1..8 {
                        queen_moves.push((i, 0)); // Right
                        queen_moves.push((-i, 0)); // Left
                        queen_moves.push((0, i)); // Up
                        queen_moves.push((0, -i)); // Down
                        queen_moves.push((i, i)); // Diagonal up-right
                        queen_moves.push((-i, i)); // Diagonal up-left
                        queen_moves.push((i, -i)); // Diagonal down-right
                        queen_moves.push((-i, -i)); // Diagonal down-left
                    }
                    queen_moves
                }
                "King" => vec![
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                    (1, 1),
                    (-1, 1),
                    (1, -1),
                    (-1, -1),
                ], // Kings move one step in any direction
                _ => Vec::new(), // Default to no moves for unknown pieces
            },
            path_check: match n.as_str() {
                "Pawn" | "Knight" | "King" => false, // These pieces do not check paths
                _ => true,                           // Rook, Bishop, Queen check paths
            },
            symbol: match (n.as_str(), c.as_str()) {
                ("Pawn", "White") => '♙',
                ("Rook", "White") => '♖',
                ("Knight", "White") => '♘',
                ("Bishop", "White") => '♗',
                ("Queen", "White") => '♕',
                ("King", "White") => '♔',
                ("Pawn", "Black") => '♟',
                ("Rook", "Black") => '♜',
                ("Knight", "Black") => '♞',
                ("Bishop", "Black") => '♝',
                ("Queen", "Black") => '♛',
                ("King", "Black") => '♚',
                _ => '?',
            },
            name: n,
            color: c,
            x: x_pos,
            y: y_pos,
        }
    }

    fn move_select(&mut self, move_index: i32) {
        if move_index < 0 || move_index as usize >= self.moves.len() {
            println!("Invalid move index for piece {}.", self.name);
            return;
        }
        let (dx, dy) = self.moves[move_index as usize];
        self.x += dx;
        self.y += dy;
    }
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
        }
    }

    pub fn display(&self) {
        println!("{}", "-".repeat(((self.size.0 * 2) as usize) - 1));
        for y in (0..self.size.1).rev() {
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
        println!("{}", "-".repeat(((self.size.0 * 2) as usize) - 1));
    }

    pub fn move_piece(&mut self, piece_x: i32, piece_y: i32, move_index: i32) {
        for piece in &mut self.pieces {
            if piece.x == piece_x && piece.y == piece_y {
                piece.move_select(move_index);
                return;
            }
        }
        println!("No piece found at position ({}, {}).", piece_x, piece_y);
    }
}
