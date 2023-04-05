var opt1 = document.getElementById("number8")
var opt2 = document.getElementById("number9")
var opt3 = document.getElementById("number10")
var opt4 = document.getElementById("number11")
var opt5 = document.getElementById("number13")
var opt6 = document.getElementById("number14")
var opt7 = document.getElementById("number16")

var values = [opt1.innerText, opt2.innerText, opt3.innerText, opt4.innerText, opt5.innerText, opt6.innerText, opt7.innerText]

var highestValue = Math.max(...values)
 


if (opt1.innerText == highestValue)
{
    
    var win = document.getElementById("votes8").style.backgroundColor = "#94b78f";
    opt1.innerHTML += "<b>CURRENTLY WINNING<b/>";

}

if(opt2.innerText == highestValue)
{
    
    var win = document.getElementById("votes9").style.backgroundColor = "#94b78f";
    opt2.innerHTML += "<b>CURRENTLY WINNING<b/>";
}


if(opt3.innerText == highestValue)
{
    
    var win = document.getElementById("votes10").style.backgroundColor = "#94b78f";
    opt3.innerHTML += "<b>CURRENTLY WINNING<b/>";
}

if(opt4.innerText == highestValue)
{
    
    var win = document.getElementById("votes11").style.backgroundColor = "#94b78f";
    opt4.innerHTML += "<b>CURRENTLY WINNING<b/>";
}

if(opt5.innerText == highestValue)
{
    
    var win = document.getElementById("votes13").style.backgroundColor = "#94b78f";
    opt5.innerHTML += "<b>CURRENTLY WINNING<b/>";
}

if(opt6.innerText == highestValue)
{
    
    var win = document.getElementById("votes14").style.backgroundColor = "#94b78f";
    opt6.innerHTML += "<b>CURRENTLY WINNING<b/>";
}

if(opt7.innerText == highestValue)
{
    
    var win = document.getElementById("votes16").style.backgroundColor = "#94b78f";
    opt7.innerHTML += "<b>CURRENTLY WINNING<b/>";
    
}


