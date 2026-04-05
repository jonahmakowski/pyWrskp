use crate::types;

pub fn get_position_from_input() -> Result<types::Position, &'static str> {
    let position_string = match simple_lib::input::get_string_input() {
        Ok(val) => val,
        Err(e) => {
            eprintln!("Something Went wrong Error: {e}");
            return Err("Something Went wrong");
        }
    };

    let position_parsed: Vec<i8> = position_string
        .split(", ")
        .map(|item| item.trim().parse().unwrap_or(-1))
        .collect();

    if position_parsed.contains(&-1) || position_parsed.len() != 2 {
        println!("Please enter two numbers");
        return Err("Didn't input correct numbers");
    }

    Ok(types::Position {
        x: position_parsed[0],
        y: position_parsed[1],
    })
}

pub fn player_vs_player() {
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

        println!("Enter the position of where you want to move from in the format of: x, y");
        let from_pos = match get_position_from_input() {
            Ok(pos) => pos,
            Err(_) => continue,
        };

        println!("Enter the position of where you want to move to in the format of: x, y");
        let to_pos = match get_position_from_input() {
            Ok(pos) => pos,
            Err(_) => continue,
        };

        match board.move_piece_with_error_checking(&from_pos, &to_pos) {
            Ok(_) => (),
            Err(e) => println!("{e}"),
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
