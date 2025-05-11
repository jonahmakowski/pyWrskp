use std::process::Command;
use walkdir::WalkDir;

fn main() {
    for entry in WalkDir::new("../../").into_iter().filter_map(|e| e.ok()) {
        if entry.path().to_string_lossy().contains("Cargo.toml") {
            let folder = entry.path().parent().unwrap();
            Command::new("cargo")
                .arg("fmt")
                .current_dir(folder)
                .status()
                .expect("Failed to format Rust code");
            println!("Found Rust folder: {}", entry.path().display());
        }
    }
}
