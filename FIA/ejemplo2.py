class B{
    public:
        int m, a;
        int Product1(){
            return a*m;
        }            
};

class D: public B{
    public:
        int n;
        int Product2(){
            return n*Product1();
        }
};