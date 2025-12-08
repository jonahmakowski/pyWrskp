use std::fmt;

#[derive(Clone, PartialEq, Debug)]
pub enum Side {
    BLACK,
    WHITE,
}

#[derive(Clone, PartialEq, Debug)]
pub enum PieceType {
    PAWN,
    ROOK,
    KNIGHT,
    BISHOP,
    QUEEN,
    KING,
}

#[derive(Clone, PartialEq, Debug)]
pub struct ChessPiece {
    t: PieceType,
    color: Side,
    position: Position,
    symbol: char,
}

impl ChessPiece {
    pub fn new(t: PieceType, color: Side, position: Position) -> Self {
        let symbol = match (&t, &color) {
            (PieceType::PAWN, Side::WHITE) => '♙',
            (PieceType::PAWN, Side::BLACK) => '♟',
            (PieceType::ROOK, Side::WHITE) => '♖',
            (PieceType::ROOK, Side::BLACK) => '♜',
            (PieceType::KNIGHT, Side::WHITE) => '♘',
            (PieceType::KNIGHT, Side::BLACK) => '♞',
            (PieceType::BISHOP, Side::WHITE) => '♗',
            (PieceType::BISHOP, Side::BLACK) => '♝',
            (PieceType::QUEEN, Side::WHITE) => '♕',
            (PieceType::QUEEN, Side::BLACK) => '♛',
            (PieceType::KING, Side::WHITE) => '♔',
            (PieceType::KING, Side::BLACK) => '♚',
        };

        Self {
            t,
            color,
            position,
            symbol,
        }
    }

    pub fn is_valid_move(&self, new_position: Position, board: Board) -> bool {
        match self.t {
            PieceType::PAWN => {
                if new_position.x < 0 || new_position.y < 0 || new_position.x > 7 || new_position.y > 7 {
                    return false;
                }

                let (start_row, direction) = if self.color == Side::WHITE {(1, 1)} else {(6, -1)};
                let forward_one = self.position.add(Position {x: 0, y: 1*direction});
                let forward_two = self.position.add(Position {x: 0, y: 2*direction});
                let diagonal_1 = self.position.add(Position {x: 1, y: 1*direction});
                let diagonal_2 = self.position.add(Position {x: -1, y: 1*direction});

                let diagonal_one_available = {
                    match board.at_location(&diagonal_1) {
                        Some(obj) => {
                            if obj.color != self.color {
                                true
                            } else {
                                false
                            }
                        }
                        None => false
                    }
                };

                let diagonal_two_available = {
                    match board.at_location(&diagonal_2) {
                        Some(obj) => {
                            if obj.color != self.color {
                                true
                            } else {
                                false
                            }
                        }
                        None => false
                    }
                };

                if new_position == forward_one && board.is_location_empty(&forward_one) {
                    return true;
                } else if self.position.y == start_row && new_position == forward_two && board.is_location_empty(&forward_one) && board.is_location_empty(&forward_two) {
                    return true;
                } else if new_position == diagonal_1 && diagonal_one_available {
                    return true;
                } else if new_position == diagonal_2 && diagonal_two_available {
                    return true;
                } else {
                    return false;
                }
            },
            PieceType::ROOK => panic!(),
            PieceType::KNIGHT => panic!(),
            PieceType::BISHOP => panic!(),
            PieceType::QUEEN => panic!(),
            PieceType::KING => panic!(),
        }
    }
}

impl fmt::Display for ChessPiece {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.symbol)
    }
}

#[derive(Clone, PartialEq, Debug)]
pub struct Position {
    pub x: i8,
    pub y: i8,
}

impl Position {
    pub fn add(&self, other: Self) -> Self {
        Self {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

pub struct Board {
    pub pieces: Vec<ChessPiece>,
    pub turn: Side,
}

impl Board {
    pub fn new() -> Self {
        let mut pieces = Vec::new();

        // White Pawns
        for x in 0..8 {
            pieces.push(ChessPiece::new(
                PieceType::PAWN,
                Side::WHITE,
                Position { x, y: 1 },
            ));
        }

        // Black Pawns
        for x in 0..8 {
            pieces.push(ChessPiece::new(
                PieceType::PAWN,
                Side::BLACK,
                Position { x, y: 6 },
            ));
        }

        // White Main Row
        pieces.push(ChessPiece::new(PieceType::ROOK, Side::WHITE, Position { x: 0, y: 0 }));
        pieces.push(ChessPiece::new(PieceType::KNIGHT, Side::WHITE, Position { x: 1, y: 0 }));
        pieces.push(ChessPiece::new(PieceType::BISHOP, Side::WHITE, Position { x: 2, y: 0 }));
        pieces.push(ChessPiece::new(PieceType::QUEEN, Side::WHITE, Position { x: 3, y: 0 }));
        pieces.push(ChessPiece::new(PieceType::KING, Side::WHITE, Position { x: 4, y: 0 }));
        pieces.push(ChessPiece::new(PieceType::BISHOP, Side::WHITE, Position { x: 5, y: 0 }));
        pieces.push(ChessPiece::new(PieceType::KNIGHT, Side::WHITE, Position { x: 6, y: 0 }));
        pieces.push(ChessPiece::new(PieceType::ROOK, Side::WHITE, Position { x: 7, y: 0 }));

        // Black Main Row
        pieces.push(ChessPiece::new(PieceType::ROOK, Side::BLACK, Position { x: 0, y: 7 }));
        pieces.push(ChessPiece::new(PieceType::KNIGHT, Side::BLACK, Position { x: 1, y: 7 }));
        pieces.push(ChessPiece::new(PieceType::BISHOP, Side::BLACK, Position { x: 2, y: 7 }));
        pieces.push(ChessPiece::new(PieceType::QUEEN, Side::BLACK, Position { x: 3, y: 7 }));
        pieces.push(ChessPiece::new(PieceType::KING, Side::BLACK, Position { x: 4, y: 7 }));
        pieces.push(ChessPiece::new(PieceType::BISHOP, Side::BLACK, Position { x: 5, y: 7 }));
        pieces.push(ChessPiece::new(PieceType::KNIGHT, Side::BLACK, Position { x: 6, y: 7 }));
        pieces.push(ChessPiece::new(PieceType::ROOK, Side::BLACK, Position { x: 7, y: 7 }));

        Self {
            pieces,
            turn: Side::WHITE,
        }
    }

    pub fn into_grid(&self) -> Vec<Vec<Option<ChessPiece>>> {
        let mut result: Vec<Vec<Option<ChessPiece>>> = vec![];

        for x in 0..8 {
            result.push(Vec::new());
            for _ in 0..8 {
                result[x].push(None);
            }
        }

        for piece in self.pieces.iter() {
            result[piece.position.y as usize][piece.position.x as usize] = Some(piece.clone());
        }

        result
    }

    pub fn move_piece(&mut self, pos_from: Position, pos_to: Position) -> Result<(), &str> {
        if (pos_from.x > 7 || pos_from.y > 7) || (pos_to.x > 7 || pos_to.y > 7) {
            return Err("Positions are outside of bounds");
        }

        self.pieces.retain(|piece| piece.position != pos_to);

        for piece in self.pieces.iter_mut() {
            if piece.position == pos_from {
                piece.position = pos_to.clone();
                return Ok(());
            }
        }

        Err("Can't find piece at that position")
    }

    pub fn at_location(&self, pos: &Position) -> Option<ChessPiece> {
        let grid_version = self.into_grid();

        match &grid_version[pos.y as usize][pos.x as usize] {
            Some(obj) => Some(obj.clone()),
            None => None,
        }
    }

    pub fn is_location_empty(&self, pos: &Position) -> bool {
        match self.at_location(&pos) {
            Some(_) => return false,
            None => return true,
        }
    }
}

impl fmt::Display for Board {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let mut output = String::new();

        let grid_format = self.into_grid();

        for col in grid_format.iter() {
            for piece in col.iter() {
                match piece {
                    Some(p) => output.push(p.symbol),
                    None => output.push('*'),
                }
                output.push(' ');
            }
            output.push('\n');
        }

        write!(f, "{output}")
    }
}
