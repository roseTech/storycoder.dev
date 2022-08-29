fn main() {
    let iterations = 10;
    let p = 7;
    let sum : i32 = (0..iterations).map(|i| { p * (i + 1) }).sum();
    println!("{}", sum);
}
