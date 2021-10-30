import { addMask } from './modules/masks.js'
import { forMoneyBRMask, strMask, forDateBRMask } from './modules/functions.js'



//! write ->  type = "module" in tag script
// test use class needs-validation



document.addEventListener('DOMContentLoaded', functionsForForm)
// DOMContentLoaded



function functionsForForm(){


    let useMasks = false





    if (useMasks){
        //! <script src="https://cdn.jsdelivr.net/npm/cleave.js@1.6.0/dist/cleave.min.js"></script>
        //! Adaptado para uso com input do tipo text
        let modifications = [
            //['id_field', mask],
        ]//using id
        let allowedMasks = ['cpf', 'cnpj', 'phoneBR', 'dateBR', 'moneyBR', 'card', 'numericOnly', 'numericPositiveOnly', 'securityPasswordCard']
        for (let i in modifications){
            addMask(modifications[i][0], modifications[i][1])
        } 
        //* Functions
        // case mask for string --> strMask(idInput, False)
        // case moneyBR in modifications  --> forMoneyBRMask(idInput)
        // case dateBR in modifications  --> forDateBRMask(idInput)
    }

}
