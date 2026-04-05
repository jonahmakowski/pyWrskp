use crate::{types, user_interface};
use std::cmp::{max, min};

#[derive(Clone, PartialEq, Debug, Copy)]
struct Move <'a> {
    pub piece: &'a types::ChessPiece,
    pub new_position: types::Position,
    pub old_position: types::Position,
}

fn find_all_current_moves(board: &types::Board, color: types::Side) -> Vec<Move<'_>> {
    let mut moves: Vec<Move<'_>> = Vec::new();

    for piece in &board.pieces {
        if piece.get_color() != color {
            continue;
        }

        let piece_moves = piece.valid_moves(board);
        for m in &piece_moves {
            moves.push(Move {
                piece,
                new_position: m.1,
                old_position: m.0,
            })
        }
    }

    moves
}

fn new_board_with_move(board: &types::Board, to_move: Move) -> types::Board {
    let mut new_board = board.clone();
    new_board.move_piece_without_error_checking(&to_move.old_position, &to_move.new_position).unwrap();
    new_board
}

// White is trying to maximize
fn minimax(cur_position: &types::Board, depth: i64, mut best_white_score: i32, mut best_black_score: i32, side: types::Side) -> i32 {
    if depth == 0 || cur_position.is_checkmate(types::Side::BLACK) || cur_position.is_checkmate(types::Side::WHITE) {
        return cur_position.get_score().make_relative()
    }

    if side == types::Side::WHITE {
        let mut max_eval = -10000;
        for possible_move in find_all_current_moves(cur_position, side) {
            let eval = minimax(&new_board_with_move(cur_position, possible_move), depth-1, best_white_score, best_black_score, side.opposite());
            max_eval = max(max_eval, eval);
            best_white_score = max(best_white_score, eval);
            
            if best_black_score <= best_white_score {
                break;
            }
        }

        return max_eval
    } else {
        let mut min_eval = 10000;
        for possible_move in find_all_current_moves(cur_position, side) {
            let eval = minimax(&new_board_with_move(cur_position, possible_move), depth-1, best_white_score, best_black_score, side.opposite());
            min_eval = max(min_eval, eval);
            best_white_score = min(best_white_score, eval);
            
            if best_white_score <= best_black_score {
                break;
            }
        }

        return min_eval
    }
}

fn bot_move(cur_position: &mut types::Board, side: types::Side, depth: i64) {
    let mut best_score = if side == types::Side::BLACK { 10000 } else { -10000 };
    let mut best_move: Option<Move> = None; 
    for possible_move in find_all_current_moves(cur_position, side) {
        let eval = minimax(&new_board_with_move(cur_position, possible_move), depth, -10000, 10000, side.opposite());
        
        if (eval > best_score && side == types::Side::WHITE) || (eval < best_score && side == types::Side::BLACK) {
            best_score = eval;
            best_move = Some(possible_move);
        }
    }

    match best_move {
        Some(best_move_data) => cur_position.move_piece_without_error_checking(&best_move_data.old_position, &best_move_data.new_position).expect("Couldn't move piece"),
        None => panic!("No valid piece for side {:#?}", side),
    }
}

pub fn play_against_bot(depth: i64) {
    let mut board = types::Board::new();

    loop {
        print!("{}[2J", 27 as char);
        println!(
            "{}'s turn",
            if board.turn == types::Side::WHITE {
                "White"
            } else {
                "Black"
            }
        );
        println!("{board}");

        if board.turn == types::Side::WHITE {
            println!("Enter the position of where you want to move from in the format of: x, y");
            let from_pos = match user_interface::get_position_from_input() {
                Ok(pos) => pos,
                Err(_) => continue,
            };

            println!("Enter the position of where you want to move to in the format of: x, y");
            let to_pos = match user_interface::get_position_from_input() {
                Ok(pos) => pos,
                Err(_) => continue,
            };

            match board.move_piece_with_error_checking(&from_pos, &to_pos) {
                Ok(_) => (),
                Err(e) => println!("{e}"),
            }
        } else {
            bot_move(&mut board, types::Side::BLACK, depth)
        }

        if board.is_checkmate(types::Side::WHITE) {
            println!("Black won!");
            break;
        }

        if board.is_checkmate(types::Side::BLACK) {
            println!("White won!");
            break;
        }
    }
}
