alert("Hello world, Como estas Gerardo?");

document.getElementById("submit-button").addEventListener("click",submitForm,true);

function submitForm(){
    var inputBox = document.getElementById("link-to-shorten");// value to get element from inside
    var linkToShorten = inputBox.value;
    // rename to input box
    if(isFormatIncorrect(linkToShorten)){
        alert("Please input a valid input in the box")
        inputBox.style.borderColor = "red";
    }
}

function isFormatIncorrect(link){
    return (typeof link === "string" && link.length === 0)
}

function isUserInputEmpty(){


}

function isLinkCurrentlyWorking(){

}