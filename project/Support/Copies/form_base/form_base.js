import {adaptTextAreas} from './modules/textAreas';
import {adaptLabels} from './modules/labels';

//! write ->  type = "module" in tag script

document.addEventListener('DOMContentLoaded', adapt_form);


function adapt_form(){
    let editLabels = true;
    let editTextAreas = true;
    
    
    let optionalFields  = {
        // 'nome': 'i'
    }

    if (editLabels){
        /* 
        Edita o texto do label
        */
       adaptLabels(optionalFields);
    }
    
    if (editTextAreas){
        /* 
        Controla tamanho da tag textarea no form, se
        columns = 0, ele utiliza o valor padrão do form
        */
        let rows = 2;
        let columns = 0;
        adaptTextAreas(columns, rows);
    }
    



    let weInputs = document.querySelectorAll('input')

    

    

    weInputs.forEach((input) => {
        let type = input.getAttribute('type')
        let name = input.getAttribute('name')
        let nameExceptions = {'nome_user':1, 'email_user':3, 'bio':2, 'telefone_pessoal': 6}
        if ((type !== 'file' && type !== 'submit' && type !== 'hidden')&&(!(name in nameExceptions))){
            input.setAttribute('required', '')
            input.setAttribute('value', '')
        }
        if (type === 'text' && input.getAttribute('name').slice(0, 4) == 'data'){
            input.setAttribute('type', 'date')
            input.setAttribute('value', strDate())
        }
    })
}

function adaptTheTime(day, month){
    if (day>=10&&month>=10){
        return `${month+1}-${day}`
    }else if (day>=10&&month<10){
        return `0${month+1}-${day}`
    }else if (day<10&&month>=10){
        return `${month+1}-0${day}`
    }else if (day<10&&month<10){
        return `0${month+1}-0${day}`
    }
}
    

function strDate(){
    let date = new Date()
    let year = date.getFullYear()
    let month = date.getMonth()
    let day = date.getDate()
    let summaryDate = adaptTheTime(day, month)
    return `${year}-${summaryDate}`
}
