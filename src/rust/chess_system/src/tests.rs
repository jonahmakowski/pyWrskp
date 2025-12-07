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

    if let Err(error) = new_board.move_piece(types::Position {x: 1, y: 1}, types::Position {x: 1, y: 3}) {
        eprintln!("Error: {error}");
        panic!();
    }

    let correct_output = "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n♙ * ♙ ♙ ♙ ♙ ♙ ♙ \n* * * * * * * * \n* ♙ * * * * * * \n* * * * * * * * \n* * * * * * * * \n♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n";

    assert_eq!(format!("{new_board}"), correct_output);
}
