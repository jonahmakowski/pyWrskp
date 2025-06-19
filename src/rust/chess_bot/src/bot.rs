use crate::board::*;

pub fn find_all_valid_moves(board: &Board, color: &String) -> Vec<(i32, i32, i32)> {
    let mut valid_moves = Vec::new();
    for piece in &board.pieces {
        if piece.color != *color {
            continue;
        }
        let (x, y) = (piece.x, piece.y);
        let moves = &piece.moves;
        for (index, &(_, _)) in moves.iter().enumerate() {
            if board.valid_move(x, y, index as i32) {
                valid_moves.push((x, y, index as i32));
            }
        }
    }
    return valid_moves; // (x, y, move_index)
}

fn most_score_move(
    board: &Board,
    color: &String,
    moves: Vec<(i32, i32, i32)>,
) -> Option<(i32, i32, i32, bool)> {
    let mut best_move = None;
    let mut best_score = i32::MIN;
    let mut has_king = true;

    for (x, y, move_index) in moves {
        let mut temp_board = board.deep_clone();
        temp_board.move_piece(x, y, move_index);
        let score = temp_board.count_score(color);

        if score.0 > best_score && score.1 {
            best_score = score.0;
            best_move = Some((x, y, move_index, has_king));
        }
    }

    best_move
}

pub fn play_best_move(board: &mut Board, color: &String, ahead: i32) {
    let moves = find_all_valid_moves(&board, &color);
    let mut move_scores = Vec::new();
    let mut index_to_play = 0;
    let mut score_to_play = 0;
    let mut enemy_score_to_play = 0;
    let mut my_score_to_play = 0;

    for m in &moves {
        let (x, y, move_index) = m;
        let mut move_board = board.deep_clone();
        move_board.move_piece(x.clone(), y.clone(), move_index.clone());
        let turn_result =
            find_best_move(&mut move_board, &color, ahead - 1, 0, *x, *y, *move_index);
        move_scores.push(turn_result);
    }

    let mut max_score = i32::MIN;
    let mut to_play = (0, 0, 0);

    for moves in move_scores {
        for inner_moves in moves {
            for (
                index,
                (has_king_me, has_king_enemy, score, enemy_score, depth, x, y, move_index),
            ) in inner_moves.into_iter().enumerate()
            {
                println!(
                    "Move: ({}, {}, {}) \t Score: {} \t Enemy Score: {} \t Depth: {}",
                    x, y, move_index, score, enemy_score, depth
                );
                if score - enemy_score > max_score && has_king_me {
                    to_play = (x, y, move_index);
                    max_score = score - enemy_score;
                    index_to_play = index;
                    score_to_play = score - enemy_score;
                    enemy_score_to_play = enemy_score;
                    my_score_to_play = score;
                }
            }
        }
    }
    // has_king_me, has_king_enemy, score, enemy_score, depth, x, y, move_index

    println!("Max score: {}", max_score);
    println!(
        "Playing move: ({}, {}, {}) with score {} me: {} enemy: {}",
        to_play.0, to_play.1, to_play.2, score_to_play, my_score_to_play, enemy_score_to_play
    );
    board.move_piece(to_play.0, to_play.1, to_play.2);
}

pub fn find_best_move(
    board: &Board,
    color: &String,
    ahead: i32,
    depth: i32,
    move_x: i32,
    move_y: i32,
    move_index: i32,
) -> Vec<Vec<(bool, bool, i32, i32, i32, i32, i32, i32)>> {
    //returns a vec with has_king_me, has_king_enemy, score, enemy_score, depth, x, y, move_index
    if ahead == 0 {
        return vec![vec![(
            board.count_score(color).1,
            board.count_score(&board.get_opponent_color(color)).1,
            board.count_score(color).0,
            board.count_score(&board.get_opponent_color(color)).0,
            depth,
            move_x,
            move_y,
            move_index,
        )]];
    }

    let moves = find_all_valid_moves(board, color);
    if moves.is_empty() {
        return vec![vec![(
            board.count_score(color).1,
            board.count_score(&board.get_opponent_color(color)).1,
            board.count_score(color).0,
            board.count_score(&board.get_opponent_color(color)).0,
            depth,
            move_x,
            move_y,
            move_index,
        )]];
    }

    let mut best_moves = Vec::new();
    for (x, y, move_index) in moves {
        let mut temp_board = board.deep_clone();
        if temp_board.turn != *color {
            let opponent_color = temp_board.get_opponent_color(&color);

            let moves = find_all_valid_moves(&temp_board, &opponent_color);
            let (enemy_move_x, enemy_move_y, enemy_move_index, _) =
                most_score_move(&temp_board, &opponent_color, moves)
                    .expect("Failed to find a valid enemy move");
            temp_board.move_piece(enemy_move_x, enemy_move_y, enemy_move_index);
            // println!("Enemy move: ({}, {}, {})", enemy_move_x, enemy_move_y, enemy_move_index);
        }
        temp_board.move_piece(x, y, move_index);
        let next_moves =
            find_best_move(&temp_board, &color, ahead - 1, depth + 1, x, y, move_index);
        best_moves.extend(next_moves);
    }

    best_moves
}
