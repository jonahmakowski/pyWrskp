pub struct Piece {
    pub name: String,
    pub color: String,
    pub x: i32,
    pub y: i32,
    pub symbol: char,
    pub moves: Vec<(i32, i32)>,
    pub path_check: bool,
    pub exists: bool,
    pub invaluable: bool,
    pub value: i32,
}

impl Piece {
    pub fn new(n: String, c: String, x_pos: i32, y_pos: i32) -> Self {
        Self {
            moves: match n.as_str() {
                "Pawn" => {
                    match c.as_str() {
                        "White" => vec![(0, 1)],  // Pawns move forward one step
                        "Black" => vec![(0, -1)], // Pawns move forward one step
                        _ => vec![],              // Default to no moves for unknown colors
                    }
                }
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
            color: c,
            x: x_pos,
            y: y_pos,
            exists: true,
            value: match n.as_str() {
                "Pawn" => 1,
                "Knight" => 3,
                "Bishop" => 3,
                "Rook" => 5,
                "Queen" => 9,
                "King" => 0,
                _ => 0,
            },
            invaluable: match n.as_str() {
                "King" => true, // King is invaluable
                _ => false,     // Other pieces can be captured
            },
            name: n,
        }
    }

    pub fn move_select(&mut self, move_index: i32) {
        if move_index < 0 || move_index as usize >= self.moves.len() {
            println!("Invalid move index for piece {}.", self.name);
            return;
        }
        let (dx, dy) = self.moves[move_index as usize];
        self.x += dx;
        self.y += dy;
    }

    pub fn clone(&self) -> Self {
        Self {
            name: self.name.clone(),
            color: self.color.clone(),
            x: self.x,
            y: self.y,
            symbol: self.symbol,
            moves: self.moves.clone(),
            path_check: self.path_check,
            exists: self.exists,
            invaluable: self.invaluable,
            value: self.value,
        }
    }
}
