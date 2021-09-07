import {adaptTextAreas} from './modules/textArea';
// write ->  type = "module" in tag script

document.addEventListener('DOMContentLoaded', adapt_form);


function adapt_form(){
    let editTextAreas = true;
    
    if (editTextAreas){
        let rows = 2;
        let columns = 0;
        adaptTextAreas(columns, rows)
    }





    let weLabels = document.querySelectorAll('label')
    let weInputs = document.querySelectorAll('input')

    

    weLabels.forEach((label) => {
        if ('span' === label.innerHTML.slice(label.innerHTML.length - 6, label.innerHTML.length - 2)){
            label.innerHTML = label.innerHTML.slice(0, label.innerHTML.length - 35)
            label.innerHTML += ':'
        }else{
            label.innerHTML = `${label.innerHTML.slice(0, label.innerHTML.length - 13)}:`
        }
    })

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
