use super::*;

#[test]
fn board_into_grid() {
    let new_board = types::Board::new();

    let correct_output = "7 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n6 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n5 □ □ □ □ □ □ □ □ \n4 □ □ □ □ □ □ □ □ \n3 □ □ □ □ □ □ □ □ \n2 □ □ □ □ □ □ □ □ \n1 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n0 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n  0 1 2 3 4 5 6 7";

    assert_eq!(format!("{new_board}"), correct_output);
}

#[test]
fn move_piece() {
    let mut new_board = types::Board::new();

    if let Err(error) = new_board.move_piece_with_error_checking(
        &types::Position { x: 1, y: 1 },
        &types::Position { x: 1, y: 3 },
    ) {
        eprintln!("Error: {error}");
        panic!();
    }

    let correct_output = "0 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n1 ♙ □ ♙ ♙ ♙ ♙ ♙ ♙ \n2 □ □ □ □ □ □ □ □ \n3 □ ♙ □ □ □ □ □ □ \n4 □ □ □ □ □ □ □ □ \n5 □ □ □ □ □ □ □ □ \n6 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n7 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n  0 1 2 3 4 5 6 7";

    assert_eq!(format!("{new_board}"), correct_output);
}

#[test]
fn board_empty_position() {
    let new_board = types::Board::new();

    assert!(!new_board.is_location_empty(&types::Position {x: 0, y: 0}));
    assert!(new_board.is_location_empty(&types::Position {x: 3, y: 3}));
}

#[test]
fn board_location() {
    let new_board = types::Board::new();

    assert_eq!(
        new_board.at_location(&types::Position { x: 0, y: 0 }),
        Some(types::ChessPiece::new(types::PieceType::ROOK, types::Side::WHITE, types::Position {x: 0, y: 0}))
    );

    assert_eq!(
        new_board.at_location(&types::Position { x: 3, y: 3 }),
        None
    );
}

// ========== PAWN MOVEMENT TESTS ==========

#[test]
fn pawn_move_forward_one() {
    let mut board = types::Board::new();
    
    // White pawn moves forward one
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 1 },
        &types::Position { x: 0, y: 2 }
    ).is_ok());

    // Black pawn moves forward one
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 6 },
        &types::Position { x: 0, y: 5 }
    ).is_ok());
}

#[test]
fn pawn_move_forward_two_from_start() {
    let mut board = types::Board::new();
    
    // White pawn moves forward two from starting position
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 1 },
        &types::Position { x: 4, y: 3 }
    ).is_ok());

    // Black pawn moves forward two from starting position
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 6 },
        &types::Position { x: 4, y: 4 }
    ).is_ok());
}

#[test]
fn pawn_cannot_move_forward_two_after_first_move() {
    let mut board = types::Board::new();
    
    // Move white pawn forward one
    board.move_piece_with_error_checking(
        &types::Position { x: 3, y: 1 },
        &types::Position { x: 3, y: 2 }
    ).unwrap();

    // Skip black turn
    board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 6 },
        &types::Position { x: 0, y: 5 }
    ).unwrap();

    // Try to move white pawn forward two - should fail
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 3, y: 2 },
        &types::Position { x: 3, y: 4 }
    ).is_err());
}

#[test]
fn pawn_diagonal_capture() {
    let mut board = types::Board::new();
    
    // Set up a capture scenario - move white pawn forward
    board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 1 },
        &types::Position { x: 4, y: 3 }
    ).unwrap();

    // Move black pawn to capturable position
    board.move_piece_with_error_checking(
        &types::Position { x: 3, y: 6 },
        &types::Position { x: 3, y: 4 }
    ).unwrap();

    // Capture diagonally
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 3 },
        &types::Position { x: 3, y: 4 }
    ).is_ok());
}

#[test]
fn pawn_cannot_capture_forward() {
    let mut board = types::Board::new();
    
    // Move white pawn forward
    board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 1 },
        &types::Position { x: 4, y: 3 }
    ).unwrap();

    // Move black pawn to blocking position
    board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 6 },
        &types::Position { x: 4, y: 4 }
    ).unwrap();

    // Try to capture forward - should fail
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 3 },
        &types::Position { x: 4, y: 4 }
    ).is_err());
}

// ========== ROOK MOVEMENT TESTS ==========

#[test]
fn rook_move_vertical() {
    let mut board = types::Board::new();
    
    // Clear path for white rook
    board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 1 },
        &types::Position { x: 0, y: 3 }
    ).unwrap();

    board.move_piece_with_error_checking(
        &types::Position { x: 7, y: 6 },
        &types::Position { x: 7, y: 5 }
    ).unwrap();

    // Move rook vertically
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 0 },
        &types::Position { x: 0, y: 2 }
    ).is_ok());
}

#[test]
fn rook_move_horizontal() {
    let mut board = types::Board::new();
    
    // Clear bottom row except rooks
    board.pieces.retain(|p| {
        let pos = p.get_position();
        !(pos.y == 0 && pos.x > 0 && pos.x < 7)
    });

    // Move rook horizontally
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 0 },
        &types::Position { x: 5, y: 0 }
    ).is_ok());
}

#[test]
fn rook_cannot_jump_pieces() {
    let board = types::Board::new();
    
    let rook = board.at_location(&types::Position { x: 0, y: 0 }).unwrap();
    
    // Try to move rook through pawn - should be invalid
    assert!(!rook.is_valid_move(types::Position { x: 0, y: 3 }, &board));
}

#[test]
fn rook_can_capture() {
    let mut board = types::Board::new();
    
    // Clear path for white rook
    board.pieces.retain(|p| p.get_position() != types::Position { x: 0, y: 1 });

    // Try to capture black pawn
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 0 },
        &types::Position { x: 0, y: 6 }
    ).is_ok());

    // Verify capture occurred
    assert!(board.is_location_empty(&types::Position { x: 0, y: 6 }) == false);
}

// ========== KNIGHT MOVEMENT TESTS ==========

#[test]
fn knight_l_shape_moves() {
    let board = types::Board::new();
    
    let knight = board.at_location(&types::Position { x: 1, y: 0 }).unwrap();
    
    // Valid L-shaped moves for knight at (1, 0)
    assert!(knight.is_valid_move(types::Position { x: 2, y: 2 }, &board));
    assert!(knight.is_valid_move(types::Position { x: 0, y: 2 }, &board));
    // (3, 1) is blocked by white pawn at (3, 1)
}

#[test]
fn knight_can_jump_pieces() {
    let mut board = types::Board::new();
    
    // Knight can jump over pawn
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 1, y: 0 },
        &types::Position { x: 2, y: 2 }
    ).is_ok());
}

#[test]
fn knight_cannot_move_to_occupied_same_color() {
    let mut board = types::Board::new();
    
    // Move white pawn forward one
    board.move_piece_with_error_checking(
        &types::Position { x: 2, y: 1 },
        &types::Position { x: 2, y: 2 }
    ).unwrap();
    
    board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 6 },
        &types::Position { x: 0, y: 5 }
    ).unwrap();

    let knight = board.at_location(&types::Position { x: 1, y: 0 }).unwrap();
    
    // Try to move to square occupied by same color pawn - should be invalid
    assert!(!knight.is_valid_move(types::Position { x: 2, y: 2 }, &board));
}

// ========== BISHOP MOVEMENT TESTS ==========

#[test]
fn bishop_move_diagonal() {
    let mut board = types::Board::new();
    
    // Clear path for white bishop
    board.move_piece_with_error_checking(
        &types::Position { x: 3, y: 1 },
        &types::Position { x: 3, y: 3 }
    ).unwrap();

    board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 6 },
        &types::Position { x: 0, y: 5 }
    ).unwrap();

    // Move bishop diagonally
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 2, y: 0 },
        &types::Position { x: 4, y: 2 }
    ).is_ok());
}

#[test]
fn bishop_cannot_move_straight() {
    let mut board = types::Board::new();
    
    // Clear pawns
    board.pieces.retain(|p| p.get_position().y != 1);

    let bishop = board.at_location(&types::Position { x: 2, y: 0 }).unwrap();
    
    // Try to move straight - should be invalid
    assert!(!bishop.is_valid_move(types::Position { x: 2, y: 3 }, &board));
    assert!(!bishop.is_valid_move(types::Position { x: 5, y: 0 }, &board));
}

#[test]
fn bishop_cannot_jump_pieces() {
    let board = types::Board::new();
    
    let bishop = board.at_location(&types::Position { x: 2, y: 0 }).unwrap();
    
    // Try to move through pawn - should be invalid
    assert!(!bishop.is_valid_move(types::Position { x: 4, y: 2 }, &board));
}

// ========== QUEEN MOVEMENT TESTS ==========

#[test]
fn queen_move_all_directions() {
    let mut board = types::Board::new();
    
    // Clear board except queens
    board.pieces.retain(|p| {
        p.get_type() == types::PieceType::QUEEN || p.get_type() == types::PieceType::KING
    });

    let queen = board.at_location(&types::Position { x: 3, y: 0 }).unwrap();
    
    // Queen can move straight
    assert!(queen.is_valid_move(types::Position { x: 3, y: 5 }, &board));
    assert!(queen.is_valid_move(types::Position { x: 1, y: 0 }, &board));
    
    // Queen can move diagonally
    assert!(queen.is_valid_move(types::Position { x: 5, y: 2 }, &board));
    assert!(queen.is_valid_move(types::Position { x: 1, y: 2 }, &board));
}

#[test]
fn queen_can_capture() {
    let mut board = types::Board::new();
    
    // Clear path for white queen
    board.pieces.retain(|p| {
        p.get_position() != types::Position { x: 3, y: 1 }
    });

    // Queen captures black pawn
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 3, y: 0 },
        &types::Position { x: 3, y: 6 }
    ).is_ok());
}

// ========== KING MOVEMENT TESTS ==========

#[test]
fn king_move_one_square() {
    let mut board = types::Board::new();
    
    // Clear space around white king
    board.pieces.retain(|p| {
        let pos = p.get_position();
        pos != types::Position { x: 3, y: 1 } &&
        pos != types::Position { x: 4, y: 1 }
    });

    let king = board.at_location(&types::Position { x: 4, y: 0 }).unwrap();
    
    // King can move one square to cleared spaces
    assert!(king.is_valid_move(types::Position { x: 4, y: 1 }, &board));
    assert!(king.is_valid_move(types::Position { x: 3, y: 1 }, &board));
}

#[test]
fn king_cannot_move_two_squares() {
    let mut board = types::Board::new();
    
    // Clear board
    board.pieces.retain(|p| p.get_type() == types::PieceType::KING);

    let king = board.at_location(&types::Position { x: 4, y: 0 }).unwrap();
    
    // King cannot move two squares
    assert!(!king.is_valid_move(types::Position { x: 4, y: 2 }, &board));
    assert!(!king.is_valid_move(types::Position { x: 6, y: 0 }, &board));
}

// ========== POSITION TESTS ==========

#[test]
fn position_add() {
    let pos1 = types::Position { x: 2, y: 3 };
    let pos2 = types::Position { x: 1, y: -2 };
    
    let result = pos1.add(pos2);
    
    assert_eq!(result.x, 3);
    assert_eq!(result.y, 1);
}

#[test]
fn position_equality() {
    let pos1 = types::Position { x: 4, y: 5 };
    let pos2 = types::Position { x: 4, y: 5 };
    let pos3 = types::Position { x: 4, y: 6 };
    
    assert_eq!(pos1, pos2);
    assert_ne!(pos1, pos3);
}

// ========== BOARD STATE TESTS ==========

#[test]
fn turn_alternates() {
    let mut board = types::Board::new();
    
    assert_eq!(board.turn, types::Side::WHITE);
    
    board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 1 },
        &types::Position { x: 0, y: 2 }
    ).unwrap();
    
    assert_eq!(board.turn, types::Side::BLACK);
    
    board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 6 },
        &types::Position { x: 0, y: 5 }
    ).unwrap();
    
    assert_eq!(board.turn, types::Side::WHITE);
}

#[test]
fn does_location_match_color() {
    let board = types::Board::new();
    
    // White piece at (0, 0)
    assert_eq!(board.does_location_match_color(&types::Position { x: 0, y: 0 }, &types::Side::WHITE), Some(true));
    assert_eq!(board.does_location_match_color(&types::Position { x: 0, y: 0 }, &types::Side::BLACK), Some(false));
    
    // Black piece at (0, 7)
    assert_eq!(board.does_location_match_color(&types::Position { x: 0, y: 7 }, &types::Side::BLACK), Some(true));
    assert_eq!(board.does_location_match_color(&types::Position { x: 0, y: 7 }, &types::Side::WHITE), Some(false));
    
    // Empty square
    assert_eq!(board.does_location_match_color(&types::Position { x: 4, y: 4 }, &types::Side::WHITE), None);
}

#[test]
fn invalid_move_returns_error() {
    let mut board = types::Board::new();
    
    // Try to move pawn sideways - should fail
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 1 },
        &types::Position { x: 1, y: 1 }
    ).is_err());
    
    // Try to move from empty square - should fail
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 4 },
        &types::Position { x: 4, y: 5 }
    ).is_err());
}

#[test]
fn invalid_move_keeps_turn_and_position() {
    let mut board = types::Board::new();

    let original_piece = board.at_location(&types::Position { x: 0, y: 1 });
    assert_eq!(board.turn, types::Side::WHITE);

    // Invalid sideways pawn move
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 1 },
        &types::Position { x: 1, y: 1 }
    ).is_err());

    // Turn and position unchanged
    assert_eq!(board.turn, types::Side::WHITE);
    assert_eq!(board.at_location(&types::Position { x: 0, y: 1 }), original_piece);
}

#[test]
fn out_of_bounds_move_rejected() {
    let mut board = types::Board::new();

    // Move beyond board limits
    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 0, y: 1 },
        &types::Position { x: 0, y: 8 }
    ).is_err());

    assert_eq!(board.turn, types::Side::WHITE);
}

#[test]
fn capture_removes_piece_and_switches_turn() {
    let mut board = types::Board::new();

    // White advances
    board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 1 },
        &types::Position { x: 4, y: 3 }
    ).unwrap();

    // Black advances
    board.move_piece_with_error_checking(
        &types::Position { x: 3, y: 6 },
        &types::Position { x: 3, y: 4 }
    ).unwrap();

    let pieces_before = board.pieces.len();

    // White captures
    board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 3 },
        &types::Position { x: 3, y: 4 }
    ).unwrap();

    assert_eq!(board.turn, types::Side::BLACK);
    assert_eq!(board.pieces.len(), pieces_before - 1);
    let captured_square = board.at_location(&types::Position { x: 3, y: 4 }).unwrap();
    assert_eq!(captured_square.get_color(), types::Side::WHITE);
}

#[test]
fn pawn_double_step_blocked_by_piece() {
    let mut board = types::Board::new();

    // Place a friendly blocker directly ahead of the pawn
    board.pieces.push(types::ChessPiece::new(
        types::PieceType::PAWN,
        types::Side::WHITE,
        types::Position { x: 4, y: 2 },
    ));

    assert!(board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 1 },
        &types::Position { x: 4, y: 3 }
    ).is_err());
}

#[test]
fn piece_symbols_correct() {
    let board = types::Board::new();
    
    // Check white pieces
    assert_eq!(board.at_location(&types::Position { x: 0, y: 0 }).unwrap().get_symbol(), '♖');
    assert_eq!(board.at_location(&types::Position { x: 1, y: 0 }).unwrap().get_symbol(), '♘');
    assert_eq!(board.at_location(&types::Position { x: 2, y: 0 }).unwrap().get_symbol(), '♗');
    assert_eq!(board.at_location(&types::Position { x: 3, y: 0 }).unwrap().get_symbol(), '♕');
    assert_eq!(board.at_location(&types::Position { x: 4, y: 0 }).unwrap().get_symbol(), '♔');
    assert_eq!(board.at_location(&types::Position { x: 0, y: 1 }).unwrap().get_symbol(), '♙');
    
    // Check black pieces
    assert_eq!(board.at_location(&types::Position { x: 0, y: 7 }).unwrap().get_symbol(), '♜');
    assert_eq!(board.at_location(&types::Position { x: 1, y: 7 }).unwrap().get_symbol(), '♞');
    assert_eq!(board.at_location(&types::Position { x: 2, y: 7 }).unwrap().get_symbol(), '♝');
    assert_eq!(board.at_location(&types::Position { x: 3, y: 7 }).unwrap().get_symbol(), '♛');
    assert_eq!(board.at_location(&types::Position { x: 4, y: 7 }).unwrap().get_symbol(), '♚');
    assert_eq!(board.at_location(&types::Position { x: 0, y: 6 }).unwrap().get_symbol(), '♟');
}

#[test]
fn knight_cannot_move_off_board() {
    let board = types::Board::new();

    let knight = board.at_location(&types::Position { x: 1, y: 0 }).unwrap();

    // Off-board destinations should be invalid
    assert!(!knight.is_valid_move(types::Position { x: -1, y: -1 }, &board));
    assert!(!knight.is_valid_move(types::Position { x: -1, y: 1 }, &board));
}

#[test]
fn queen_blocked_by_same_color() {
    let board = types::Board::new();
    let queen = board.at_location(&types::Position { x: 3, y: 0 }).unwrap();

    // White pawn at (3,1) blocks vertical move
    assert!(!queen.is_valid_move(types::Position { x: 3, y: 2 }, &board));

    // White bishop at (2,0) blocks horizontal move
    assert!(!queen.is_valid_move(types::Position { x: 1, y: 0 }, &board));
}

#[test]
fn king_cannot_capture_own_piece() {
    let board = types::Board::new();
    let king = board.at_location(&types::Position { x: 4, y: 0 }).unwrap();

    // Own pawn at (4,1) blocks capture
    assert!(!king.is_valid_move(types::Position { x: 4, y: 1 }, &board));
}

#[test]
fn index_and_empty_update_after_capture() {
    let mut board = types::Board::new();

    // White pawn advances
    board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 1 },
        &types::Position { x: 4, y: 3 }
    ).unwrap();

    // Black pawn advances to be captured
    board.move_piece_with_error_checking(
        &types::Position { x: 3, y: 6 },
        &types::Position { x: 3, y: 4 }
    ).unwrap();

    // Capture
    board.move_piece_with_error_checking(
        &types::Position { x: 4, y: 3 },
        &types::Position { x: 3, y: 4 }
    ).unwrap();

    // Captured square now holds the white pawn
    assert_eq!(board.index_at_location(&types::Position { x: 3, y: 4 }).is_some(), true);
    let occupant = board.at_location(&types::Position { x: 3, y: 4 }).unwrap();
    assert_eq!(occupant.get_color(), types::Side::WHITE);

    // Original square is empty
    assert!(board.is_location_empty(&types::Position { x: 4, y: 3 }));
}

// ========== KING SAFETY & CHECKMATE TESTS ==========

#[test]
fn king_under_attack_by_knight() {
    let pieces = vec![
        types::ChessPiece::new(types::PieceType::KING, types::Side::WHITE, types::Position { x: 4, y: 4 }),
        types::ChessPiece::new(types::PieceType::KNIGHT, types::Side::BLACK, types::Position { x: 2, y: 3 }),
    ];

    let board = types::Board { pieces, turn: types::Side::WHITE };

    assert!(board.is_king_under_attack(types::Side::WHITE));
}

#[test]
fn king_not_under_attack_when_blocked() {
    let pieces = vec![
        types::ChessPiece::new(types::PieceType::KING, types::Side::WHITE, types::Position { x: 4, y: 4 }),
        types::ChessPiece::new(types::PieceType::ROOK, types::Side::BLACK, types::Position { x: 4, y: 7 }),
        types::ChessPiece::new(types::PieceType::PAWN, types::Side::WHITE, types::Position { x: 4, y: 5 }),
    ];

    let board = types::Board { pieces, turn: types::Side::WHITE };

    assert!(!board.is_king_under_attack(types::Side::WHITE));
}

#[test]
fn checkmate_when_king_boxed_and_attacked() {
    let mut pieces = vec![
        types::ChessPiece::new(types::PieceType::KING, types::Side::WHITE, types::Position { x: 4, y: 4 }),
        types::ChessPiece::new(types::PieceType::KNIGHT, types::Side::BLACK, types::Position { x: 2, y: 3 }),
    ];

    // Surround the king with friendly pieces to block all adjacent moves
    let blockers = [
        types::Position { x: 3, y: 3 }, types::Position { x: 3, y: 4 }, types::Position { x: 3, y: 5 },
        types::Position { x: 4, y: 3 }, /* king */                       types::Position { x: 4, y: 5 },
        types::Position { x: 5, y: 3 }, types::Position { x: 5, y: 4 }, types::Position { x: 5, y: 5 },
    ];

    for pos in blockers.iter() {
        pieces.push(types::ChessPiece::new(types::PieceType::PAWN, types::Side::WHITE, *pos));
    }

    let board = types::Board { pieces, turn: types::Side::WHITE };

    assert!(board.is_king_under_attack(types::Side::WHITE));
    assert!(board.is_checkmate(types::Side::WHITE));
}

#[test]
fn not_checkmate_if_escape_square_exists() {
    let mut pieces = vec![
        types::ChessPiece::new(types::PieceType::KING, types::Side::WHITE, types::Position { x: 4, y: 4 }),
        types::ChessPiece::new(types::PieceType::KNIGHT, types::Side::BLACK, types::Position { x: 2, y: 3 }),
    ];

    // Block most adjacent squares, leave (5,5) open for escape
    let blockers = [
        types::Position { x: 3, y: 3 }, types::Position { x: 3, y: 4 }, types::Position { x: 3, y: 5 },
        types::Position { x: 4, y: 3 }, /* king */                       types::Position { x: 4, y: 5 },
        types::Position { x: 5, y: 3 }, types::Position { x: 5, y: 4 },
    ];

    for pos in blockers.iter() {
        pieces.push(types::ChessPiece::new(types::PieceType::PAWN, types::Side::WHITE, *pos));
    }

    let board = types::Board { pieces, turn: types::Side::WHITE };

    assert!(board.is_king_under_attack(types::Side::WHITE));
    assert!(!board.is_checkmate(types::Side::WHITE));
}
