use std::fmt;

#[derive(Clone, PartialEq, Debug, Copy)]
pub enum Side {
    BLACK,
    WHITE,
}

#[derive(Clone, PartialEq, Debug, Copy)]
pub enum PieceType {
    PAWN,
    ROOK,
    KNIGHT,
    BISHOP,
    QUEEN,
    KING,
}

#[derive(Clone, PartialEq, Debug, Copy)]
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

    pub fn get_type(&self) -> PieceType {
        self.t
    }

    pub fn get_color(&self) -> Side {
        self.color
    }

    pub fn get_position(&self) -> Position {
        self.position
    }

    pub fn get_symbol(&self) -> char {
        self.symbol
    }

    pub fn is_valid_move(&self, new_position: Position, board: &Board) -> bool {
        if self.valid_moves(&board).contains(&(self.position, new_position)) {
            true
        } else {
            false
        }
    }

    pub fn valid_moves(&self, board: &Board) -> Vec<(Position, Position)> {
        let mut output = Vec::new();
        match self.t {
            PieceType::PAWN => {
                let (start_row, direction) = if self.color == Side::WHITE {
                    (1, 1)
                } else {
                    (6, -1)
                };
                
                let forward_one = self.position.add(Position {
                    x: 0,
                    y: 1 * direction,
                });

                let forward_two = self.position.add(Position {
                    x: 0,
                    y: 2 * direction,
                });

                let diagonal_1 = self.position.add(Position {
                    x: 1,
                    y: 1 * direction,
                });

                let diagonal_2 = self.position.add(Position {
                    x: -1,
                    y: 1 * direction,
                });

                let diagonal_one_available = {
                    match board.at_location(&diagonal_1) {
                        Some(obj) => {
                            if obj.color != self.color {
                                true
                            } else {
                                false
                            }
                        }
                        None => false,
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
                        None => false,
                    }
                };

                if board.is_location_empty(&forward_one) {
                    output.push((self.position, forward_one));
                }
                if self.position.y == start_row && board.is_location_empty(&forward_one) && board.is_location_empty(&forward_two) {
                    output.push((self.position, forward_two));
                }
                if diagonal_one_available {
                    output.push((self.position, diagonal_1));
                }
                if diagonal_two_available {
                    output.push((self.position, diagonal_2));
                }
            }
            PieceType::ROOK => {
                let directions = vec![(0, 1), (0, -1), (1, 0), (-1, 0)];

                self.in_direction_check(board, directions, &mut output);
            }
            PieceType::KNIGHT => {
                let locations = [
                    Position { x: 2, y: 1 },
                    Position { x: 2, y: -1 },
                    Position { x: -2, y: 1 },
                    Position { x: -2, y: -1 },
                    Position { x: 1, y: 2 },
                    Position { x: 1, y: -2 },
                    Position { x: -1, y: 2 },
                    Position { x: -1, y: -2 },
                ];

                self.check_locations(board, &mut output, locations);
            }
            PieceType::BISHOP => {
                let directions = vec![(1, 1), (-1, 1), (-1, -1), (1, -1)];

                self.in_direction_check(board, directions, &mut output);
            }
            PieceType::QUEEN => {
                let directions = vec![
                    (1, 1),
                    (-1, 1),
                    (-1, -1),
                    (1, -1),
                    (0, 1),
                    (0, -1),
                    (1, 0),
                    (-1, 0),
                ];

                self.in_direction_check(board, directions, &mut output);
            }
            PieceType::KING => {
                let locations = [
                    Position { x: 1, y: 1 },
                    Position { x: 1, y: -1 },
                    Position { x: 1, y: 0 },
                    Position { x: 0, y: 1 },
                    Position { x: 0, y: -1 },
                    Position { x: -1, y: 1 },
                    Position { x: -1, y: -1 },
                    Position { x: -1, y: 0 },
                ];

                // Only allow king moves that do not result in being under attack
                let mut safe_moves = Vec::new();
                self.check_locations(board, &mut safe_moves, locations);

                for (from, to) in safe_moves {
                    let mut hypothetical_board = board.clone();
                    // Try to move the king to the new position
                    if hypothetical_board.move_piece(from, to).is_ok() {
                        // If king is not under attack after the move, it's a valid move
                        if !hypothetical_board.is_king_under_attack(self.color) {
                            output.push((from, to));
                        }
                    }
                }
            }
        }
        output
    }

    fn check_locations(
        &self,
        board: &Board,
        output: &mut Vec<(Position, Position)>,
        relative_locations: [Position; 8],
    ) -> bool {
        for location in relative_locations {
            let position = self.position.add(location);

            if position.x < 0 || position.x > 7 || position.y < 0 || position.y > 7 {
                continue;
            }

            match board.does_location_match_color(&position, &self.color) {
                Some(is_color) => {
                    if !is_color {
                        output.push((self.position, position));
                    }
                }
                None => {
                    output.push((self.position, position));
                }
            }
        }
        return true;
    }

    fn in_direction_check(
        &self,
        board: &Board,
        directions: Vec<(i8, i8)>,
        output: &mut Vec<(Position, Position)>
    ) {
        if self.t != PieceType::QUEEN && self.t != PieceType::BISHOP && self.t != PieceType::ROOK {
            panic!(
                "Function should not be called with {:?} only Queen Bishop and Rook",
                self.t
            )
        }

        for direction in directions.iter() {
            for i in 1..8 {
                let position = self.position.add(Position {
                    x: i * direction.0,
                    y: i * direction.1,
                });

                if position.x < 0 || position.x > 7 || position.y < 0 || position.y > 7 {
                    break;
                }

                match board.does_location_match_color(&position, &self.color) {
                    Some(is_color) => {
                        if is_color {
                            break;
                        } else {
                            output.push((self.position, position));
                            break;
                        }
                    }
                    None => {
                        output.push((self.position, position));
                    }
                }
            }
        }
    }
}

impl fmt::Display for ChessPiece {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.symbol)
    }
}

#[derive(Clone, PartialEq, Debug, Copy)]
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

#[derive(Clone)]
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
        pieces.push(ChessPiece::new(
            PieceType::ROOK,
            Side::WHITE,
            Position { x: 0, y: 0 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::KNIGHT,
            Side::WHITE,
            Position { x: 1, y: 0 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::BISHOP,
            Side::WHITE,
            Position { x: 2, y: 0 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::QUEEN,
            Side::WHITE,
            Position { x: 3, y: 0 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::KING,
            Side::WHITE,
            Position { x: 4, y: 0 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::BISHOP,
            Side::WHITE,
            Position { x: 5, y: 0 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::KNIGHT,
            Side::WHITE,
            Position { x: 6, y: 0 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::ROOK,
            Side::WHITE,
            Position { x: 7, y: 0 },
        ));

        // Black Main Row
        pieces.push(ChessPiece::new(
            PieceType::ROOK,
            Side::BLACK,
            Position { x: 0, y: 7 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::KNIGHT,
            Side::BLACK,
            Position { x: 1, y: 7 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::BISHOP,
            Side::BLACK,
            Position { x: 2, y: 7 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::QUEEN,
            Side::BLACK,
            Position { x: 3, y: 7 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::KING,
            Side::BLACK,
            Position { x: 4, y: 7 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::BISHOP,
            Side::BLACK,
            Position { x: 5, y: 7 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::KNIGHT,
            Side::BLACK,
            Position { x: 6, y: 7 },
        ));
        pieces.push(ChessPiece::new(
            PieceType::ROOK,
            Side::BLACK,
            Position { x: 7, y: 7 },
        ));

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

    fn move_piece(&mut self, pos_from: Position, pos_to: Position) -> Result<(), &str> {
        if (pos_from.x > 7 || pos_from.y > 7) || (pos_to.x > 7 || pos_to.y > 7) {
            return Err("Positions are outside of bounds");
        }

        self.pieces.retain(|piece| piece.position != pos_to);

        for piece in self.pieces.iter_mut() {
            if piece.position == pos_from {
                piece.position = pos_to.clone();
                self.turn = if self.turn == Side::WHITE {
                    Side::BLACK
                } else {
                    Side::WHITE
                };
                return Ok(());
            }
        }

        Err("Can't find piece at that position")
    }

    pub fn index_at_location(&self, pos: &Position) -> Option<usize> {
        for (index, &piece) in self.pieces.iter().enumerate() {
            if piece.position == *pos {
                return Some(index);
            }
        }
        return None;
    }

    pub fn at_location(&self, pos: &Position) -> Option<ChessPiece> {
        match self.index_at_location(pos) {
            Some(index) => Some(self.pieces[index]),
            None => None,
        }
    }

    pub fn is_location_empty(&self, pos: &Position) -> bool {
        match self.at_location(&pos) {
            Some(_) => return false,
            None => return true,
        }
    }

    pub fn does_location_match_color(&self, pos: &Position, color: &Side) -> Option<bool> {
        match self.index_at_location(pos) {
            Some(index) => {
                if self.pieces[index].color == *color {
                    return Some(true);
                } else {
                    return Some(false);
                }
            }
            None => return None,
        }
    }

    pub fn move_piece_with_error_checking(
        &mut self,
        from: &Position,
        to: &Position,
    ) -> Result<(), &str> {
        let piece = self.pieces[match self.index_at_location(from) {
            Some(index) => index,
            None => return Err("No Piece at that position"),
        }];

        if !piece.is_valid_move(*to, self) {
            return Err("Invalid Move");
        }

        if piece.color != self.turn {
            return Err("That's the other side's piece!");
        }
        
        self.move_piece(*from, *to)
    }

    fn find_pieces(&self, piece_type: PieceType, side: Side) -> Option<usize> {
        for (index, piece) in self.pieces.iter().enumerate() {
            if piece.t == piece_type && piece.color == side {
                return Some(index);
            }
        }

        return None;
    }

    pub fn is_king_under_attack(&self, side: Side) -> bool {
        let king = self.pieces[match self.find_pieces(PieceType::KING, side) {
            Some(index) => index,
            None => panic!("There's no king!"),
        }];

        for piece in self.pieces.iter() {
            if piece.color != king.color {
                // Skip king pieces to avoid infinite recursion
                if piece.t == PieceType::KING {
                    // Check if king is adjacent
                    if (piece.position.x - king.position.x).abs() <= 1
                        && (piece.position.y - king.position.y).abs() <= 1
                    {
                        return true;
                    }
                } else if piece.is_valid_move(king.position, self) {
                    return true;
                }
            }
        }

        false
    }

    pub fn is_checkmate(&self, side: Side) -> bool {
        let king = self.pieces[match self.find_pieces(PieceType::KING, side) {
            Some(index) => index,
            None => panic!("There's no king!"),
        }];

        let locations = [
            Position { x: 1, y: 1 },
            Position { x: 1, y: -1 },
            Position { x: 1, y: 0 },
            Position { x: 0, y: 1 },
            Position { x: 0, y: -1 },
            Position { x: -1, y: 1 },
            Position { x: -1, y: -1 },
            Position { x: -1, y: 0 },
        ];

        for location in locations {
            if king.is_valid_move(king.position.add(location), self) {
                return false;
            }
        }

        if !self.is_king_under_attack(side) {
            return false;
        }

        true
    }

    pub fn is_stalemate(&self) {

    }
}

impl fmt::Display for Board {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let mut output = String::new();

        let grid_format = self.into_grid();

        let iterator: Box<dyn Iterator<Item = &Vec<Option<ChessPiece>>> + '_> =
            if self.turn == Side::WHITE {
                Box::new(grid_format.iter().rev())
            } else {
                Box::new(grid_format.iter())
            };

        for (index, col) in iterator.enumerate() {
            output.push_str(&format!(
                "{} ",
                if self.turn == Side::WHITE {
                    7 - index
                } else {
                    index
                }
            ));
            for piece in col.iter() {
                match piece {
                    Some(p) => output.push(p.symbol),
                    None => output.push('□'),
                }
                output.push(' ');
            }
            output.push('\n');
        }

        output.push_str("  0 1 2 3 4 5 6 7");

        write!(f, "{output}")
    }
}
