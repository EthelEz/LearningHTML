// Learning Event Handling with jQuery

// // Clicks
// var xx = $('h1')
// xx.click(function() {
//   console.log('There was a Click');
// })
//
// var yy = $('li')
// yy.dblclick(function() {
//   console.log('any li was double clicked');
// })
//
// // You use 'this' keyword to call a method in jQuery
//
// this.xx.text('I was changed')
//
// // // or
// // $('h1').click(function() {
// //   $(this).text('I was changed')
// // })

// Interacting with the Keyboard(KEY Press) using the jQuery.
// $('input').eq(0).keypress(function() {
//   console.log('I am pressed');
// })

$('input').eq(0).keypress(function() {
  $('input').eq(1).toggleClass('turnRed')
})

$('input').eq(0).keypress(function(event) {
  console.log(event);
})

// NB: The 'which' parameter in event log logs the number of keyboards when typed.
// we can use this to report certain event when they happen to the keyboard, eg.

$('input').eq(0).keypress(function(event) {
  if (event.which === 110){
    $('h3').toggleClass('turnRed')
  }
})
// Also you can google online for the numerical codes of specific keys on your keyboard
// here 13 is the enter key for windows and 110 is n

// another event function we'd look at is the on().EG on doublclicking h1, turn turnBrown
$('h1').on('dblclick', function(){
  $(this).toggleClass('turnBlue')
})

$('h3').on('mouseenter', function(){
  $(this).toggleClass('turnBlue')
})

// Talking about event and annimations, lets go there. You can go api.jquery.com/category/effects
// to get more infor on effects/

// $('input').eq(1).on('click', function() {
//   $('.container').fadeOut(300)
// })

$('input').eq(1).on('click', function() {
  $('.container').slideUp(300)
})
