use super::*;

#[test]
fn board_into_grid() {
    let new_board = types::Board::new();

    let correct_output = "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n* * * * * * * * \n* * * * * * * * \n* * * * * * * * \n* * * * * * * * \n♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n";

    assert_eq!(format!("{new_board}"), correct_output);
}

#[test]
fn move_piece() {
    let mut new_board = types::Board::new();

    if let Err(error) = new_board.move_piece(
        types::Position { x: 1, y: 1 },
        types::Position { x: 1, y: 3 },
    ) {
        eprintln!("Error: {error}");
        panic!();
    }

    let correct_output = "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n♙ * ♙ ♙ ♙ ♙ ♙ ♙ \n* * * * * * * * \n* ♙ * * * * * * \n* * * * * * * * \n* * * * * * * * \n♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n";

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
