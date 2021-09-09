function cpfMask(idInput) {
    new Cleave(idInput, {
        delimiters: ['.', '.', '-'],
        blocks: [3, 3, 3, 2],
        numericOnly: true
        });
}

function cnpjMask(idInput) {
    new Cleave(idInput, {
        delimiters: ['.', '.', '/', '-'],
        blocks: [3, 3, 3, 5, 2],
        numericOnly: true
    });
}

function phoneBRMask(idInput) {
    new Cleave(idInput, {
        delimiters: ['(', ') ', '-'],
        blocks: [0, 2, 5, 4],
        numericOnly: true
        });
}

function moneyBRMask(idInput) {
    new Cleave(idInput, {
        prefix: 'R$ ',        
        numeral: true,
        numeralDecimalMark: ',',
        delimiter: '.'
        });
}

function dateBRMask(idInput) {
    new Cleave(idInput, {
        date: true,
        // dateMin: '2000-01-01',
        dateMax: '2100-01-01',
        delimiters: ['/', '/'],
        datePattern: ['d', 'm', 'Y']
        });
}

function cardMask(idInput) {
    new Cleave(idInput, {
        delimiters: [' ', ' ', ' '],
        blocks: [4, 4, 4, 4],
        numericOnly: true
        });
}

function numericOnlyMask(idInput) {
    new Cleave(idInput, {
        numeral : true , 
        delimiter: '',
        });
}

function numericPositiveOnlyMask(idInput) {
    new Cleave(idInput, {
        numeral : true , 
        delimiter: '',
        numeralPositiveOnly : true 
        });
}

function securityPasswordCardMask(idInput) {
    new Cleave(idInput, {
        date: true,
        delimiter: '/',
        datePattern: ['m', 'y']
        });
}


export function addMask(idInput, mask){
    if (mask==='cpf'){
        cpfMask(idInput)
    }
    else if (mask==='cnpj'){
        cnpjMask(idInput)
    }
    else if (mask==='phoneBR'){
        phoneBRMask(idInput)
    }
    else if (mask==='moneyBR'){
        moneyBRMask(idInput)
    }
    else if (mask==='dateBR'){
        dateBRMask(idInput)
    }
    else if (mask==='card'){
        cardMask(idInput)
    }
    else if (mask==='numericOnly'){
        numericOnlyMask(idInput)
    }
    else if (mask==='numericPositiveOnly'){
        numericPositiveOnlyMask(idInput)
    }
    else if (mask==='securityPasswordCard'){
        securityPasswordCardMask(idInput)
    }

}


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