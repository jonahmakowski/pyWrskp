use std::fmt;

#[derive(Clone)]
pub enum Side {
    BLACK,
    WHITE,
}

#[derive(Clone)]
pub enum PieceType {
    PAWN,
    ROOK,
    KNIGHT,
    BISHOP,
    QUEEN,
    KING,
}

#[derive(Clone)]
pub struct ChessPiece {
    t: PieceType,
    color: Side,
    position: Position,
    symbol: char,
}

#[derive(Clone, PartialEq)]
pub struct Position {
    pub x: u8,
    pub y: u8,
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
            pieces.push(ChessPiece {
                t: PieceType::PAWN,
                color: Side::WHITE,
                position: Position { x, y: 1 },
                symbol: '♙',
            });
        }

        // Black Pawns
        for x in 0..8 {
            pieces.push(ChessPiece {
                t: PieceType::PAWN,
                color: Side::BLACK,
                position: Position { x, y: 6 },
                symbol: '♟',
            });
        }

        // White Main Row
        pieces.push(ChessPiece {
            t: PieceType::ROOK,
            color: Side::WHITE,
            position: Position { x: 0, y: 0 },
            symbol: '♖',
        });
        pieces.push(ChessPiece {
            t: PieceType::KNIGHT,
            color: Side::WHITE,
            position: Position { x: 1, y: 0 },
            symbol: '♘',
        });
        pieces.push(ChessPiece {
            t: PieceType::BISHOP,
            color: Side::WHITE,
            position: Position { x: 2, y: 0 },
            symbol: '♗',
        });
        pieces.push(ChessPiece {
            t: PieceType::QUEEN,
            color: Side::WHITE,
            position: Position { x: 3, y: 0 },
            symbol: '♕',
        });
        pieces.push(ChessPiece {
            t: PieceType::KING,
            color: Side::WHITE,
            position: Position { x: 4, y: 0 },
            symbol: '♔',
        });
        pieces.push(ChessPiece {
            t: PieceType::BISHOP,
            color: Side::WHITE,
            position: Position { x: 5, y: 0 },
            symbol: '♗',
        });
        pieces.push(ChessPiece {
            t: PieceType::KNIGHT,
            color: Side::WHITE,
            position: Position { x: 6, y: 0 },
            symbol: '♘',
        });
        pieces.push(ChessPiece {
            t: PieceType::ROOK,
            color: Side::WHITE,
            position: Position { x: 7, y: 0 },
            symbol: '♖',
        });

        // Black Main Row
        pieces.push(ChessPiece {
            t: PieceType::ROOK,
            color: Side::BLACK,
            position: Position { x: 0, y: 7 },
            symbol: '♜',
        });
        pieces.push(ChessPiece {
            t: PieceType::KNIGHT,
            color: Side::BLACK,
            position: Position { x: 1, y: 7 },
            symbol: '♞',
        });
        pieces.push(ChessPiece {
            t: PieceType::BISHOP,
            color: Side::BLACK,
            position: Position { x: 2, y: 7 },
            symbol: '♝',
        });
        pieces.push(ChessPiece {
            t: PieceType::QUEEN,
            color: Side::BLACK,
            position: Position { x: 3, y: 7 },
            symbol: '♛',
        });
        pieces.push(ChessPiece {
            t: PieceType::KING,
            color: Side::BLACK,
            position: Position { x: 4, y: 7 },
            symbol: '♚',
        });
        pieces.push(ChessPiece {
            t: PieceType::BISHOP,
            color: Side::BLACK,
            position: Position { x: 5, y: 7 },
            symbol: '♝',
        });
        pieces.push(ChessPiece {
            t: PieceType::KNIGHT,
            color: Side::BLACK,
            position: Position { x: 6, y: 7 },
            symbol: '♞',
        });
        pieces.push(ChessPiece {
            t: PieceType::ROOK,
            color: Side::BLACK,
            position: Position { x: 7, y: 7 },
            symbol: '♜',
        });

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

        for piece in self.pieces.iter_mut() {
            if piece.position == pos_from {
                piece.position = pos_to.clone();
                return Ok(());
            }
        }

        Err("Can't find piece at that position")
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
