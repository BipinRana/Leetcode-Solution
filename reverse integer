/*Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
*/
int reverse(int x){
int ans=0;
bool s;
if(x<-2147483647){
    return 0;
}
s=(x>0)?true:false;
x=(x>0)?x:-x;
while (x>0){
    if(ans>214748364){
        return 0;
    }
ans= ans * 10+ x % 10;
x=x/10;
}
if(s){
    return ans;
}
else{
    return -ans;
}
}
