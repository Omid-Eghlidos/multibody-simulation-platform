# Query Engine (queries/)

Rust crate implementing the Sedaro Nano query language parser.  
Uses [LALRPOP](https://lalrpop.github.io/lalrpop/) to handle constructs like `prev!(velocity)` and `agent!(Body2).position`.

## Structure

- **Cargo.toml** – crate manifest  
- **build.rs** – build script  
- **src/**  
  - `grammar.lalrpop` – query language grammar  
  - `lib.rs` – parser library  
  - `main.rs` – binary entrypoint  

## Build

```bash
cd queries
cargo build --release
```

## Notes

- Original Rust code preserved for compatibility.
- Integrated with Python backend to resolve simulation state dependencies.