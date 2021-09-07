var notPermissionTypes = {
    'file': 0,
    'submit': 0,
    'hidden': 0
}


export function setRequiredInputs(optionals){
    let weInputs = document.querySelectorAll('input');

    weInputs.forEach((input) => {
        let type = input.getAttribute('type');
        let idInput = input.getAttribute('id');
        
        if ((!(type in notPermissionTypes))&&(!(idInput in optionals))){
            input.setAttribute('required', '');
        }

    });
}

export function setValueForInput(idInput, value){
    let input = document.querySelector(`input#${idInput}`);

    let type = input.getAttribute('type');
    let idInput = input.getAttribute('id');
    
    if ((!(type in notPermissionTypes))&&(!(idInput))){
        input.setAttribute('value', value);
    }
}