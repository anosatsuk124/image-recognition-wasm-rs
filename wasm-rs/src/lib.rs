use wasm_bindgen::prelude::*;
extern crate wee_alloc;
mod bindings;

#[global_allocator]
static ALLOC: wee_alloc::WeeAlloc = wee_alloc::WeeAlloc::INIT;

#[wasm_bindgen(start)]
pub fn main() {
    console_log!("Hello");
}
