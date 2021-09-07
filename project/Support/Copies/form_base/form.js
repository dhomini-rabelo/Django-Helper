import {adaptTextAreas} from './modules/textAreas';
import {adaptLabels} from './modules/labels';
import {setRequiredInputs, setValueForInput} from './modules/input';
import {strDate} from './modules/utils';

//! write ->  type = "module" in tag script


document.addEventListener('DOMContentLoaded', adapt_form);



function adapt_form(){




    let editLabels = true;
    let useRequiredInputs = true;
    let useValuesForInputs = true;
    let editTextAreas = true;
    



    //*--------------------------------------------------------------




    
    let optionalFields  = {
        // 'id_name': 0 -> initialIndex
    }// using id

    if (useRequiredInputs){
        /* 
        Define os campos que são requeridos
        */
        setRequiredInputs(optionalFields);
    }

    if (editLabels){
        /* 
        Edita o texto do label
        */
       adaptLabels(optionalFields);
    }
    
    if (useValuesForInputs){
        /* 
        Edita o valor do input
        */
        modifications = [
           //('id_field', 'value),
        ];//using id

        for (let i in modifications){
           setValueForInput(modifications[i][0], modifications[i][1]);
        }
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
    
}

