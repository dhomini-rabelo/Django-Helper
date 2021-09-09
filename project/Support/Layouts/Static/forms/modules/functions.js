export function forMoneyBRMask(idInput){
    let input = document.querySelector(idInput);
    input.addEventListener('focus', moneyBRFocus);
    input.addEventListener('blur', moneyBRBlur);


    function moneyBRFocus(){
        if (input.value === "R$ 0,00"){
            input.value = 'R$ ';
        }
    }   

    function moneyBRBlur(){
        let commaPosition = input.value.indexOf(',');
        let sizeTxt = input.value.length;
        if (commaPosition == -1){
            if (input.value.length > 3){
                input.value += ',00';
            }else{
                input.value += '0,00';
            }
        }else if (commaPosition == 3){
            input.value = 'R$ 0,00';
        }else if (commaPosition == sizeTxt - 1){
            input.value += '00';
        }else if (commaPosition == sizeTxt - 2){
            input.value += '0';
        }
    }
}

export function toTitleCase(str){
    let newStr = '';
    for (let c in str){
        if (c === 0 || str[c-1] === " "){
            newStr += str.toUpperCase();
        }else{
            newStr += str.toLowerCase();
        }
    }

}

export function strMask(idInput, useTitleCase){
    let weInput = document.querySelector(idInput);
    weInput.addEventListener('blur', onlyLetters);
    
    function onlyLetters(e){
        let text = e.target.value;
        let newText = '';
        for (letter of text){
            if (isNaN(letter)){
                newText += letter;
            }
        }   
        e.target.value = useTitleCase ? newText : toTitleCase(newText);
    }
}

