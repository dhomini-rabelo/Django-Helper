import {adaptTextAreas} from './modules/textAreas';
import {adaptLabels} from './modules/labels';
import {setRequiredInputs, setValueForInput, changeTypeInput} from './modules/input';
import { addMask, forMoneyBRMask } from './modules/masks';
import { inputValidator } from './modules/validateInput';
import {strDate} from './modules/utils';

//! write ->  type = "module" in tag script



document.addEventListener('load', adaptForm);
// DOMContentLoaded


function adaptForm(){




    let useValuesForInputs = false;
    let editTypeOfInputs = false;
    let useRequiredInputs = false;
    let editLabels = false;
    let editTextAreas = false;
    let useMasks = false;
    let useInputValidator = false;
    



    //*--------------------------------------------------------------




    if (useValuesForInputs){
        /* 
        Edita o valor do input
        */
        let modifications = [
           //('id_field', value),
        ];//using id

        for (let i in modifications){
           setValueForInput(modifications[i][0], modifications[i][1]);
        }
    }



    if (editTypeOfInputs){
        /* 
        Edita o tipo do input
        */
        let modifications = [
            //('id_field', newType),
         ];//using id
 
         for (let i in modifications){
            changeTypeInput(modifications[i][0], modifications[i][1]);
         }        
    }



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
    


    if (editTextAreas){
        /* 
        Controla tamanho da tag textarea no form, se
        columns = 0, ele utiliza o valor padrão do form
        */
        let rows = 2;
        let columns = 0;
        adaptTextAreas(columns, rows);
    }


    
    if (useMasks){
        //! <script src="https://cdn.jsdelivr.net/npm/cleave.js@1.6.0/dist/cleave.min.js"></script>
        let modifications = [
            //('id_field', mask),
        ];//using id
        let allowedMasks = ['cpf', 'cnpj', 'phoneBR', 'dateBR', 'moneyBR', 'card', 'numericOnly', 'numericPositiveOnly', 'securityPasswordCard']
        for (let i in modifications){
            addMask(modifications[i][0], modifications[i][1]);
        }  
        // case moneyBR in modifications 
        // forMoneyBRMask(idInput);
    }



    if (useInputValidator){
        let idInputs = [
            //'id'
        ];
        let inputs = [];
        for(let idInput in idInputs) {
            let input = document.querySelector(idInput);
            inputs.push(input);
        }
        inputs.forEach((input) => {
            input.addEventListener('blur', inputValidator);
        });
    }
}

