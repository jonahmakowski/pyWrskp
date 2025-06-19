fn main() {
    const START: i32 = 1;
    const END: i32 = 100;

    let mut result: i128 = START.into();

    println!("Fibonacci sequence:");
    for i in START..=END {
        result = fibonacci(result);
        println!("Fibonacci of {} is {}", i, result);
    }
}

fn fibonacci(n: i128) -> i128 {
    n + n
}
