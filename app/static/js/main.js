var boton = document.getElementById("btn");


boton.onclick = function(){
    var inpu1 = document.getElementById("input1").value;
    var inpu2 = document.getElementById("input2").value;
    var inpu3 = document.getElementById("input3").value;
    
    if (inpu1 == "" ||inpu2 == "" ||inpu3 == ""){
        alert("There's any empty space, please try again")
    }
}