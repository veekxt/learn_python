fn main() {
    //println!("Hello, world!");
    let is_she = false;
    let is_he = true;
    let c = '张';
    let arr = [3,4,5];
    let arr2:[u32;4] =[1,2,3,4];
    let s = "李四";
    struct st {
        name: String, 
    }
    impl st {
        fn new(n:&str) -> st {
            st{name: n.to_string(),}
        }
        fn print_hisname(&self) {
            println!("{}",self.name);
        }
    }
    let tao = st::new("XieTao");
    tao.print_hisname();
    print!("{}",arr2[1]);
}
