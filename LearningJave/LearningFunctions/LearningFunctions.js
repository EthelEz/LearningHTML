// function hello(){
//   console.log("Hello the United Kingdom!");
// }

// function HeyYou(name){
//   console.log("Hello "+name);
// }
 // function addNum(num1, num2) {
 //  console.log(num1 + num2);
 // }

 // function helloSomeone(name="Ethels") {
 //   console.log("Hello "+name);
 // }

 // function formal(name="Sam", title="Dr") {
 //   return title + " "+name;
 // }

// function timeFive(numInput) {
//   // The result and numInput has local scope to the function.
//   var result = (numInput*5)
//   return result
// }

var v = " GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside func"
  console.log(stuff);

}

fun()
console.log(stuff);
