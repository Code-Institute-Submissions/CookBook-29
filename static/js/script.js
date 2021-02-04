/**
 * When the user pass the mouse over a card
 * this function highlights the card
 */
function over(card){
    card.style.background = '#f1bc80'
}
/**
 * This function returns the original color of the card
 */
function out(card){
    card.style.background = '#ffeedb'
}


var coll = document.getElementsByClassName("collapsible");
var i;
/**
 * This function creates a collapsible effect in
 * ingredients and steps 
 */
for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}